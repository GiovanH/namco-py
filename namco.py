import re
import textwrap
import collections
import nc_hardcoded
from bs4 import NavigableString
from pprint import pprint
from types import GeneratorType

pathsep = "_"
sceneid = ""


# TODO maybe add a finalizing opacity statement after ATLs to 
# workaround the half-faded bug

SHOW_UNHANDLED_ATTRS = True

TextStore = nc_hardcoded.TextStore.copy()
ActorPrevStore = collections.defaultdict(lambda: None)
JumpLabelStore = []
unhandled_attrs = collections.defaultdict(set)
ActorIsFlipped = collections.defaultdict(lambda: 1.0)
last_image_for_tag = {}
AllStores = set()
DefaultVars = []
cps_mult = 1.0
last_say_what = None

def init():
    global ActorIsFlipped
    global AllStores
    global JumpLabelStore
    global ActorPrevStore
    global TextStore
    global last_image_for_tag
    global unhandled_attrs
    global DefaultVars
    global cps_mult
    global last_say_what

    TextStore = nc_hardcoded.TextStore.copy()
    ActorPrevStore = collections.defaultdict(lambda: None)
    JumpLabelStore = []
    unhandled_attrs = collections.defaultdict(set)
    ActorIsFlipped = collections.defaultdict(lambda: 1.0)
    last_image_for_tag = {}
    AllStores = set()
    DefaultVars = []
    cps_mult = 1.0
    last_say_what = None

def textToRpyInterp(text):
    text = re.sub(r"([\\\"])", r"\\\g<1>", text)
    text = re.sub(r"\${(.+?):(.+?)}", lambda m: f"[{getStoreVarName(m.group(1), m.group(2))}]", text)
    return text

def fixname(char):
    return char.replace("@", "")

def toPyValue(value):
    if value == "false":
        return False
    elif value == "true":
        return True
    else:
        try:
            return int(value)
        except:
            return value

def getStoreVarName(storeName, varName):
    AllStores.add(storeName)
    if storeName == "game":
        # DefaultVars.append(("persistent", varName, None))
        return f"persistent.{varName}"
    return f"{storeName}_{varName}"

def findNode(nodes, **kwargs):
    for n in nodes:
        if all(n.attrs[k] == v for k, v in kwargs.items()):
            return n
    return None

def findNodes(nodes, **kwargs):
    for n in nodes:
        if all(n.attrs[k] == v for k, v in kwargs.items()):
            yield n

def p2f(x):
    return float(x.strip('%')) / 100

def getPrevLevel(node):
    named_parent = None
    while not named_parent or not named_parent.label:
        named_parent = (named_parent.parent if named_parent else node.parent)
    return node.parent.getLabel().replace(pathsep + named_parent.name, "")

def slugify(string):
    assert "/" not in string, string
    return string.replace("@", "").replace(".", "p")

def jsExprToPy(value):
    value2 = textToRpyInterp(value)
    value2 = re.sub(r"^\[(.+)\]$", r"\g<1>", value2)
    value2 = re.sub(r"(st_[^.]+)\.([A-Za-z0-9_]+)", r"\g<1>['\g<2>']", value2)
    assert "$" not in value2, (value, value2)
    # assert "." not in value2, (value, value2)
    return value2

def transformScaleX(factor, actor):
    fl = float(factor)
    ActorIsFlipped[actor] = fl

    return f"xzoom {fl} "


def allChildrenR(node):
    for c in node.children:
        yield c
        yield from allChildrenR(c)


transformation = {
    "opacity": lambda a, i: f"alpha {round(float(a), 2)}",
    "delay": lambda a, i: f"pause {round(float(a), 2)} ",
    "x": lambda a, i: f"xpos {round(0.5 + p2f(a), 2)} ",
    "y": lambda a, i: f"ypos {round(0.5 + p2f(a), 2)} ",
    "scaleX": transformScaleX,
    "scaleY": lambda a, i: f"yzoom {float(a)} ",
}

def resolveAtl(atl):
    actor_id = atl['actor_id']
    atl_statements = atl.get('lines', [])
    duration = atl.get('duration', 0)

    if not last_image_for_tag.get(actor_id):
        atl['create'] = True

    if atl.get("image"):
        target = slugify(atl.get("image"))
        last_image_for_tag[actor_id] = target
    else:
        target = last_image_for_tag[actor_id]

    statement = f"show {target}"
    statement += f" as {actor_id}"

    if atl.get("zorder"):
        statement += f" zorder {atl['zorder']}"
    if atl.get("create"):
        if atl_statements:
            atl_statements.insert(0, "default")
        else:
            statement += f" at default"

    if atl_statements:
        if not all(a.startswith("#") for a in atl_statements):
            statement += ":\n" 
        statement += textwrap.indent("\n".join(atl_statements), "    ")

    if atl.get("with"):
        statement += "\nwith " + atl.get("with")

    # if duration > 0:
    #     statement += f"\n# $ renpy.pause({duration})"

    return statement

def toRpyInterp(interpolation):
    return {
        "linear": "linear",
        "ease": "ease",
        "ease-out": "easeout",
        "ease-in": "easein",
        "ease-in-out": "ease_expo"
    }[interpolation]


def showActorWithAtl(node, fields):
    interpolation = toRpyInterp(node.attrs.get("ease", "linear"))  # ease-out
    duration = node.attrs.pop("duration", 0.5)

    atl_statements = ["# ShowWithAtl"]
    pause = 0

    delay = node.attrs.pop("delay", 0)

    target = node.attrs.pop('target')

    if delay:
        atl_statements.append(f"pause {float(delay)} ")
        pause += float(delay)

    for style, value in list(node.attrs.items()):
        if style in fields:
            statement = f"{interpolation} {duration} " if duration and float(duration) > 0 else ""
            statement += transformation[style](value, target)
            atl_statements.append(statement)
            pause += float(duration)
            node.attrs.pop(style)

    return {
        "actor_id": target,
        "lines": atl_statements,
        "duration": pause,
        "create": False
    }


# Abstract tree handlers

