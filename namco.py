import re
import textwrap
import collections
import nc_hardcoded
from bs4 import NavigableString

TextStore = nc_hardcoded.TextStore.copy()
ActorPrevStore = collections.defaultdict(default=None)
JumpLabelStore = []

AllStores = set()

pathsep = "_"
sceneid = ""

last_image_for_tag = {}

ActorIsFlipped = collections.defaultdict(default=False)

# First, nodes are made and initialized.
# Then, Scene calls Preprocess, which assigns parents to nodes
# (we can't do this when we create them because they aren't built yet!)
# Finally, you can call getRpy on Scene

# Conversion



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
    text = re.sub(r"\${(.+):(.+?)}", r"[\g<1>.\g<2>]", text)
    return text

def fixname(char):
    fixes = {
        "t_ch_tutorial": "narrator",
        # "max": "bluemax",
    }
    return fixes.get(char, char).replace("@", "")

def toPyValue(value):
    if value == "false":
        return False
    elif value == "true":
        return True
    else:
        return value

def getStoreVarName(storeName, varName):
    AllStores.add(storeName)
    return f"{storeName}.{varName}"

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
    return float(x.strip('%'))/100

def getPrevLevel(node):
    named_parent = None
    while not named_parent or not named_parent.label:
        named_parent = (named_parent.parent if named_parent else node.parent)
    return node.parent.getLabel().replace(pathsep + named_parent.name, "")

def slugify(string):
    assert "/" not in string, string
    return string.replace("@", "").replace(".", "p")

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
                assert child.name not in tag.attrs
                tag.attrs[child.name] = child.text
            else:
                children.append(Node.fromTag(child))
        return node_cls(tag.name, tag.attrs, children, text)

    def __repr__(self):
        if self.children:
            childrenstr = "\n".join(str(c) for c in self.children)
            return f"""<{self.__class__.__name__} {self.attrs} {self.kind} '{self.text}'
    {textwrap.indent(childrenstr, "    ")}
>"""
        else:
            return f"<{self.__class__.__name__} {self.attrs} {self.kind} '{self.text}'>"

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
        return f"# Pass ({self.kind})\n"

class NodeContainer(Node):
    def toRpy(self):
        return f"# <{self.__class__.__name__} {self.attrs} {self.kind} '{self.text}'>\nlabel {self.label}:\n" + textwrap.indent(NodeBody.toRpy(self), "    ")

class NodeBody(Node):
    def toRpy(self):
        if self.attrs or self.text:
            return f"# <{self.__class__.__name__} {self.attrs} {self.kind} '{self.text}'>\n" + "\n".join([s for s in [c.toRpy() for c in self.children] if s])
        else:
            return "\n".join([s for s in [c.toRpy() for c in self.children] if s])
        
class ATLSource(Node):
    def getAtl():
        return {
            actor_id: None,
            lines: []
        }

# Actual stuff

class Scene(NodeContainer, Node):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.preprocess()

    def process(self):
        self.label = self.attrs["id"].replace('.', '_')
        self.name = self.label
        global sceneid
        sceneid = self.label

    def makeExtraLines(self):
        extra_lines = []
        for store_name in AllStores:
            extra_lines.append(f"define {store_name} =" + " renpy.python.StoreModule({})\n")
        return extra_lines

    def toRpy(self):
        extra_lines = self.makeExtraLines()
        return "\n".join(extra_lines) + NodeContainer.toRpy(self)
        
class Assets(NoScript, Node):
    pass  # Assets are handled when parsed

class Events(NodeBody, Node):
    pass  # Events is a plain container, doesn't have attrs.
    # TODO: Events can have strings in it?


transformation = {
    "opacity": lambda a: f"alpha {float(a)}",
    "delay": lambda a: f"pause {float(a)}",
    "x": lambda a: f"xpos {0.5 + p2f(a)}",
    "y": lambda a: f"ypos {1.0 + p2f(a)}",
    "scaleX": lambda a: f"xzoom {float(a)}",
    "scaleY": lambda a: f"yzoom {float(a)}",
}

