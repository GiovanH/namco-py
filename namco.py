import re
import textwrap
import collections
import nc_hardcoded
from bs4 import NavigableString
from pprint import pprint
from types import GeneratorType

pathsep = "_"
sceneid = ""

SHOW_UNHANDLED_ATTRS = False

TextStore = nc_hardcoded.TextStore.copy()
ActorPrevStore = collections.defaultdict(lambda: None)
JumpLabelStore = []
unhandled_attrs = collections.defaultdict(set)
ActorIsFlipped = collections.defaultdict(lambda: 1.0)
last_image_for_tag = {}
AllStores = set()
DefaultVars = []
cps_mult = 1.0

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

    TextStore = nc_hardcoded.TextStore.copy()
    ActorPrevStore = collections.defaultdict(lambda: None)
    JumpLabelStore = []
    unhandled_attrs = collections.defaultdict(set)
    ActorIsFlipped = collections.defaultdict(lambda: 1.0)
    last_image_for_tag = {}
    AllStores = set()
    DefaultVars = []
    cps_mult = 1.0

# First, nodes are made and initialized.
# Then, Scene calls Preprocess, which assigns parents to nodes
# (we can't do this when we create them because they aren't built yet!)
# Finally, you can call getRpy on Scene

# Conversion

# ParallelEvents execute their contents(?) in parallel
# Need to time inner events (.duration prop?) and pause

# Renpy executes everything in parallel
# except for interactions
# and with statements

# Ideally we would make each interaction last a max time
# separately from the interaction logic
# Might be able to simulate this with renpy.pause?
# If not we should pause when there's a block and no interact

# Maybe look into how renpy interactions hook?
# Maybe move text to the end of the block so
# the interaction doesn't block animation?

# ATL: Need to group statements so 

    # show i_digdug_right as digdug:
    #     time 0.25 
    #     linear 0.0 ypos 0.75
    # # $ renpy.pause(0.25)
    # show i_digdug_right as digdug:
    #     time 0.5 
    #     linear 0.25 xpos 0.2
    # # $ renpy.pause(0.75)
    # show i_digdug_right as digdug:
    #     unflip(delay=0.75)
    # show i_digdug_right as digdug:
    #     time 1.0 
    #     linear 0.0 ypos 1.0

    #     becomes 

    # show i_digdug_right as digdug:
    #     time 0.25 
    #     linear 0.0 ypos 0.75
    #     time 0.5 
    #     linear 0.25 xpos 0.2
    #     unflip(delay=0.75)
    #     time 1.0 
    #     linear 0.0 ypos 1.0

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
    prev = ActorIsFlipped.get(actor, None)
    ActorIsFlipped[actor] = fl

    return f"xzoom {fl} # {factor} flipped {prev} -> {ActorIsFlipped.get(actor)}"


def allChildrenR(node):
    for c in node.children:
        yield c
        yield from allChildrenR(c)