class Node():
    def __init__(self, tag_name=None, attrs={}, children=[], text=""):
        super().__init__()
        self.__dict__.update(attrs)  # helper
        self.attrs = self.__dict__

        self.label = None
        self.parent = None
        if tag_name is None:
            tag_name = self.__class__.__name__
        self.kind = tag_name
        self.attrs = attrs
        self.children = children
        self.text = text

        self.attrs_copy = self.attrs.copy()
        self.attrs['kind'] = tag_name
        self.pausetime = 0

    def preprocess(self):
        self.process()
        for child in self.children:
            try:
                child.parent = self
            except TypeError:
                print(child)
                raise
            child.preprocess()

    def process(self):
        pass

    @classmethod
    def fromTag(cls, tag, parent=None):
        node_cls = NODE_TYPES.get(tag.name, cls)
        children = []
        text = ""
        for child in tag.contents:
            if isinstance(child, NavigableString):
                text += str(child).strip()
            elif child.name in PROPERTY_NODES:
                assert child.name not in tag.attrs, (child, tag)
                assert not child.attrs
                tag.attrs[child.name] = child.text
            else:
                children.append(Node.fromTag(child))
        return node_cls(tag.name, tag.attrs, children, text)

    def __repr__(self, short=True):
        selfr = f"<{self.__class__.__name__} {self.attrs_copy} {self.kind} '{self.text}'>"
        if self.children and not short:
            childrenstr = "\n".join(str(c) for c in self.children)
            return f"{selfr}\n  {textwrap.indent(childrenstr, '    ')}\n>"
        else:
            return selfr

    def __str__(self):
        return self.__repr__(short=False)

    def toRpy(self):
        print(self.__class__.__name__, "Unhandled")
        return textwrap.indent(f"UNHANDLED TAG {self}", "# ")
        # body = NodeContainer.toRpy(self, sublabel=new_sublabel)
        # return f"label {new_sublabel}:\n" + textwrap.indent(body, "    ")
        
    def getLabel(self):
        if self.label:
            return self.label
        if self.parent:
            return self.parent.getLabel()
        else: 
            raise ValueError(self, "Can't get label, no parent")
    

class NoScript(Node):
    def toRpy(self):
        return f"# Pass ({self.kind})"

class NodeContainer(Node):
    def toRpy(self, prefix=""):
        if not self.label:
            return NodeBody.toRpy(self)
        return f"{textwrap.indent(repr(self), '# ')}\nlabel {self.label}:\n" + textwrap.indent(NodeBody.toRpy(self, prefix=prefix), "    ")

class Macro():
    def process(self):
        if "name" in self.attrs:
            self.label = self.attrs.pop("name")


class Annotation(Node):
    def toRpy(self):
        return textwrap.indent(self.text, '# ')

class RawRpy(Node):
    def toRpy(self):
        return self.text

class NodeBody(Node):
    def toRpy(self, prefix=""):
        lines = []
        if prefix:
            lines.append(prefix)
        lines.append(textwrap.indent(repr(self), '# '))
        
        # Flatten macros

        #TODO when is this ever needed?
        # i = 0
        # while i < len(self.children):
        #     if isinstance(self.children[i], Events):
        #         new_children = [
        #             *self.children[:i],
        #             Annotation(tag_name="Splice", text=repr(self.children[i])),
        #             *self.children[i].children,
        #             *self.children[i + 1:]
        #         ]
        #         print("Splice")
        #         print(str(self))
        #         print(new_children)
        #         self.children = new_children
        #     i += 1

        i = 0

        while i < len(self.children):
            atl_groups = collections.defaultdict(list)
            while i < len(self.children) and isinstance(self.children[i], ATLSource):
                atl = self.children[i].getAtl()
                if isinstance(atl, GeneratorType):
                    for a in atl:
                        atl_groups[a['actor_id']].append(a)
                else:
                    assert atl, self.children[i]
                    atl_groups[atl['actor_id']].append(atl)
                i += 1

            for actor_id, atls in atl_groups.items():
                atl_buffer = {}
                for atl in atls:
                    if atl_buffer:
                        assert atl_buffer['actor_id'] == atl['actor_id']
                        atl_buffer['lines'] += atl.get('lines', [])
                        atl_buffer['duration'] += atl.get('duration', 0)

                        if atl.get("image"):
                            if atl_buffer.get("image"):
                                lines.append(resolveAtl(atl_buffer))
                                lines.append(f"$ renpy.pause({atl_buffer['duration']}) # Image change")
                                last_say_what = None
                                atl_buffer = atl
                                atl_buffer['lines'] = atl.get('lines', [])
                                atl_buffer['duration'] = atl.get('duration', 0)

                            target = slugify(atl.get("image"))
                            last_image_for_tag[actor_id] = target
                            atl_buffer['image'] = target
                    else:
                        atl_buffer = atl
                        atl_buffer['lines'] = atl.get('lines', [])
                        atl_buffer['duration'] = atl.get('duration', 0)
                # print(atl_buffer)
                lines.append(resolveAtl(atl_buffer))

            while i < len(self.children) and not isinstance(self.children[i], ATLSource):
                # print(self.children[i])
                lines.append(self.children[i].toRpy())
                i += 1

        for child in self.children:
            for attr in child.attrs:
                if attr in ['kind']:
                    continue
                unhandled_attrs[child.kind].add(attr)

        return "\n".join(lines)
        
class ATLSource(Node):
    def getAtl(self):
        raise NotImplementedError

    def toRpy(self):
        return resolveAtl(self.getAtl())

# Actual stuff

class Scene(NodeContainer, Node):
    def __init__(self, *args, **kwargs):
        init()
        super().__init__(*args, **kwargs)
        self.preprocess()
        print("Scene", self.name, "processed!")

    def process(self):
        self.label = slugify(self.attrs.pop("id"))
        self.name = self.label
        global sceneid
        sceneid = self.label

    def makeExtraLines(self):
        extra_lines = []
        # extra_lines.append("init -1 python:\n    from types import SimpleNamespace\n")
        for store_name in AllStores:
            # extra_lines .append(f"define {store_name} =" + " renpy.python.StoreModule({})\n")
            # extra_lines.append(f"define st_{store_name} = " + "{}")
            pass
        for (store_name, var_name, value) in DefaultVars:
            extra_lines.append(f"define {getStoreVarName(store_name, var_name)} = {value}")

        extra_lines.append("")
        return extra_lines

    def toRpy(self):
        extra_lines = self.makeExtraLines()
        prefix = "\n".join([
            "scene i_sw_black with dissolve",
            "stop music fadeout 1.0",
            f"$ slot_day_name = \"{self.label}\"",
            "$ renpy.pause(1) # buffer"  # fake loading
        ])
        ret = "\n".join(extra_lines) + NodeContainer.toRpy(self, prefix=prefix)
        if unhandled_attrs and SHOW_UNHANDLED_ATTRS:
            print("Unhandled attributes:")
            pprint(unhandled_attrs)
        return ret
        
class Assets(NoScript, Node):
    pass  # Assets are handled when parsed