class ActorEvent(ATLSource, Node):
    def process(self):
        self.actor_id = self.attrs['target']  # albatros

        self.styles = list(findNodes(self.children, kind="styles"))  # todo
        self.transitions = list(findNodes(self.children, kind="transitions"))
        self.interpolation = toRpyInterp(self.attrs.get("ease", "linear"))  # ease-out

    def getAtl():
        lines = []
        for style in self.styles:
            actor_id = style.attrs.get("id", self.actor_id)
            if 'image' in style.attrs:
                image = slugify(style.attrs['image'])
                last_image_for_tag[actor_id] = image
                statement = f"show {image}"
                if 'depth' in style.attrs:
                    statement += (f" zorder {style.attrs['depth']}")
                statement += f" as {actor_id} at default"

                atl_statements = []
                for pre_style, value in style.attrs.items():
                    if pre_style in ['image', 'depth', 'kind', 'id']:
                        continue
                    atl_statements.append(transformation[pre_style](value))

                transitiondur = self.attrs.get("duration", 0)
                for t in self.transitions:
                    for style, value in t.attrs.items():
                        if style in ['kind']:
                            continue
                        atl_statements.append(f"{self.interpolation} {transitiondur} " + transformation[style](value))

                if atl_statements:
                    statement += ":\n" + textwrap.indent("\n".join(atl_statements), "    ")

                lines.append(statement)

            # return {
            #     "actor_id": self.actor_id,
            #     "zorder": style.attrs.get("depth"),
            #     "lines": lines
            # }

def toRpyInterp(interpolation):
    return {
        "linear": "linear",
        "ease": "ease",
        "ease-out": "easeout",
        "ease-in": "easein",
        "ease-in-out": "ease_expo"
    }[interpolation]

class ActorCreate(ActorEvent, Node):
    # or "DOMImageCreate"
    # can contain <transition>s and <style>s
    def process(self):
        self.actor_id = self.attrs['actorId']  # albatros
        self.actor_type = self.attrs['actorType']  # character

        self.styles = list(findNodes(self.children, kind="styles"))  # todo
        self.transitions = list(findNodes(self.children, kind="transitions"))

        self.transition_duration = self.attrs.get("duration", 0)
        self.name = self.attrs.get("name", None)  # _1
        self.allow_interrupt = self.attrs.get("allowInterrupt", True)  # bool
        self.auto = self.attrs.get("auto", False)  # bool
        self.interpolation = toRpyInterp(self.attrs.get("ease", "linear"))  # ease-out

    def toRpy(self):
        #todo still a LOT unhandled here
        extra_lines = []
        extra_lines.append(ActorEvent.toRpy(self))
        return "\n".join(extra_lines)

class ActorCrossfade(Node):
    pass

class ActorDepth(Node):
    # or "DepthShortcut"
    pass

class ActorDestroy(Node):
    def toRpy(self):
        target = last_image_for_tag[self.attrs['target']]
        return f"hide {target}"

def showActorWithAtl(node, fields):
    actor_id = node.attrs['target']
    target = last_image_for_tag[actor_id]
    interpolation = toRpyInterp(node.attrs.get("ease", "linear"))  # ease-out
    duration = node.attrs.get("duration", 0)

    statement = f"show {target}"
    statement += f" as {actor_id}"

    atl_statements = []
    pause = 0

    delay = node.attrs.get("delay", 0)

    if delay:
        atl_statements.append(f"time {float(delay)} ")
        pause += float(delay)

    for style, value in node.attrs.items():
        if style in fields:
            atl_statements.append(f"{interpolation} {float(duration)} " + transformation[style](value))
            pause += float(duration)

    if atl_statements:
        statement += ":\n" + textwrap.indent("\n".join(atl_statements), "    ")
    if pause:
        statement += f"\n# $ renpy.pause({pause})"

    return statement



class ActorFade(Node):
    def toRpy(self):
        return showActorWithAtl(self, ['opacity'])

class ActorFlip(Node):
    def process(self):
        self.actor = self.attrs['target']
        self.atlattrs = {}
        
        for atr in ['duration', 'ease', 'delay']:
            if self.attrs.get(atr):
                try:
                    self.atlattrs[atr] = float(self.attrs.get(atr))
                except:
                    self.atlattrs[atr] = self.attrs.get(atr)
        self.atlattrs = ", ".join(f"{k}={v}" for k, v in self.atlattrs.items())

    def toRpy(self):
        flip_transform = "unflip" if ActorIsFlipped.get(self.actor) else "flip"
        ActorIsFlipped[self.actor] = not ActorIsFlipped.get(self.actor)
        if self.atlattrs:
            return f"show {last_image_for_tag[self.actor]}:\n    {self.actor} at {flip_transform}({self.atlattrs})"
        else:
            return f"show {last_image_for_tag[self.actor]}:\n    {self.actor} at {flip_transform}()"

