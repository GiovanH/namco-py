import re
import textwrap
import collections
import nc_hardcoded

TextStore = nc_hardcoded.TextStore.copy()
ActorPrevStore = collections.defaultdict(default=None)
JumpLabelStore = []


class NodeContainer():
    def toRpy(self, sublabel):
        lines = (c.toRpy(sublabel=sublabel) for c in self.children)
        return "\n".join((l for l in lines if l))

class NoScript():
    def toRpy(self, sublabel):
        return None

def textToRpyInterp(text):
    text = re.sub(r"([\\\"])", r"\\\g<1>", text)
    text = re.sub(r"\${(.+):(.+?)}", "[\g<1>__\g<2>]", text)
    return text

def fixname(char):
    fixes = {
        "t_ch_tutorial": "narrator",
        # "max": "bluemax",
    }
    return fixes.get(char, char)

sceneid = ""

class Scene(NodeContainer):
    def __init__(self, id, children):
        super(Scene, self).__init__()
        self.id = id
        self.children = children
        global sceneid
        sceneid = self.id.replace('.', '_')

    @classmethod
    def fromTag(cls, xml):
        children = []
        for tag in xml.findAll(recursive=False):
            if tag.name == "assets":
                children.append(Assets.fromTag(tag))
            elif tag.name == "events":
                children.append(Events.fromTag(tag))
            else:
                raise NotImplementedError(tag.name)
        return cls(xml['id'], children)

    def __repr__(self):
        return f"<{self.__class__.__name__} {self.id=}>"

    def toRpy(self, sublabel=None):
        new_sublabel = self.id.replace('.', '_')
        body = NodeContainer.toRpy(self, sublabel=new_sublabel)
        return f"label {new_sublabel}:\n" + textwrap.indent(body, "    ")
        
class Assets(NodeContainer):
    def __init__(self, children):
        super(Assets, self).__init__()
        self.children = children

    @classmethod
    def fromTag(cls, xml):
        children = []
        for tag in xml.findAll(recursive=False):
            if tag.name == "TextAsset":
                children.append(TextAsset.fromTag(tag))
            else:
                raise NotImplementedError(tag.name)
        return cls(children)

    def __repr__(self):
        return f"<{self.__class__.__name__}\n{self.children}>"

class TextAsset(NoScript):
    def __init__(self, key, value):
        super(TextAsset, self).__init__()
        self.key = key
        self.value = value
        global TextStore
        TextStore[key] = value

    @classmethod
    def fromTag(cls, xml):
        return cls(
            key=xml.attrs['key'], 
            value=xml.find(key="en").text
        )

    def __repr__(self):
        return f"<{self.__class__.__name__} {self.key=}, {self.value=}"