class TimedPause(Node):
    def toRpy(self):
        duration = self.attrs.pop('duration')
        if float(duration) > 0:
            return f"$ renpy.pause({duration}) # TimedPause"
        return ""

class Events(NodeBody, Node):
    def process(self):
        self.kind = "events"
        self.attrs['kind'] = self.kind
        # assert self.attrs.get("kind", "events") == "events"

    def block(self, should_block):

        # self.attrs['should_block'] = should_block

        # Technically this is incorrect
        # What we need is the total ATL time, 
        # but we can't sum them together because ATL events from
        # different characters run in parallel.
        pausetime = max(c.pausetime for c in self.children)

        # If we have a textevent, move it to the end of the list.
        if any(isinstance(c, TextEvent) for c in self.children):
            # if len(self.children) == 1:
            #     return
            i = 0
            TextEvents = []
            while i < len(self.children):
                if isinstance(self.children[i], TextEvent):
                    self.children[i].block = False
                    TextEvents.append(self.children.pop(i))
                else:
                    i += 1
            self.children += TextEvents
            if should_block:
                assert isinstance(self.children[-1], TextEvent)
                self.children[-1].block = "Last"
                self.children[-1].delay += pausetime
            return
        else:
            # TODO: Pause for duration of inner animation.
            # Extend w=x for better visuals?
            if should_block:
                # assert pausetime != 0, str(self)
                self.children.append(
                    TimedPause("TimedPause", attrs={
                        "duration": pausetime
                    })
                )


class ActorEvent(ATLSource, Node):
    def process(self):
        self.actor_id = self.attrs.pop('target')  # albatros

        self.styles = list(findNodes(self.children, kind="styles"))
        self.transitions = list(findNodes(self.children, kind="transitions"))
        self.interpolation = toRpyInterp(self.attrs.pop("ease", "linear"))  # ease-out

        self.atl = self._getAtl()

    def getAtl(self, source="ActorEvent"):
        self.atl['lines'] = [f"# {source}"] + self.atl.get("lines", [])
        return self.atl

    def _getAtl(self, source="ActorEvent"):
        transitiondur = self.attrs.pop("duration", 0)
        delay = self.attrs.pop("delay", 0)

        atl_statements = []
        for style in self.styles:
            
            for pre_style, value in style.attrs.items():
                if pre_style in ['image', 'depth', 'kind', 'id']:
                    continue
                atl_statements.append(transformation[pre_style](value, self.actor_id))

            for t in self.transitions:
                for prop, value in t.attrs.items():
                    if prop in ['kind']:
                        continue
                    statement = f"pause {delay}\n" if delay else ""
                    self.pausetime += float(delay)

                    statement += f"{self.interpolation} {transitiondur} " if transitiondur else ""
                    self.pausetime += float(transitiondur)
                    
                    statement += transformation[prop](value, self.actor_id)
                    atl_statements.append(statement)

            return {
                "actor_id": style.attrs.pop("id", self.actor_id),
                "image": style.attrs.pop('image', None),
                "zorder": style.attrs.pop("depth", None),
                "duration": self.pausetime,
                "lines": atl_statements,
                "create": False
            }

        # Transition only

        atl_statements = ["# ActorEvent (Transition only)"]
        for t in self.transitions:
            statement = f"pause {delay}\n" if delay else ""
            self.pausetime += float(delay)
            statement += f"{self.interpolation} {transitiondur} " if transitiondur else ""
            self.pausetime += float(transitiondur)
            for prop, value in t.attrs.items():
                if prop in ['kind']:
                    continue
                statement += transformation[prop](value, self.actor_id)
            atl_statements.append(statement)

            return {
                "actor_id": t.attrs.pop("id", self.actor_id),
                "zorder": t.attrs.pop("depth", None),
                "delay": delay,
                "lines": atl_statements,
                "duration": self.pausetime,
                "create": False
            }

        # Animation Only

        atl_statements = ["# ActorEvent (Animation only)"]
        atl = {
            "actor_id": self.actor_id,
            "duration": self.attrs.get("duration"),
            "create": False
        }
        
        self.pausetime = self.attrs.pop("duration", 0)
        animation = self.attrs.pop("animation", None)
        if animation:
            atl['with'] = animation
        return atl

class ActorCreate(ATLSource, Node):
    # or "DOMImageCreate"
    # can contain <transition>s and <style>s
    def process(self):
        self.actor_id = self.attrs.pop('actorId')  # albatros
        self.actor_type = self.attrs.pop('actorType')  # character

        self.styles = list(findNodes(self.children, kind="styles")) 
        self.transitions = list(findNodes(self.children, kind="transitions")) or [Transitions("Transitions")]

        # self.transitions[0].attrs['duration'] = self.attrs.pop("duration", 0)
        self.name = self.attrs.get("name", None)  # _1
        self.allow_interrupt = self.attrs.get("allowInterrupt", True)  # bool
        self.auto = self.attrs.get("auto", False)  # bool
        self.interpolation = toRpyInterp(self.attrs.get("ease", "linear"))  # ease-out

        self.atl = ActorEvent._getAtl(self, source="ActorCreate")
        self.atl['create'] = True

    def getAtl(self):
        return self.atl

class ActorCrossfade(ATLSource, Node):
    def getAtl(self):

        fadedur = self.attrs.pop("duration")
        target = self.attrs.pop("target")
        image = slugify(self.attrs.pop("image"))

        return {
            "actor_id": target,
            "image": image,
            "with": f"Dissolve({fadedur})",
            "source": "ActorCrossfade"
        }


class ActorDepth(ATLSource, Node):
    def getAtl(self):
        target = self.attrs.pop("target")
        depth = self.attrs.pop("depth")
        return {
            "actor_id": target,
            "zorder": depth,
            "lines": []
        }

class ActorDestroy(Node):
    def toRpy(self):
        target = self.attrs.pop('target')
        # target#= last_image_for_tag[self.attrs.pop('target')]
        return f"hide {target}"


class ActorFade(ATLSource, Node):
    def process(self):
        self.atl = showActorWithAtl(self, ['opacity'])
        self.pausetime += self.atl['duration']

    def getAtl(self):
        return self.atl

class ActorFlip(ATLSource, Node):
    def process(self):
        self.actor = self.attrs.pop('target')

        self.interp = toRpyInterp(self.attrs.pop('ease', 'linear'))
        self.duration = self.attrs.pop('duration', 0)
        self.delay = self.attrs.pop('delay', 0)

        self.pausetime = float(self.delay)

    def getAtl(self):
        prev = ActorIsFlipped[self.actor]
        xzoom = prev * -1

        lines = []

        if self.delay:
            lines.append(f"pause {self.delay}")

        statement = f"{self.interp} {self.duration} " if self.duration else ""
        statement += transformScaleX(xzoom, self.actor)

        lines.append(statement)

        return {
            "actor_id": self.actor,
            "lines": lines,
            "duration": self.pausetime,
        }