class ActorImage(Node):
    # or "ImageShortcut"
    # I THINK this means 
    # Set actor <actor>'s image to <image>
    def process(self):
        self.image = slugify(self.attrs['image'])
        self.actor = self.attrs['target']

        self.name = self.attrs.get('name', None)
        self.auto = toPyValue(self.attrs.get('auto', False))
        self.delay = self.attrs.get('delay', 0)

    def toRpy(self):
        lines = []
        if self.delay:
            lines.append(f"$ renpy.pause({self.delay})")
        last_image_for_tag[self.actor] = self.image
        lines.append(f"show {self.image} as {self.actor}")
        return "\n".join(lines)


class ActorMove(Node):
    def toRpy(self):
        return showActorWithAtl(self, ['x', 'y'])

class ActorReset(Node):
    pass

class ActorScale(Node):
    pass

class ActorTransform(Node):
    pass

class AudioCreate(Node):
    def process(self):
        self.layer = self.attrs['layer']
        self.loop = toPyValue(self.attrs['loop'])
        self.play = toPyValue(self.attrs['play'])
        self.path = toPyValue(self.attrs['sound'])

        if self.layer == "bgm":
            self.layer = "music"
        elif self.layer == "sfx":
            self.layer = "sound"
        else:
            raise ValueError(self.layer)

        # TODO: Unused attrs audioId, play, volume, delay, allowInterrupt

    def toRpy(self):
        real_path = re.sub(r"@a_([a-z]+)_(.*)", r"\g<1>/\g<2>.ogg", self.path)
        return f'play {self.layer} "{real_path}" {"loop" if self.loop else "noloop"}'

class AudioDestroy(Node):
    pass

class AudioEvent(Node):
    pass

class AudioOneShot(Node):   
    def process(self):
        self.sound = self.attrs['sound']
        self.delay = self.attrs.get('delay', 0)
        self.channel = "sound"

    def toRpy(self):
        sound_path = re.sub(r"@a_([a-z]+)_(.*)", r"\g<1>/\g<2>.ogg", self.sound)
        if self.delay:
            return f'play {self.channel} ["<silence {self.delay}>", "{sound_path}"]'
        else:
            return f'play {self.channel} "{sound_path}"'

class BadEndMacro(Node):
    pass

class BattleMacro(Node):
    pass

class BranchMacro(Node):
    pass

class ConsoleEvent(Node):
    pass

class CreditsEvent(Node):
    pass

class ExplorationMacro(NodeContainer, Node):
    def process(self):
        self.label = self.attrs['name']
        self.pass_text = self.attrs['passText']
        self.lockout = toPyValue(self.attrs['lockout'])
        self.store_name = self.attrs.get("storeName", "scene")
        self.var_name = "explore" + self.attrs['sceneName']

    def toRpy(self):
        lines = ["menu:"]
        for name, id in nc_hardcoded.char_name_to_id.items():
            # target = getPrevLevel(self) + pathsep + id
            target = sceneid + pathsep + id
            lines.append(f'    "{name}":')
            lines.append(f'        jump {target}')
        # TODO: Only pass if you've talked to somebody!
        # target = getPrevLevel(self) + pathsep + "cousin"
        target = sceneid + pathsep + "cousin"
        lines.append(f'    "{TextStore[self.pass_text]}":')
        lines.append(f'        jump {target}')
        return "\n".join(lines)

    # todo charlist

class FadeEvent(Node):
    def toRpy(self):
        actor_id = self.attrs['target']
        target = last_image_for_tag[actor_id]

        statement = f"show {target}"
        statement += f" as {actor_id}"

        atl_statement = []
        if 'duration' in self.attrs:
            atl_statement.append(f"linear {float(self.attrs['duration'])}")
        atl_statement.append(f"alpha {float(self.attrs['to'])}")
        if atl_statement:
            statement += ":\n" + textwrap.indent(" ".join(atl_statement), "    ")

        return statement

class GameOver(Node):
    pass

class HardSwap(Node):
    pass

class IfExpr(NodeContainer, Node):
    def toRpy(self):
        return f"if {self.expr}:\n" + textwrap.indent(NodeContainer.toRpy(self), "    ")


class IfEqual(Node):
    pass