class Events(NodeContainer):
    def __init__(self, children):
        super(Events, self).__init__()
        self.children = children

    @classmethod
    def fromTag(cls, xml):
        children = []
        for tag in xml.findAll(recursive=False):
            tag.name = tag.name.lower()
            try:
                if tag.name == 'actorcrossfade': 
                    children.append(EventUnhandled.fromTag(tag))
                elif tag.name == 'actorevent': 
                    children.append(EventUnhandled.fromTag(tag))
                elif tag.name == 'actorcreate': 
                    children.append(EventActorCreate.fromTag(tag))
                elif tag.name == 'actordepth': 
                    children.append(EventUnhandled.fromTag(tag))
                elif tag.name == 'actorfade': 
                    children.append(EventActorfade.fromTag(tag))
                elif tag.name == 'actorflip': 
                    children.append(EventUnhandled.fromTag(tag))
                elif tag.name == 'actorimage': 
                    children.append(EventActorImage.fromTag(tag))
                elif tag.name == 'actormove': 
                    children.append(EventUnhandled.fromTag(tag))
                elif tag.name == 'actordestroy': 
                    children.append(EventUnhandled.fromTag(tag))
                elif tag.name == 'actorscale': 
                    children.append(EventUnhandled.fromTag(tag))
                elif tag.name == 'actorreset': 
                    children.append(EventUnhandled.fromTag(tag))

                elif tag.name == 'audioevent': 
                    children.append(EventUnhandled.fromTag(tag))
                elif tag.name == 'audiocreate': 
                    children.append(EventAudioplay.fromTag(tag, "music"))
                elif tag.name == 'audiodestroy': 
                    children.append(EventUnhandled.fromTag(tag))
                elif tag.name == 'audiooneshot': 
                    children.append(EventAudioplay.fromTag(tag, "sound"))

                elif tag.name == 'jumpevent': 
                    children.append(EventJump.fromTag(tag))
                elif tag.name == 'yesnochoice': 
                    children.append(EventUnhandled.fromTag(tag))
                elif tag.name == 'consoleevent': 
                    children.append(EventUnhandled.fromTag(tag))

                elif tag.name in {'ifequal', 'ifgte', 'iflte'}: 
                    children.append(EventCompare.fromTag(tag))
                elif tag.name in {'iftrue', 'iffalse'}: 
                    children.append(EventTest.fromTag(tag))

                elif tag.name == 'creditsevent': 
                    children.append(EventUnhandled.fromTag(tag))
                elif tag.name == 'lockoutchoice': 
                    children.append(EventUnhandled.fromTag(tag))
                elif tag.name == 'fadeevent': 
                    children.append(EventActorfade.fromTag(tag))
                elif tag.name == 'gameover': 
                    children.append(EventUnhandled.fromTag(tag))
                elif tag.name == 'hardswap': 
                    children.append(EventUnhandled.fromTag(tag))
                elif tag.name == 'nhscenechange': 
                    children.append(EventJump.fromTag(tag))
                elif tag.name == 'parallelevent': 
                    children.append(EventParallel.fromTag(tag))
                elif tag.name == 'settingchange': 
                    children.append(EventUnhandled.fromTag(tag))
                elif tag.name == 'textevent': 
                    children.append(EventText.fromTag(tag))

                elif tag.name == 'varensure': 
                    children.append(EventVardefine.fromTag(tag))
                elif tag.name == 'varset': 
                    children.append(EventUnhandled.fromTag(tag))
                elif tag.name == 'varinc': 
                    children.append(EventUnhandled.fromTag(tag))

                elif tag.name == 'macro': 
                    children.append(EventMacro.fromTag(tag))
                elif tag.name == 'battlemacro': 
                    children.append(EventNamedmacro.fromTag(tag))
                elif tag.name == 'silhouettemacro': 
                    children += MacroSilhouette(tag)
                elif tag.name == 'explorationmacro': 
                    children.append(EventNamedmacro.fromTag(tag))
                elif tag.name == 'branchmacro': 
                    children.append(EventNamedmacro.fromTag(tag))
                elif tag.name == 'normalendmacro': 
                    children.append(EventNamedmacro.fromTag(tag))
                elif tag.name == 'badendmacro': 
                    children.append(EventNamedmacro.fromTag(tag))
                elif tag.name == 'supersecretmacro': 
                    children.append(EventNamedmacro.fromTag(tag))
                else:
                    raise NotImplementedError(tag.name)
            except:
                print(tag.prettify())
                raise
        return cls(children)

    def __repr__(self):
        return f"<{self.__class__.__name__} {self.children}>"



def MacroExploration(tag):
    # <ExplorationMacro lockout="false" name="day0choice" passText="@t_ui_waitfordetention" sceneName="day0" />

    return [
        EventActorCreate("", id=tag['silActor'], image=tag['silImage'], style={}),
        EventActorCreate("", id=tag['realActor'], image=tag['realImage'], style={}),
        EventActorImage("", target=tag['realActor'], image=tag['realImage']),
        EventText("", char=tag['actorName'], text=tag['firstText']),
    ] + ([EventText("", char=tag['actorName'], text=tag['secondText'])] if tag.get('secondText') else [])
        


def MacroSilhouette(tag):
    # actorName="@t_ch_donko" actorScaleX="0.75" actorScaleY="0.75" actorY="12.5%" 
    # appendSecond="true" cousinActor="cousin" cousinScaleX="1" cousinX="-20%"
    # firstText="@t_sintro21.00" name="_u" realActor="alt1" realImage="@i_donko_akimbo_wink"
    # secondText="@t_sintro21.01" silActor="alt1_sil" silImage="@i_donko_akimbo_sil"

    # Text & sil simultaneously
    # Then cousin moves
    # Then second text and reveal

    # TODO: missing transformation, sil, etc

    return [
        EventActorCreate("", id=tag['silActor'], image=tag['silImage'], style={}),
        EventActorCreate("", id=tag['realActor'], image=tag['realImage'], style={}),
        EventActorImage("", target=tag['realActor'], image=tag['silImage']),
        EventText("", char=tag['actorName'], text=tag['firstText']),
        EventActorImage("", target=tag['realActor'], image=tag['realImage']),
    ] + ([EventText("", char=tag['actorName'], text=tag['secondText'])] if tag.get('secondText') else [])
        