class ActorImage(ATLSource, Node):
    # or "ImageShortcut"
    # I THINK this means 
    # Set actor <actor>'s image to <image>
    def process(self):
        self.image = slugify(self.attrs.pop('image'))
        self.actor = self.attrs.pop('target')

        self.name = self.attrs.get('name', None)
        self.auto = toPyValue(self.attrs.get('auto', False))
        self.delay = float(self.attrs.pop('delay', 0))
        # TODO delay not implemented

        self.pausetime += float(self.delay)

    def getAtl(self):
        return {
            "actor_id": self.actor,
            "image": self.image,
            "delay": self.delay,
            "source": "ActorImage"
        }

class ActorMove(ATLSource, Node):
    def process(self):
        self.atl = showActorWithAtl(self, ['x', 'y'])
        self.pausetime += self.atl['duration']
        
    def getAtl(self):
        return self.atl

class ActorReset(NoScript, Node):
    pass

class ActorScale(ATLSource, Node):
    def process(self):
        if 'x' in self.attrs:
            self.attrs['scaleX'] = self.attrs.pop('x')
        if 'y' in self.attrs:
            self.attrs['scaleY'] = self.attrs.pop('y')

        self.atl = showActorWithAtl(self, ['scaleX', 'scaleY'])
        self.pausetime += self.atl['duration']
        
    def getAtl(self):
        return self.atl


class ActorTransform(Node):
    def process(self):
        self.atl = showActorWithAtl(self, ['scaleX', 'scaleY', 'x', 'y'])
        self.pausetime += self.atl['duration']
        
    def getAtl(self):
        return self.atl

AudioLayer = {}

class AudioCreate(Node):
    def process(self):
        self.layer = self.attrs.pop('layer')
        self.loop = toPyValue(self.attrs.pop('loop'))
        # self.play = toPyValue(self.attrs.pop('play'))
        self.path = toPyValue(self.attrs.pop('sound'))
        self.delay = toPyValue(self.attrs.pop('delay', None))

        if self.layer == "bgm":
            self.layer = "music"
        elif self.layer == "sfx":
            self.layer = "sound"
        else:
            raise ValueError(self.layer)

        AudioLayer[self.attrs.pop('audioId')] = self.layer

        # TODO: Unused attrs play, volume, allowInterrupt

    def toRpy(self):
        real_path = re.sub(r"@a_([a-z]+)_(.*)", r"\g<1>/\g<2>.ogg", self.path)

        if real_path == "bgm/credits.ogg":
            return "# Credits music -- NOT PLAYING (in screen)"

        if self.delay:
            return f'play {self.layer} ["<silence {self.delay}>", "{real_path}"] {"loop" if self.loop else "noloop"}'
        else:
            return f'play {self.layer} "{real_path}" {"loop" if self.loop else "noloop"}'

class AudioDestroy(Node):
    def toRpy(self):
        return f"stop {AudioLayer[self.attrs.pop('target')]}"

class AudioEvent(Node):
    def process(self):
        self.layer = self.attrs.pop('target')
        if self.layer == "bgm":
            self.layer = "music"
        elif self.layer == "sfx":
            self.layer = "sound"
        elif self.layer == "river":
            self.layer = "sound"
        else:
            raise ValueError(self.layer)

    def toRpy(self):
        volume = float(self.attrs.pop("volume"))
        fadeduration = float(self.attrs.pop("fadeDuration", 0))
        if volume == 0:
            return f"stop {self.layer} fadeout {fadeduration}"
        return f"$ AudioEvent('{self.layer}', {volume}, {fadeduration})"

class AudioOneShot(Node):   
    def process(self):
        self.sound = self.attrs.pop('sound')
        self.delay = self.attrs.get('delay', 0)
        self.channel = "sound"

    def toRpy(self):
        sound_path = re.sub(r"@a_([a-z]+)_(.*)", r"\g<1>/\g<2>.ogg", self.sound)
        if self.delay:
            return f'play {self.channel} ["<silence {self.delay}>", "{sound_path}"]'
        else:
            return f'play {self.channel} "{sound_path}"'


class NormalEndMacro(NodeBody, Node):
    def process(self):
        g = self.attrs.pop("partnerActor")
        t = partnerImage = self.attrs.pop("partnerImage")

        o = cousinX = self.attrs.pop("cousinX", "-15%")
        p = partnerX = self.attrs.pop("partnerX", "-35%")
        u = runCredits= self.attrs.pop("runCredits", False)

        c = curtainActor = "curtain"
        d = cousinActor = "cousin"
        h = pacmanActor = "pacman"
        digdugActor = "digdug"
        i = firstLine = "@t_com00.00"
        n = secondLine = "@t_com01.00"
        q = curtainFadeOutTime = .5
        r = curtainFadeInTime = .5
        s = cousinImage = "@i_cousin_energetic_grin"
        m = "@a_bgm_credits"

        self.children = [
            ParallelEvent("ParallelEvent", attrs={"auto": True}, children=[
                Events("events", children=[
                    ActorEvent("ActorEvent", attrs={
                        "target": d
                    }, children=[
                        Styles("styles", attrs={
                            "x": o,
                            "image": s,
                            "depth": 3
                        })
                    ]),
                    ActorEvent("ActorEvent", attrs={
                        "target": g
                    }, children=[
                        Styles("styles", attrs={
                            "x": p,
                            "image": t,
                            "depth": 2
                        })
                    ]),
                    ActorEvent("ActorEvent", attrs={
                        "target": h
                    }, children=[
                        Styles("styles", attrs={
                            "x": "30%",
                            "opacity": 1,
                            "depth": 2
                        })
                    ]),
                    TextEvent(attrs={
                        "char": "@t_ch_pacman",
                        "text": i
                    })
                ])
            ]),
            ActorEvent("ActorEvent", attrs={
                "target": c,
                "duration": q
            }, children=[
                Transitions(attrs={
                    "opacity": 0
                })
            ]),
            TextEvent(attrs={
                "char": "@t_ch_cousin",
                "text": n
            }),

            ActorEvent("ActorEvent", attrs={
                "target": c,
                "duration": r,
                "auto": False
            }, children=[
                Transitions(attrs={
                    "opacity": 1
                })
            ]),
            TextEvent(attrs={
                "char": "",
                "text": "",
                "auto": False
            })
        ]

        if u:
            self.children.append(AudioEvent(attrs={
                "target": "bgm",
                "volume": 1,
                "sound": m,
                "auto": True,
                "loop": False,
                "play": True
            }))
            self.children.append(CreditsEvent())