transformation = {
    "opacity": lambda a, i: f"alpha {round(float(a), 2)} # {a}",
    "delay": lambda a, i: f"pause {round(float(a), 2)} # {a}",
    "x": lambda a, i: f"xpos {round(0.5 + p2f(a), 2)} # {a}",
    "y": lambda a, i: f"ypos {round(0.5 + p2f(a), 2)} # {a}",
    "scaleX": transformScaleX,
    "scaleY": lambda a, i: f"yzoom {float(a)} # {a}",
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

    atl_statements = ["# ShowWith"]
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
    def __init__(self, tag_name, attrs={}, children=[], text=""):
        super().__init__()
        self.__dict__.update(attrs)  # helper
        self.attrs = self.__dict__

        self.label = None
        self.parent = None
        self.kind = tag_name
        self.attrs = attrs
        self.children = children
        self.text = text

        self.attrs['kind'] = tag_name

    def preprocess(self):
        self.process()
        for child in self.children:
            child.parent = self
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
        selfr = f"<{self.__class__.__name__} {self.attrs} {self.kind} '{self.text}'>"
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

class NodeBody(Node):
    def toRpy(self, prefix=""):
        lines = []
        if prefix:
            lines.append(prefix)
        lines.append(textwrap.indent(repr(self), '# '))
        
        # Flatten macros

        i = 0
        while i < len(self.children):
            if isinstance(self.children[i], Events):
                self.children = self.children[:i] + [Annotation("Splice", text=repr(self.children[i]))] + self.children[i].children + self.children[i + 1:]
            i += 1

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
                                lines.append("$ renpy.pause()")
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
        ret = "\n".join(extra_lines) + NodeContainer.toRpy(self, prefix="scene i_sw_black with dissolve\nstop music fadeout\n")
        if unhandled_attrs and SHOW_UNHANDLED_ATTRS:
            print("Unhandled attributes:")
            pprint(unhandled_attrs)
        return ret
        
class Assets(NoScript, Node):
    pass  # Assets are handled when parsed

class Events(NodeBody, Node):
    def block(self, should_block):
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
                self.children[-1].block = "LastEvent"
            return
        else:
            # TODO: Pause for duration of inner animation.
            # Extend w=x for better visuals?
            if should_block:
                self.children.append(Interaction("Interaction"))


class ActorEvent(ATLSource, Node):
    def process(self):
        self.actor_id = self.attrs.pop('target')  # albatros

        self.styles = list(findNodes(self.children, kind="styles"))  # todo
        self.transitions = list(findNodes(self.children, kind="transitions"))
        self.interpolation = toRpyInterp(self.attrs.get("ease", "linear"))  # ease-out

    def getAtl(self):
        transitiondur = self.attrs.pop("duration", 0)
        delay = self.attrs.pop("delay", 0)

        for style in self.styles:
            
            atl_statements = ["# ActorEvent"]
            for pre_style, value in style.attrs.items():
                if pre_style in ['image', 'depth', 'kind', 'id']:
                    continue
                atl_statements.append(transformation[pre_style](value, self.actor_id))

            for t in self.transitions:
                for prop, value in t.attrs.items():
                    if prop in ['kind']:
                        continue
                    statement = f"pause {delay}\n" if delay else ""
                    statement += f"{self.interpolation} {transitiondur} " if transitiondur else ""
                    statement += transformation[prop](value, self.actor_id)
                    atl_statements.append(statement)

            return {
                "actor_id": style.attrs.get("id", self.actor_id),
                "image": style.attrs.get('image'),
                "zorder": style.attrs.get("depth"),
                "lines": atl_statements,
                "create": False
            }

        # Transition only

        atl_statements = ["# ActorEvent (Transition only)"]
        for t in self.transitions:
            for prop, value in t.attrs.items():
                if prop in ['kind']:
                    continue
                statement = f"pause {delay}\n" if delay else ""
                statement += f"{self.interpolation} {transitiondur} " if transitiondur else ""
                statement += transformation[prop](value, self.actor_id)
                atl_statements.append(statement)

            return {
                "actor_id": t.attrs.get("id", self.actor_id),
                "zorder": t.attrs.get("depth"),
                "delay": delay,
                "lines": atl_statements,
                "create": False
            }

class ActorCreate(ATLSource, Node):
    # or "DOMImageCreate"
    # can contain <transition>s and <style>s
    def process(self):
        self.actor_id = self.attrs.pop('actorId')  # albatros
        self.actor_type = self.attrs.pop('actorType')  # character

        self.styles = list(findNodes(self.children, kind="styles"))  # todo
        self.transitions = list(findNodes(self.children, kind="transitions")) or [Transitions("Transitions")]

        # self.transitions[0].attrs['duration'] = self.attrs.pop("duration", 0)
        self.name = self.attrs.get("name", None)  # _1
        self.allow_interrupt = self.attrs.get("allowInterrupt", True)  # bool
        self.auto = self.attrs.get("auto", False)  # bool
        self.interpolation = toRpyInterp(self.attrs.get("ease", "linear"))  # ease-out

    def getAtl(self):
        atl = ActorEvent.getAtl(self)
        atl['create'] = True
        return atl

class ActorCrossfade(ATLSource, Node):
    def getAtl(self):

        fadedur = self.attrs.pop("duration")
        target = self.attrs.pop("target")
        image = slugify(self.attrs.pop("image"))

        return {
            "actor_id": target,
            "image": image,
            "with": f"Dissolve({fadedur})"
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
    def getAtl(self):
        return showActorWithAtl(self, ['opacity'])

class ActorFlip(ATLSource, Node):
    def process(self):
        self.actor = self.attrs.pop('target')

        self.interp = toRpyInterp(self.attrs.pop('ease', 'linear'))
        self.duration = self.attrs.pop('duration', 0)
        self.delay = self.attrs.pop('delay', 0)

    def getAtl(self):
        prev = ActorIsFlipped[self.actor]
        xzoom = prev * -1

        lines = [f"# ActorFlip (from {prev})"]

        if self.delay:
            lines.append(f"pause {self.delay}")

        statement = f"{self.interp} {self.duration} " if self.duration else ""
        statement += transformScaleX(xzoom, self.actor)

        lines.append(statement)

        return {
            "actor_id": self.actor,
            "lines": lines
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
        self.delay = self.attrs.get('delay', 0)

    def getAtl(self):
        return {
            "actor_id": self.actor,
            "image": self.image,
        }

class ActorMove(ATLSource, Node):
    def getAtl(self):
        return showActorWithAtl(self, ['x', 'y'])

class ActorReset(NoScript, Node):
    pass

class ActorScale(ATLSource, Node):
    def process(self):
        if 'x' in self.attrs:
            self.attrs['scaleX'] = self.attrs.pop('x')
        if 'y' in self.attrs:
            self.attrs['scaleY'] = self.attrs.pop('y')

    def getAtl(self):
        return showActorWithAtl(self, ['scaleX', 'scaleY'])

class ActorTransform(Node):
    def getAtl(self):
        return showActorWithAtl(self, ['scaleX', 'scaleY', 'x', 'y'])

AudioLayer = {}

class AudioCreate(Node):
    def process(self):
        self.layer = self.attrs.pop('layer')
        self.loop = toPyValue(self.attrs.pop('loop'))
        # self.play = toPyValue(self.attrs.pop('play'))
        self.path = toPyValue(self.attrs.pop('sound'))
        self.delay = toPyValue(self.attrs.pop('delay',  None))

        if self.layer == "bgm":
            self.layer = "music"
        elif self.layer == "sfx":
            self.layer = "sound"
        else:
            raise ValueError(self.layer)

        AudioLayer[self.attrs.pop('audioId')] = self.layer

        # TODO: Unused attrs audioId, play, volume, delay, allowInterrupt

    def toRpy(self):
        real_path = re.sub(r"@a_([a-z]+)_(.*)", r"\g<1>/\g<2>.ogg", self.path)
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
        fadeduration = float(self.attrs.pop("fadeDuration"))
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


class NormalEndMacro(Node):
    # todo too complicated for renpy
    pass


class BadEndMacro(Node):
    def process(self):
        self.expr = jsExprToPy(self.attrs.pop('varName'))
        # TODO I DON'T KNOW HOW THIS WORKS?
        # lvalue = varname
        # rvalue = 1



    def toRpy(self):
        return f"$ {self.expr} = 1\ncall BadEndMacro"

class BattleMacro(NodeBody, Node):
    def toRpy(self):
        return f"call BattleMacro('{self.attrs.pop('partnerActor', None)}')\n" + NodeBody.toRpy(self)
    # def process(self):


    #     # Zoom in on evil namco
    #     self.children.append(ActorEvent("ActorEvent", attrs={
    #         "target": cousin_id,
    #         "duration": 0.5,
    #     }, children=[
    #         Styles("styles", attrs={"scaleX": scalex}),
    #         Transitions("transitions", attrs={"x": cousinx})
    #     ]))

    # pass

    # Thunderclap!
    # ease out

    # Fade in evil namco robots
    # evil linear move left

    # on thunderclaps:
    # Fade in partner, right top
    # Fade in cousin, right bottom

    # Move together, fade to white
    # Fade to black

    # Roll credits (handled by other)


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
        return f"if {self.comparison}:\n    jump {self.jumplabel}"


class ConsoleEvent(Node):
    def toRpy(self):
        value = self.attrs.pop("value")
        return f'$ print("{value}")'

class CreditsEvent(Node):
    def toRpy(self):
        return "call credits"

class ExplorationMacro(NodeContainer, Node):
    def process(self):
        self.label = self.attrs.pop('name')
        self.pass_text = self.attrs.pop('passText')
        self.lockout = toPyValue(self.attrs.pop('lockout'))
        self.store_name = self.attrs.get("storeName", "scene")
        self.var_name = "explore" + self.attrs.pop('sceneName')

    def toRpy(self):
        lines = ['menu (screen="ChoiceExploration"):']
        for name, id in nc_hardcoded.char_name_to_id.items():
            # target = getPrevLevel(self) + pathsep + id
            target = sceneid + pathsep + id
            lines.append(f'    "{name}":')
            lines.append(f'        jump {target}')
        # TODO: Only pass if you've talked to somebody!
        # target = getPrevLevel(self) + pathsep + "cousin"
        target = sceneid + pathsep + "cousin"
        try:
            lines.append(f'    "{TextStore[self.pass_text]}":')
        except KeyError: # i have no idea
            lines.append(f'    "{TextStore["@" + self.pass_text]}":')
        lines.append(f'        jump {target}')
        return "\n".join(lines)

class FadeEvent(ATLSource, Node):
    def getAtl(self):
        actor_id = self.attrs.pop('target')
        target_opacity = float(self.attrs.pop('to'))

        atl_statement = []
        if 'duration' in self.attrs:
            duration = float(self.attrs.pop('duration'))
            if duration > 0:
                atl_statement.append(f"linear {float(duration)}")
        atl_statement.append(f"alpha {target_opacity}")

        return {
            "actor_id": actor_id,
            "lines": ["# FadeEvent", " ".join(atl_statement)]
        }

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
        self.jumplabel = sceneid + pathsep + slugify(self.attrs.pop('path').replace("/", pathsep))

    def toRpy(self):
        return f"jump {self.jumplabel}"

class Macro(NodeContainer, Node):
    def process(self):
        self.name = self.attrs.pop('name')
        self.label = self.getLabel() + pathsep + self.name

class NHSceneChange(Node):
    def process(self):
        self.jumplabel = slugify(self.attrs.pop('scene'))

    def toRpy(self):
        return f"jump {self.jumplabel}"

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

        self.auto = self.attrs.pop("auto", False)

    def toRpy(self):
        findNode(self.children, kind="events").block(not self.auto)

        if self.label:
            return NodeContainer.toRpy(self)  # + '\nextend ""'
        else:
            return NodeBody.toRpy(self)  # + '\nextend ""'

class Transitions(Node):
    pass

class Styles(Node):
    def process(self):
        assert self.kind == "styles"  # capitalization...

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
        lines.append(f"$ renpy.pause({curtain_fadetime})")

        lines.append(f"show {bg_image} as {bg_actor} # behind {curtain_actor}")

        lines.append(NodeContainer.toRpy(self))
        lines.append(f"show i_sw_black as {curtain_actor}:")
        lines.append(f"    alpha 1.0")
        lines.append(f"    linear {curtain_fadetime} alpha 0.0")
        lines.append(f"$ renpy.pause({curtain_fadetime})")

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
    # TODO:
    # var a = !0,
    #     b = c.scenes;
    # for (var d in b) {
    #     var e = "got_trueend_" + b[d];
    #     a = a && f.get(e, "game")
    # }
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

        # todo
        # self.transform = self.attrs.pop('transform', None)
        self.extend = toPyValue(self.attrs.pop('append', False))

        self.block = False if self.attrs.pop('auto', False) else "NoAuto" # (self.extend)

        # self.letter_class = self.attrs.pop('letterClass', None)
        self.letter_delay = self.attrs.pop('letterDelay', None)
        self.delay = self.attrs.pop('delay', 0)

        # Default letter delay is .0125 . which is 80 CPS
        # 0.0125 second pause before each character?

    def toRpy(self):

        lines = []
        did_wait = False

        # Wait happens first (question mark?)
        if self.delay and not did_wait:
            lines.append('extend "{w=%s}"' % self.delay)
            did_wait = True

        if not self.textkey:
            lines.append("# Blank text event " + repr(self))
        else:
            printtext = textToRpyInterp(self.text)
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
                    chunk = "{cps=*" + str(cps_mult) + "}" + chunk

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