class Event(NoScript):
    def __init__(self, kind, children=[]):
        super().__init__()
        self.kind = kind
        self.children = children
        # print(self)

    def __repr__(self):
        return f"<{self.__class__.__name__} {self.kind} {self.children}>"

    def toRpy(self, sublabel):
        return textwrap.indent(f"UNHANDLED TAG {self}", "# ")

class EventUnhandled(Event):
    @classmethod
    def fromTag(cls, xml):
        print("unhandled tag", xml.name)
        return cls(
            kind=xml.name
        )

    def toRpy(self, sublabel):
        return f"# UNDEFINED TAG {self}"


class EventVardefine(Event):
    def __init__(self, kind, store, varname, value):
        self.store = store
        self.varname = varname
        self.value = value
        super().__init__(kind)

    @classmethod
    def fromTag(cls, xml):
        value = xml['value']
        if value == "true":
            value = True
        if value == "false":
            value = False
        return cls(
            kind=xml.name, 
            store=xml['storeName'],
            varname=xml['varName'],
            value=value,
        )

    def __repr__(self):
        return f"<{self.__class__.__name__} {self.store}.{self.varname} = {self.value}"

    def toRpy(self, sublabel):
        return f'$ {self.store}__{self.varname} = {self.value}'

class EventAudioplay(Event):
    def __init__(self, kind, sound, channel):
        self.sound = sound
        self.channel = channel
        super().__init__(kind)

    @classmethod
    def fromTag(cls, xml, channel):
        return cls(
            kind=xml.name, 
            sound=xml['sound'],
            channel=channel
        )

    def __repr__(self):
        return f"<{self.__class__.__name__} {self.kind} {self.sound=}"

    def toRpy(self, sublabel):
        sound_path = re.sub(r"@a_([a-z]+)_(.*)", "\g<1>/\g<2>.ogg", self.sound)
        return f'play {self.channel} "{sound_path}"'

class EventParallel(Event):
    def __init__(self, kind, name, auto, children):
        self.name = name
        self.auto = auto
        super().__init__(kind, children)

    @classmethod
    def fromTag(cls, xml):
        assert not xml.partneractor
        return cls(
            kind=xml.name, 
            name=xml.get('name', 'undefined'),
            auto=xml.get('auto'),
            children=Events.fromTag(xml.events).children
        )

    def toRpy(self, sublabel):
        new_sublabel = sublabel + "_" + self.name.replace('.', '_')
        body = NodeContainer.toRpy(self, sublabel=new_sublabel)
        if self.name.replace('.', '_') in JumpLabelStore:
            return f"label {new_sublabel}: # (ParallelEvent)\n" + textwrap.indent(body, "    ")
        else:
            return f"# {self.kind} {self.name} {new_sublabel}\n" + body

class EventText(Event):
    def __init__(self, kind, char, text):
        self.char = char.replace("@", "")
        self.text = re.sub(r"\@([^ ]+)", lambda m: TextStore[m.group(1)], text)
        super().__init__(kind)

    @classmethod
    def fromTag(cls, xml):
        return cls(
            kind=xml.name, 
            char=xml.get('char', ""),
            text=xml.get('text', ""),
        )

    def __repr__(self):
        return f"<{self.__class__.__name__} {self.char} {self.text=}"

    def toRpy(self, sublabel):
        if not self.char:
            return "# Blank text event"
        return f'{fixname(self.char)} "{textToRpyInterp(self.text)}"'

class EventActorfade(Event):
    def __init__(self, kind, duration, opacity, target):
        self.duration = duration
        self.opacity = opacity
        self.target = target
        super().__init__(kind)

    @classmethod
    def fromTag(cls, xml):
        return cls(
            kind=xml.name, 
            duration=xml.get('duration', 0.5),
            opacity=xml.get('opacity', xml.get("to")),
            target=xml['target']
        )

    def toRpy(self, sublabel):
        # TODO this is wrong behavior
        try:
            return f"show {ActorPrevStore[self.target]} as {self.target} with Dissolve({self.duration})"
        except:
            return f"# ERROR: Missing previous image for target '{self.target}'"

class EventActorImage(Event):
    def __init__(self, kind, image, target):
        self.image = image
        self.target = target
        super().__init__(kind)

    @classmethod
    def fromTag(cls, xml):
        return cls(
            kind=xml.name, 
            image=xml['image'],
            target=xml['target']
        )

    def toRpy(self, sublabel):
        char = re.sub(r'@i_([a-z]+)_.+', '\g<1>', self.image)
        ActorPrevStore[self.target] = self.image.replace('@', '')
        return f"show {self.image.replace('@', '')} as {self.target}"
        