class BadEndMacro(Node):
    def process(self):
        self.expr = jsExprToPy(self.attrs.pop('varName'))

    def toRpy(self):
        lines = [
            f"if {self.expr} <= 1:",
            f"    call BadEndMacro"

        ]
        return "\n".join(lines)

class BattleMacro(NodeBody, Node):
    def process(self):

        partnerActor = self.attrs.pop('partnerActor', None)

        m = "thunderclap"

        whiteSwatchActor = "white_swatch"  # i
        robotArmyActor = "robotarmy"  # p
        curtainActor = "curtain"  # q
        cousinActor = "cousin"  # r
        bgActor = "bg"  # s
        whiteHoldTime = 2  # t
        whiteFadeOutTime = 2  # u
        whiteFadeOutTime = 2  # v
        bgZoomTime = .75  # w
        bgZoomEase = "ease-out"  # x
        robotArmyStartingX = "0%"  # y
        robotArmyDstX = "-40%"  # z
        robotArmyHoldTime = .75  # A
        robotArmyMoveTime = 1  # B
        bgmFadeTime = "bgm"  # C

        def n(a, b):
            return ParallelEvent("ParallelEvent", attrs={"auto": True}, children=[
                Events("events", children=[
                    ActorEvent("ActorEvent", attrs={
                        "target": a,
                        "duration": 0.4,
                        "animation": "flash"
                    }),
                    ActorEvent("ActorEvent", attrs={
                        "target": b,
                        "duration": 0.75,
                        "animation": "flash"
                    }, children=[
                        Transitions("transitions", attrs={"opacity": 1.0})
                    ])
                ])
            ])

        def o(a, b):
            return ActorEvent("ActorEvent", attrs={
                "ease": "ease",
                "duration": 1.0,
                "target": a,
            }, children=[
                Transitions("transitions", attrs={"x": b})
            ])

        D = [
            RawRpy(text="window hide None"),
            ParallelEvent(
                attrs={"auto": True},
                children=[
                    Events(children=[
                        ActorEvent(attrs={
                            "target": bgActor,
                        }, children=[
                            Styles("styles", attrs={
                                "x": "0%",
                                "y": "15%",
                                "scaleX": "2",
                                "scaleY": "2"
                            })
                        ]),
                        ActorEvent("ActorEvent", attrs={
                            "target": robotArmyActor,
                        }, children=[
                            Styles("styles", attrs={"x": robotArmyStartingX})
                        ])
                    ])
                ]
            ),
            ParallelEvent(
                "ParallelEvent", 
                attrs={"delay": 0.5, "auto": True},
                children=[
                    Events("events", children=[
                        AudioCreate("AudioCreate", attrs={
                            "audioId": m,
                            "sound": "@a_sfx_thunderclap",
                            "layer": "sfx",
                            "loop": False,
                            "play": True
                        }),
                        ActorEvent("ActorEvent", attrs={
                            "target": whiteSwatchActor,
                            "duration": 0.4,
                            "animation": "flash"
                        }),
                        ParallelEvent(
                            "ParallelEvent", 
                            attrs={"delay": 0.5},
                            children=[Events("events", children=[
                                ActorEvent("ActorEvent", attrs={
                                    "target": whiteSwatchActor,
                                    "duration": 0.4,
                                    "animation": "flash"
                                })
                            ])]
                        )
                    ])
                ]
            ),
            ParallelEvent(
                "ParallelEvent", 
                attrs={"delay": whiteFadeOutTime, "auto": True},
                children=[
                    Events("events", children=[
                        ActorEvent("ActorEvent", attrs={
                            "target": bgActor,
                            "duration": bgZoomTime,
                            "ease": bgZoomEase,
                        }, children=[
                            Transitions("transitions", attrs={
                                "x": "0%",
                                "y": "0%",
                                "scaleX": "1",
                                "scaleY": "1"
                            })
                        ])
                    ])
                ]
            ),
            ActorEvent("ActorEvent", attrs={
                "target": robotArmyActor,
                "duration": 0.75,
            }, children=[
                Transitions("transitions", attrs={"opacity": 1})
            ]),
            TimedPause(attrs={"duration": 0.75}),
            ParallelEvent(
                "ParallelEvent", 
                attrs={"delay": robotArmyHoldTime, "auto": True},
                children=[
                    Events("events", children=[
                        ActorEvent("ActorEvent", attrs={
                            "target": robotArmyActor,
                            "duration": robotArmyMoveTime,
                        }, children=[
                            Transitions("transitions", attrs={"x": robotArmyDstX})
                        ])
                    ])
                ]
            )
        ]

        E = [
            o(robotArmyActor, "-20%"),
            o(cousinActor, "27.5%")
        ]

        if partnerActor:
            D.append(n(whiteSwatchActor, partnerActor))
            E.append(o(partnerActor, "20%"))

        D.append(n(whiteSwatchActor, cousinActor))

        D.append(
            ParallelEvent("ParallelEvent", children=[
                Events("events", children=E)
            ])
        )

        # Fade to white
        # Fade to black
        # Inner stuff (setup)
        
        # HACK: Wrap in parallelevent to force it to block
        D.append(
            ParallelEvent("ParallelEvent", children=[Events(children=[
                ActorEvent("ActorEvent", attrs={
                    "target": whiteSwatchActor,
                    "duration": 0.5,
                }, children=[
                    Transitions("transitions", attrs={"opacity": 1})
                ])
            ])])
        )

        # This pushes "hide robotarmy" and such. ???
        if self.children:
            D.append(Annotation(text="= Battlemacro contents"))
            D.append(
                ParallelEvent("ParallelEvent", children=[
                    Events("events", children=self.children)
                ])
            )
            D.append(Annotation(text="- end battlemacro contents"))

        D.append(ParallelEvent(
            "ParallelEvent", 
            attrs={"delay": whiteHoldTime},
            children=[
                Events("events", children=[
                    AudioDestroy("AudioDestroy", attrs={
                        "target": m,
                        "duration": robotArmyMoveTime,
                    }),
                    TextEvent("TextEvent", attrs={
                        "char": "",
                        "text": "",
                    }),
                    ActorEvent("ActorEvent", attrs={
                        "target": curtainActor
                    }, children=[
                        Styles("styles", attrs={"opacity": 1})
                    ]),
                    ActorEvent("ActorEvent", attrs={
                        "target": whiteSwatchActor,
                        "duration": whiteFadeOutTime
                    }, children=[
                        Transitions("transitions", attrs={"opacity": 0})
                    ]),
                    AudioEvent("AudioEvent", attrs={
                        "target": bgmFadeTime,
                        "volume": 0,
                        "fadeDuration": whiteFadeOutTime,
                    })
                ])
            ]
        ))
        D.append(Annotation(text="End battlemacro"))

        self.children = D