class IfFalse(IfExpr, Node):
    def process(self):
        value = textToRpyInterp(self.attrs['value'])
        value = re.sub(r"^\[(.+)\]$", r"\g<1>", value)
        self.expr = f"not {value}"
        self.label = self.getLabel() + pathsep + self.attrs['name']

class IfGTE(Node):
    pass

class IfLTE(Node):
    pass

class IfTrue(IfExpr, Node):
    def process(self):
        value = textToRpyInterp(self.attrs['value'])
        value = re.sub(r"^\[(.+)\]$", r"\g<1>", value)
        self.expr = value
        self.label = self.getLabel() + pathsep + self.attrs['name']

class JumpEvent(Node):
    def process(self):
        self.jumplabel = sceneid + pathsep + slugify(self.attrs['path'].replace("/", pathsep))

    def toRpy(self):
        return f"jump {self.jumplabel}"

class LockoutChoice(Node):
    pass

class Macro(NodeContainer, Node):
    def process(self):
        self.name = self.attrs['name']
        self.label = self.getLabel() + pathsep + self.name

class NHSceneChange(Node):
    def process(self):
        self.jumplabel = slugify(self.attrs['scene'])

    def toRpy(self):
        return f"jump {self.jumplabel}"

class NormalEndMacro(Node):
    pass

class ParallelEvent(NodeBody, Node):
    # Or "DiscreteEvent"
    # Seems to just be a bunch of logic for interrupts?
    def process(self):
        self.label = self.getLabel() + pathsep + self.name

    def toRpy(self):
        if self.name.startswith("_"):
            return NodeBody.toRpy(self)
        else:
            return NodeContainer.toRpy(self)

class Transitions(Node):
    pass

class Styles(Node):
    pass

class SettingChange(Node):
    pass

class SilhouetteMacro(Node):
    pass

class SuperSecretMacro(Node):
    # TODO:
    # var a = !0,
    #     b = c.scenes;
    # for (var d in b) {
    #     var e = "got_trueend_" + b[d];
    #     a = a && f.get(e, "game")
    # }
    def toRpy(self):
        return "jump s_supersecret"

class TextAsset(NoScript, Node):
    def process(self):
        value_txt = findNode(self.children, key="en").text
        assert value_txt is not None, self
        TextStore["@" + self.key] = value_txt

class TextEvent(Node):
    def process(self):
        self.text = re.sub(r"(\@[^ ]+)", lambda m: TextStore[m.group(1)], self.attrs['text'])
        self.char = self.attrs['char']  # re.sub(r"\@([^ ]+)", lambda m: TextStore[m.group(1)], self.attrs['char'])

        # todo
        self.transform = self.attrs.get('transform', None)
        self.extend = toPyValue(self.attrs.get('append', False))

        self.letter_class = self.attrs.get('letterClass', None)
        self.letter_delay = self.attrs.get('letterDelay', None)

    def toRpy(self):
        if not self.char:
            return "# Blank text event"
        nw = "" # ""{nw}" if self.attrs.get('auto') else ""
        if self.extend:
            return f'extend " {textToRpyInterp(self.text)}{nw}"'
        else:
            return f'{fixname(self.char)} "{textToRpyInterp(self.text)}{nw}"'


class VarEnsure(Node):
    def process(self):
        self.storeName = self.attrs['storeName']
        self.varName = self.attrs['varName']
        self.value = toPyValue(self.attrs['value'])
        AllStores.add(self.storeName)

    def toRpy(self):
        return f'if not {self.storeName}.__dict__.get({self.varName!r}):\n    $ {self.storeName}.{self.varName} = {self.value!r}'


class VarInc(Node):
    pass

class VarSet(Node):
    pass

class YesNoChoice(Node):
    def process(self):
        self.auto = toPyValue(self.attrs['auto'])
        self.name = self.attrs['name']
        self.no_text = self.attrs['noText']
        self.yes_text = self.attrs['yesText']
        self.var_name = self.attrs['varName']
        self.store_name = self.attrs['storeName']
        self.promptText = self.attrs.get('promptText', None)

    def toRpy(self):
        lines = ["menu:"]
        lines.append(f'    "{TextStore[self.yes_text]}":')
        lines.append(f'        $ {self.store_name}.{self.var_name} = True')
        lines.append(f'    "{TextStore[self.no_text]}":')
        lines.append(f'        $ {self.store_name}.{self.var_name} = False')
        return "\n".join(lines)

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