x = None
class EventActorCreate(Event):
    def __init__(self, kind, image, style, id):
        self.image = image
        self.style = style
        self.id = id
        super().__init__(kind)
        # TODO: this defines something in storage

    @classmethod
    def fromTag(cls, xml):
        global x
        x = xml
        return cls(
            kind=xml.name, 
            id=xml['actorId'],
            image=xml.styles.image.text,
            style=xml.styles
        )

    def toRpy(self, sublabel):
        ActorPrevStore[self.id] = self.image.replace('@', '')

class EventJump(Event):
    def __init__(self, kind, name, scene):
        self.name = name
        self.scene = scene

        self.target = self.scene.replace('@', '').replace('.', '_').replace('/', '_')
        JumpLabelStore.append(self.target)
        super().__init__(kind)

    @classmethod
    def fromTag(cls, xml):
        return cls(
            kind=xml.name, 
            name=xml['name'],
            scene=xml.get("scene") or xml.get("path"),
        )

    def toRpy(self, sublabel):
    # if "/" in target:
        if self.kind == "nhscenechange":
            return f"jump {self.target}  # {self.kind} {self.name}"
        elif self.name == "retreat":
            retreat_target = "_".join(sublabel.split("_")[:-1])
            return f"jump {retreat_target}_{self.target}  # {self.kind} {self.name}"
        else:
            return f"jump {sublabel}_{self.target}  # {self.kind} {self.name}"

class EventMacro(Event):
    def __init__(self, kind, name, children):
        self.name = name
        JumpLabelStore.append(self.name)
        super().__init__(kind, children)

    @classmethod
    def fromTag(cls, xml):
        assert not xml.partneractor
        return cls(
            name=xml['name'],
            kind=xml.name, 
            children=Events.fromTag(xml.events).children
        )

    def toRpy(self, sublabel):
        # todo: argh
        label = f"{sublabel}_{self.name}"
        if self.name in JumpLabelStore:
            return f"label {label}:\n" + textwrap.indent(NodeContainer.toRpy(self, label), "    ")
        else:
            return f"# {self.kind} {self.name} {label}\n" + NodeContainer.toRpy(self, label) 
        # return f"label MACRO{sceneid}_{self.name}: # (Macro) \n" + textwrap.indent(NodeContainer.toRpy(self), "    ")

class EventNamedmacro(Event):
    def __init__(self, name, kind, children, partneractor):
        self.partneractor = partneractor
        self.name = name
        super().__init__(kind)

    @classmethod
    def fromTag(cls, xml):
        return cls(
            name=xml['name'],
            kind=xml.name, 
            children=Events.fromTag(xml.events) if xml.events else None,
            partneractor=xml.partneractor
        )
    def __repr__(self):
        return f"<{self.__class__.__name__} {self.name} {self.kind} {self.partneractor}"
    def toRpy(self, sublabel):
        return f"# UNHANDLED MACRO {self}\n" + textwrap.indent(NodeContainer.toRpy(self, sublabel=sublabel), "    # ")

class EventCompare(Event):
    def __init__(self, name, kind, lvalue, rvalue, children):
        self.lvalue = lvalue 
        self.rvalue = rvalue 
        self.children = children
        self.name = name
        super().__init__(kind)

    @classmethod
    def fromTag(cls, xml):
        return cls(
            name=xml['name'],
            kind=xml.name, 
            lvalue=xml['lvalue'],
            rvalue=xml['rvalue'],
            children = Events.fromTag(xml.events)
        )

    def __repr__(self):
        return f"<{self.__class__.__name__} {self.lvalue} {self.kind} {self.rvalue}\n{self.children}"

class EventTest(Event):
    def __init__(self, name, kind, expr, children):
        self.expr = expr
        self.name = name
        super().__init__(kind, children)

    @classmethod
    def fromTag(cls, xml):
        return cls(
            name=xml['name'],
            kind=xml.name, 
            expr=xml['value'],
            children=Events.fromTag(xml.events).children
        )

    def __repr__(self):
        return f"<{self.__class__.__name__} {self.kind} {self.expr}\n{self.children}"

    def toRpy(self, sublabel):
        test = {
            "iffalse": "not ",
            "iftrue": ""
        }[self.kind]
        expr = textToRpyInterp(self.expr).replace("[", "").replace("]", "")
        # TODO: Temporary "pass"
        return f"if {test}{expr}:\n" + textwrap.indent(NodeContainer.toRpy(self, sublabel=sublabel) + "\npass", "    ")