class BranchMacro(Node):
    def process(self):
        comparison = textToRpyInterp(self.attrs.pop('comparison'))
        comparison = re.sub(r"\[(.+?)\]", fr"\g<1>", comparison)
        comparison = comparison.replace("!", "not ")
        comparison = comparison.replace(" && ", " and ")
        comparison = comparison.replace(" || ", " or ")
        self.comparison = comparison
        self.jumplabel = sceneid + pathsep + slugify(self.attrs.pop('path').replace("/", pathsep))

    def toRpy(self):
        return textwrap.indent(f"{self}", "# ") + f"\nif {self.comparison}:\n    jump {self.jumplabel}"


class ConsoleEvent(Node):
    def toRpy(self):
        value = self.attrs.pop("value")
        return f'$ print("{value}")'

class CreditsEvent(Node):
    def toRpy(self):
        return "call CreditsEvent"

class ExplorationMacro(NodeContainer, Node):
    def process(self):
        self.label = self.attrs.pop('name')
        self.pass_text = self.attrs.pop('passText')
        self.lockout = toPyValue(self.attrs.pop('lockout'))
        self.store_name = self.attrs.get("storeName", "scene")
        self.var_name = "explore" + self.attrs.pop('sceneName')

    def toRpy(self):
        lines = [f'$ {sceneid}_has_picked_any = False if not "{sceneid}_has_picked_any" in store.__dict__ else {sceneid}_has_picked_any', "window hide", 'menu (screen="ChoiceExploration"):']
        for name, id in nc_hardcoded.char_name_to_id.items():
            target = sceneid + pathsep + id
            lines.append(f'    "{name}":')
            lines.append(f'        $ {sceneid}_has_picked_any = True')
            lines.append(f'        window show')
            lines.append(f'        jump {target}')

        target = sceneid + pathsep + "cousin"
        any = f"{sceneid}_has_picked_any"
        try:
            lines.append(f'    "{TextStore[self.pass_text]}" if {any}:')
        except KeyError:  # i have no idea
            lines.append(f'    "{TextStore["@" + self.pass_text]}" if {any}:')
        lines.append(f'        window show')
        lines.append(f'        jump {target}')
        return "\n".join(lines)

class FadeEvent(ATLSource, Node):
    def process(self):
        actor_id = self.attrs.pop('target')
        target_opacity = float(self.attrs.pop('to'))

        atl_statement = []
        if 'duration' in self.attrs:
            duration = float(self.attrs.pop('duration'))
            if duration > 0:
                atl_statement.append(f"linear {float(duration)}")
                self.pausetime += duration
        atl_statement.append(f"alpha {target_opacity}")

        self.atl = {
            "actor_id": actor_id,
            "lines": ["# FadeEvent", " ".join(atl_statement)]
        }

    def getAtl(self):
        return self.atl

class GameOver(Node):
    def toRpy(self):
        return "return"

class HardSwap(Node):
    def process(self):
        self.last = self.attrs.pop("lastActor")
        self.next = self.attrs.pop("nextActor")

        self.fadedur = self.attrs.pop("fadeDuration", 0.335)

        # TODO: Probably a kind of between-actor fade?
        # see s_taira3
        # this is a macro actually

class IfExpr(NodeContainer, Node):
    def toRpy(self):
        return f"if {self.expr}:\n" + textwrap.indent(NodeContainer.toRpy(self), "    ")

class IfEqual(IfExpr, Node):
    def process(self):
        lvalue = jsExprToPy(self.attrs.pop('lvalue'))
        rvalue = jsExprToPy(self.attrs.pop('rvalue'))
        self.expr = f"{lvalue} == {rvalue}"
        self.label = self.getLabel() + pathsep + self.attrs.pop('name')

class IfFalse(IfExpr, Node):
    def process(self):
        value = jsExprToPy(self.attrs.pop('value'))
        self.expr = f"not {value}"
        self.label = self.getLabel() + pathsep + self.attrs.pop('name')

class IfGTE(IfExpr, Node):
    def process(self):
        lvalue = jsExprToPy(self.attrs.pop('lvalue'))
        rvalue = jsExprToPy(self.attrs.pop('rvalue'))
        self.expr = f"{lvalue} >= {rvalue}"
        self.label = self.getLabel() + pathsep + self.attrs.pop('name')

class IfLTE(IfExpr, Node):
    def process(self):
        lvalue = jsExprToPy(self.attrs.pop('lvalue'))
        rvalue = jsExprToPy(self.attrs.pop('rvalue'))
        self.expr = f"{lvalue} <= {rvalue}"
        self.label = self.getLabel() + pathsep + self.attrs.pop('name')

class IfTrue(IfExpr, Node):
    def process(self):
        value = jsExprToPy(self.attrs.pop('value'))
        self.expr = value
        self.label = self.getLabel() + pathsep + self.attrs.pop('name')

class JumpEvent(Node):
    def process(self):
        if self.attrs.pop('scenechange', False):  # i made this up
            self.jumplabel = self.attrs.pop('path')
        else:
            self.jumplabel = sceneid + pathsep + slugify(self.attrs.pop('path').replace("/", pathsep))

    def toRpy(self):
        return f"jump {self.jumplabel}"

class Macro(NodeContainer, Node):
    def process(self):
        self.name = self.attrs.pop('name')
        self.label = self.getLabel() + pathsep + self.name

class NHSceneChange(NodeContainer, Node):
    def process(self):
        self.name = self.attrs.pop('name')
        self.label = self.getLabel() + pathsep + self.name

        jumplabel = slugify(self.attrs.pop('scene'))

        self.children.append(JumpEvent(attrs={
            "path": jumplabel,
            "scenechange": True
        }))

class Interaction(Node):
    def toRpy(self):
        return "extend ''"

class ParallelEvent(NodeBody, Node):
    # Or "DiscreteEvent"
    # Seems to just be a bunch of logic for interrupts?
    def process(self):
        if 'name' in self.attrs and not self.attrs['name'].startswith("_"):
            self.label = self.getLabel() + pathsep + slugify(self.attrs.pop('name'))
        else:
            self.label = None

        self.auto = self.attrs.get("auto", False)

    def toRpy(self):
        events = findNode(self.children, kind="events")
        if not events:
            print("Can't find events child")
            raise IndexError(self)
        # When to pause:
        # Definitely need to pause even for auto events as seen in battlemacro
        events.block(True)

        text = ""
        delay = self.attrs.pop("delay", 0)
        if delay:
            text += f"$ renpy.pause({delay}) # ParallelEvent Delay\n"


        if self.label:
            text += NodeContainer.toRpy(self)  # + '\nextend ""'
        else:
            text += NodeBody.toRpy(self)  # + '\nextend ""'

        return text

class Transitions(Node):
    pass

class Styles(Node):
    def process(self):
        self.kind = "styles"  # capitalization...

class SettingChange(Node):
    def toRpy(self):
        lines = []

        curtain_actor = self.attrs.pop("curtainActor", "curtain")
        curtain_fadetime = float(self.attrs.pop("curtainFadeTime", 0))
        bg_actor = self.attrs.pop("bgActor", "bg")
        bg_image = slugify(self.attrs.pop("bgImage"))

        # Set curtain image
        # Clear text
        # Fade in curtain
        # Do events (???) (Especially do ATL events)
        # Swap background
        # Fade our curtain
        lines.append(f"show i_sw_black as {curtain_actor}:")
        lines.append(f"    alpha 0.0")
        lines.append(f"    linear {curtain_fadetime} alpha 1.0")
        lines.append(f"$ renpy.pause({curtain_fadetime}) # Curtain fade")

        lines.append(f"show {bg_image} as {bg_actor} # behind {curtain_actor}")

        lines.append(NodeContainer.toRpy(self))
        lines.append(f"show i_sw_black as {curtain_actor}:")
        lines.append(f"    alpha 1.0")
        lines.append(f"    linear {curtain_fadetime} alpha 0.0")
        lines.append(f"$ renpy.pause({curtain_fadetime}) # Curtain fade")

        # TODO scene attributes

        return "\n".join(lines)

class SilhouetteMacro(NodeBody, Macro, Node):
    def process(self):
        # Overlapping transparency doesn't look quite right
        # but that's a renpy limitation :c

        # Fade out last actor
        lastActor = self.attrs.pop('lastActor', None)
        fadedur = self.attrs.pop('fadeTime', 0.5)
        if lastActor:
            self.children.append(ActorFade("ActorFade", attrs={
                "target": lastActor,
                "duration": fadedur,
                "opacity": 0.0
            }))

        # Silhouette fade in + first line of text
        silactor_id = self.attrs.pop('silActor')
        silImage = slugify(self.attrs.pop('silImage'))

        # Other character is always opposite cousin. 
        cousinx = self.attrs.pop('cousinX')
        self.attrs['axtorX'] = f"{int(100*(-1 * p2f(cousinx)))}%"

        styles = {}
        for macroattr, prop in {
            "actorScaleX": "scaleX",
            "actorScaleY": "scaleY",
            "actorY": "y",
            "axtorX": "x"
        }.items():
            if macroattr in self.attrs:
                styles[prop] = self.attrs.pop(macroattr)

        # Show sil with transforms
        self.children.append(ActorCreate("ActorCreate", attrs={
            "actorId": silactor_id,
            "actorType": "character",
            "duration": fadedur
        }, children=[
            Styles("styles", attrs={"image": silImage, "opacity": 0.0, **styles}),
            Transitions("transitions", attrs={"opacity": 1.0})
        ]))

        # First text

        char = self.attrs.pop('actorName')
        firstText = self.attrs.pop('firstText')

        secondtext = self.attrs.pop('secondText', None)

        if secondtext:
            self.children.append(TextEvent("TextEvent", attrs={
                "char": char,
                "text": firstText
            }))

        # Cousin move

        scalex = self.attrs.pop('cousinScaleX')
        cousin_id = self.attrs.pop('cousinActor')

        self.children.append(ActorEvent("ActorEvent", attrs={
            "target": cousin_id,
            "duration": 0.2,
        }, children=[
            Styles("styles", attrs={"scaleX": scalex}),
            Transitions("transitions", attrs={"x": cousinx})
        ]))

        # Silhouette replaced with real + second line of text extend

        realActor = self.attrs.pop('realActor')
        realImage = slugify(self.attrs.pop('realImage'))

        self.children.append(ActorEvent("ActorEvent", attrs={
            "target": silactor_id,
            "duration": fadedur,
            "delay": fadedur if not secondtext else 0
        }, children=[
            Transitions("transitions", attrs={"opacity": 0.0})
        ]))

        self.children.append(ActorCreate("ActorCreate", attrs={
            "actorId": realActor,
            "actorType": "character",
            "duration": fadedur,
            "delay": fadedur if not secondtext else 0
        }, children=[
            Styles("styles", attrs={"image": realImage, "opacity": 0.0, **styles}),
            Transitions("transitions", attrs={"opacity": 1.0})
        ]))

        if secondtext:
            if self.attrs.pop('appendSecond', False):
                self.children.append(TextEvent("TextEvent", attrs={
                    "char": char,
                    "text": secondtext,
                    "append": True
                }))
            else:
                self.children.append(TextEvent("TextEvent", attrs={
                    "char": char,
                    "text": secondtext
                }))
        else:
            self.children.append(TextEvent("TextEvent", attrs={
                "char": char,
                "text": firstText
            }))


class SuperSecretMacro(Node):
    def toRpy(self):
        return "call SuperSecretMacro"

class TextAsset(NoScript, Node):
    def process(self):
        value_txt = findNode(self.children, key="en").text
        assert value_txt is not None, self
        TextStore["@" + self.key] = value_txt

class TextEvent(Node):
    def process(self):
        self.textkey = self.attrs.pop('text', None)
        if self.textkey:
            self.text = re.sub(r"(\@[^ ]+)", lambda m: TextStore[m.group(1)], self.textkey)
        self.char = self.attrs.pop('char', "narrator")  # re.sub(r"\@([^ ]+)", lambda m: TextStore[m.group(1)], self.attrs['char'])

        if self.char == '':
            self.char = "narrator"

        if self.char == "@t_ch_galaga":
            self.text = "{smallcaps}" + self.text + "{/smallcaps}"

        # self.transform = self.attrs.pop('transform', None)
        self.extend = toPyValue(self.attrs.pop('append', False))

        self.block = 0 if self.attrs.pop('auto', False) else "NoAuto" # (self.extend)

        # self.letter_class = self.attrs.pop('letterClass', None)
        self.letter_delay = self.attrs.pop('letterDelay', None)
        self.delay = float(self.attrs.pop('delay', 0))

        # Default letter delay is .0125 . which is 80 CPS
        # 0.0125 second pause before each character?

    def toRpy(self):
        global last_say_what

        lines = []
        did_wait = False

        # ???
        # if self.block and isinstance(self.block, float):
        #     self.delay += self.block

        # Wait happens first (question mark?)
        if self.delay and not did_wait:
            if last_say_what:
                # You need to extend text, as seen with "The Next Day":

                # lines.append('$ renpy.pause(%s) # Text delay' % self.delay)
                lines.append('extend "{w=%s}{nw}"' % self.delay)
            else:
                lines.append('$ renpy.pause(%s) # Text delay' % self.delay)
            did_wait = True

        if not self.textkey:
            lines.append(f"# Blank text event " + repr(self))
        else:

            printtext = textToRpyInterp(self.text)
            last_say_what = printtext
            for chunk in [printtext]:
                is_last_chunk = True
                transform = self.attrs.pop('transform', None)
                if transform == "terezi":
                    for pattern, repl in [(c, "413"[i]) for i, c in enumerate("AIE")]:
                        chunk = re.sub(pattern, repl, chunk)

                global cps_mult
                if self.letter_delay:
                    cps_mult = round(0.0125 / float(self.letter_delay), 2)

                if cps_mult != 1.0:
                    chunk = "{cps=*" + str(cps_mult) + "}" + chunk + "{/cps}"

                nw = "{nw}"
                if is_last_chunk:
                    if self.delay and not did_wait:
                        nw = "{w=%s}" % self.delay
                        did_wait = True
                    elif self.block:
                        nw = ""

                if self.extend:
                    lines.append(f'extend " {chunk}{nw}" # {self.textkey} {self.block=}')
                else:
                    lines.append(f'{fixname(self.char)} "{chunk}{nw}" # {self.textkey} {self.block=}')

        return "\n".join(lines)


class VarEnsure(NoScript, Node):
    def process(self):
        self.storeName = self.attrs.pop('storeName')
        self.varName = self.attrs.pop('varName')
        self.value = toPyValue(self.attrs.pop('value'))
        AllStores.add(self.storeName)
        DefaultVars.append((self.storeName, self.varName, self.value))


class VarInc(Node):
    def process(self):
        self.storeName = self.attrs.pop('storeName')
        self.varName = self.attrs.pop('varName')
        AllStores.add(self.storeName)

    def toRpy(self):
        return f'$ {getStoreVarName(self.storeName, self.varName)} += 1'


class VarSet(Node):
    def process(self):
        self.storeName = self.attrs.pop('storeName', 'global')
        self.varName = self.attrs.pop('varName', None) or self.attrs.pop('name')
        self.value = toPyValue(self.attrs.pop('value'))
        AllStores.add(self.storeName)

    def toRpy(self):
        return f'$ {getStoreVarName(self.storeName, self.varName)} = {self.value!r}'


class YesNoChoice(Node):
    def process(self):
        self.auto = toPyValue(self.attrs.pop('auto'))
        self.name = self.attrs.pop('name')
        self.no_text = self.attrs.pop('noText')
        self.yes_text = self.attrs.pop('yesText')
        self.var_name = self.attrs.pop('varName')
        self.store_name = self.attrs.pop('storeName')
        self.promptText = self.attrs.pop('promptText', None)

    def toRpy(self):
        yes_text = TextStore.get(self.yes_text) or TextStore["@" + self.yes_text]
        no_text = TextStore.get(self.no_text) or TextStore["@" + self.no_text]

        lines = ["menu:"]
        if self.promptText:
            promptText = TextStore.get(self.promptText) or TextStore["@" + self.promptText]
            lines.append(f'    "{promptText}"\n')
        lines.append(f'    "{yes_text}":')
        lines.append(f'        $ {getStoreVarName(self.storeName, self.varName)} = True')
        lines.append(f'    "{no_text}":')
        lines.append(f'        $ {getStoreVarName(self.storeName, self.varName)} = False')
        return "\n".join(lines)


class LockoutChoice(YesNoChoice):
    pass

class Value(Node):
    pass

NODE_TYPES = {
    "ActorCreate": ActorCreate,
    "ActorCrossfade": ActorCrossfade,
    "ActorDepth": ActorDepth,
    "ActorDestroy": ActorDestroy,
    "ActorEvent": ActorEvent,
    "ActorFade": ActorFade,
    "ActorFlip": ActorFlip,
    "ActorImage": ActorImage,
    "ActorMove": ActorMove,
    "ActorReset": ActorReset,
    "ActorScale": ActorScale,
    "ActorTransform": ActorTransform,
    "AudioCreate": AudioCreate,
    "AudioDestroy": AudioDestroy,
    "AudioEvent": AudioEvent,
    "AudioOneShot": AudioOneShot,
    "BadEndMacro": BadEndMacro,
    "BattleMacro": BattleMacro,
    "BranchMacro": BranchMacro,
    "ConsoleEvent": ConsoleEvent,
    "CreditsEvent": CreditsEvent,
    "ExplorationMacro": ExplorationMacro,
    "events": Events,
    "FadeEvent": FadeEvent,
    "GameOver": GameOver,
    "HardSwap": HardSwap,
    "IfEqual": IfEqual,
    "IfFalse": IfFalse,
    "IfGTE": IfGTE,
    "IfLTE": IfLTE,
    "IfTrue": IfTrue,
    "JumpEvent": JumpEvent,
    "LockoutChoice": LockoutChoice,
    "Macro": Macro,
    "NHSceneChange": NHSceneChange,
    "NormalEndMacro": NormalEndMacro,
    "ParallelEvent": ParallelEvent,
    "SettingChange": SettingChange,
    "SilhouetteMacro": SilhouetteMacro,
    "SuperSecretMacro": SuperSecretMacro,
    "TextAsset": TextAsset,
    "TextEvent": TextEvent,
    "VarEnsure": VarEnsure,
    "VarInc": VarInc,
    "VarSet": VarSet,
    "YesNoChoice": YesNoChoice,
    "assets": Assets,
    "scene": Scene,
    "value": Value,
    "styles": Styles,
    "transitions": Transitions,
}
PROPERTY_NODES = [
    "depth",
    "id",
    "image",
    "opacity",
    "scaleX",
    "scaleY",
    "x",
    "y",
]
