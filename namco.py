import re
import textwrap
import collections
import nc_hardcoded
from bs4 import NavigableString
from pprint import pprint

TextStore = nc_hardcoded.TextStore.copy()
ActorPrevStore = collections.defaultdict(default=None)
JumpLabelStore = []
unhandled_attrs = collections.defaultdict(set)
from types import GeneratorType

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
    text = re.sub(r"\${(.+?):(.+?)}", r"[st_\g<1>.\g<2>]", text)
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
    return f"st_{storeName}.{varName}"

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
                assert child.name not in tag.attrs, (child, tag)
                assert not child.attrs
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
        if not self.label:
            return NodeBody.toRpy(self)
        return f"# <{self.__class__.__name__} {self.attrs} {self.kind} '{self.text}'>\nlabel {self.label}:\n" + textwrap.indent(NodeBody.toRpy(self), "    ")


def resolveAtl(atl):
    actor_id = atl['actor_id']
    atl_statements = atl['lines']

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
        statement += f" at default"

    if atl_statements:
        statement += ":\n" + textwrap.indent("\n".join(atl_statements), "    ")
    return statement


class NodeBody(Node):
    def toRpy(self):
        lines = []
        if self.attrs or self.text:
            lines.append(f"# <{self.__class__.__name__} {self.attrs} {self.kind} '{self.text}'>)")
        
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
                        atl_buffer['lines'] += atl['lines']

                        if atl.get("image"):
                            assert not atl_buffer.get("image")
                            target = slugify(atl.get("image"))
                            last_image_for_tag[actor_id] = target
                            atl_buffer['image'] = target
                    else:
                        atl_buffer = atl
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
        super().__init__(*args, **kwargs)
        self.preprocess()
        print("Scene", self.name, "processed!")

    def process(self):
        self.label = self.attrs.pop("id").replace('.', '_')
        self.name = self.label
        global sceneid
        sceneid = self.label

    def makeExtraLines(self):
        extra_lines = []
        for store_name in AllStores:
            #extra_lines .append(f"define {store_name} =" + " renpy.python.StoreModule({})\n")
            extra_lines.append(f"init python in st_{store_name}:\n    pass\n\n")
        return extra_lines

    def toRpy(self):
        extra_lines = self.makeExtraLines()
        if unhandled_attrs:
            print("Unhandled attributes:")
            pprint(unhandled_attrs)
        return "\n".join(extra_lines) + NodeContainer.toRpy(self)
        
class Assets(NoScript, Node):
    pass  # Assets are handled when parsed

class Events(NodeBody, Node):
    pass  # Events is a plain container, doesn't have attrs.
    # TODO: Events can have strings in it?

def transformScaleX(factor, actor):
    fl = float(factor)
    if (fl == -1.0):
        ActorIsFlipped[actor] = True
    elif (fl == 1.0):
        ActorIsFlipped[actor] = False
    return f"xzoom {fl} # {factor} flipped={ActorIsFlipped.get(actor)}"


transformation = {
    "opacity": lambda a, i: f"alpha {float(a)} # {a}",
    "delay": lambda a, i: f"pause {float(a)} # {a}",
    "x": lambda a, i: f"xpos 0.5 + {p2f(a)} # {a}",
    "y": lambda a, i: f"ypos 0.5 + {p2f(a)} # {a}",
    "scaleX": transformScaleX,
    "scaleY": lambda a, i: f"yzoom {float(a)} # {a}",
}


class ActorEvent(ATLSource, Node):
    def process(self):
        self.actor_id = self.attrs.pop('target')  # albatros

        self.styles = list(findNodes(self.children, kind="styles"))  # todo
        self.transitions = list(findNodes(self.children, kind="transitions"))
        self.interpolation = toRpyInterp(self.attrs.get("ease", "linear"))  # ease-out

    def getAtl(self):
        transitiondur = self.attrs.pop("duration", 0)

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
                    statement = f"{self.interpolation} {transitiondur} " if transitiondur else ""
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
                statement = f"{self.interpolation} {transitiondur} " if transitiondur else ""
                statement += transformation[prop](value, self.actor_id)
                atl_statements.append(statement)

            return {
                "actor_id": t.attrs.get("id", self.actor_id),
                "zorder": t.attrs.get("depth"),
                "lines": atl_statements,
                "create": False
            }

def toRpyInterp(interpolation):
    return {
        "linear": "linear",
        "ease": "ease",
        "ease-out": "easeout",
        "ease-in": "easein",
        "ease-in-out": "ease_expo"
    }[interpolation]

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

        yield {
            "actor_id": target,
            "lines": ["# crossfade 1", f"alpha 0.0"],
            "duration": fadedur,

        }

        yield {
            "actor_id": target,
            "image": image,
            "lines": ["# crossfade 2", f"alpha 1.0"],
            "duration": fadedur
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
        target = last_image_for_tag[self.attrs.pop('target')]
        return f"hide {target}"

def showActorWithAtl(node, fields):
    interpolation = toRpyInterp(node.attrs.get("ease", "linear"))  # ease-out
    duration = node.attrs.pop("duration", 0.5)

    atl_statements = ["# ShowWith"]
    pause = 0

    delay = node.attrs.pop("delay", 0)

    target = node.attrs.pop('target')

    if delay:
        atl_statements.append(f"time {float(delay)} ")
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



class ActorFade(ATLSource, Node):
    def getAtl(self):
        return showActorWithAtl(self, ['opacity'])

class ActorFlip(ATLSource, Node):
    def process(self):
        self.actor = self.attrs.pop('target')
        self.atlattrs = {}
        
        for atr in ['duration', 'ease', 'delay']:
            if self.attrs.get(atr):
                val = self.attrs.pop(atr)
                if atr == 'ease':
                    self.atlattrs[atr] = toRpyInterp(val)
                    continue
                try:
                    self.atlattrs[atr] = float(val)
                except:
                    self.atlattrs[atr] = val
                
        self.atlattrs = ", ".join(f"{k}={v}" for k, v in self.atlattrs.items())

    def getAtl(self):
        flip_transform = "unflip" if ActorIsFlipped.get(self.actor) else "flip"
        ActorIsFlipped[self.actor] = not ActorIsFlipped.get(self.actor)
        return {
            "actor_id": self.actor,
            "lines": [f"{flip_transform}({self.atlattrs})"]
        }

class ActorImage(Node):
    # or "ImageShortcut"
    # I THINK this means 
    # Set actor <actor>'s image to <image>
    def process(self):
        self.image = slugify(self.attrs.pop('image'))
        self.actor = self.attrs.pop('target')

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
    pass

class AudioCreate(Node):
    def process(self):
        self.layer = self.attrs.pop('layer')
        # self.loop = toPyValue(self.attrs.pop('loop'))
        # self.play = toPyValue(self.attrs.pop('play'))
        self.path = toPyValue(self.attrs.pop('sound'))

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
        self.sound = self.attrs.pop('sound')
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
    pass

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

class FadeEvent(Node):
    def toRpy(self):
        actor_id = self.attrs.pop('target')
        target = last_image_for_tag[actor_id]

        statement = f"show {target}"
        statement += f" as {actor_id}"

        atl_statement = []
        if 'duration' in self.attrs:
            duration = float(self.attrs.pop('duration'))
            if duration > 0:
                atl_statement.append(f"linear {float()}")
        atl_statement.append(f"alpha {duration}")
        if atl_statement:
            statement += ":\n" + textwrap.indent(" ".join(atl_statement), "    ")

        return statement

class GameOver(Node):
    def toRpy(self):
        return "return"

class HardSwap(Node):
    pass

class IfExpr(NodeContainer, Node):
    def toRpy(self):
        return f"if {self.expr}:\n" + textwrap.indent(NodeContainer.toRpy(self), "    ")

class IfEqual(IfExpr, Node):
    def process(self):
        lvalue = textToRpyInterp(self.attrs.pop('lvalue'))
        lvalue = re.sub(r"^\[(.+)\]$", r"\g<1>", lvalue)
        rvalue = textToRpyInterp(self.attrs.pop('rvalue'))
        rvalue = re.sub(r"^\[(.+)\]$", r"\g<1>", rvalue)
        self.expr = f"{lvalue} == {rvalue}"
        self.label = self.getLabel() + pathsep + self.attrs.pop('name')

class IfFalse(IfExpr, Node):
    def process(self):
        value = textToRpyInterp(self.attrs.pop('value'))
        value = re.sub(r"^\[(.+)\]$", r"\g<1>", value)
        self.expr = f"not {value}"
        self.label = self.getLabel() + pathsep + self.attrs.pop('name')

class IfGTE(IfExpr, Node):
    def process(self):
        lvalue = textToRpyInterp(self.attrs.pop('lvalue'))
        lvalue = re.sub(r"^\[(.+)\]$", r"\g<1>", lvalue)
        rvalue = textToRpyInterp(self.attrs.pop('rvalue'))
        rvalue = re.sub(r"^\[(.+)\]$", r"\g<1>", rvalue)
        self.expr = f"{lvalue} >= {rvalue}"
        self.label = self.getLabel() + pathsep + self.attrs.pop('name')

class IfLTE(IfExpr, Node):
    def process(self):
        lvalue = textToRpyInterp(self.attrs.pop('lvalue'))
        lvalue = re.sub(r"^\[(.+)\]$", r"\g<1>", lvalue)
        rvalue = textToRpyInterp(self.attrs.pop('rvalue'))
        rvalue = re.sub(r"^\[(.+)\]$", r"\g<1>", rvalue)
        self.expr = f"{lvalue} <= {rvalue}"
        self.label = self.getLabel() + pathsep + self.attrs.pop('name')

class IfTrue(IfExpr, Node):
    def process(self):
        value = textToRpyInterp(self.attrs.pop('value'))
        value = re.sub(r"^\[(.+)\]$", r"\g<1>", value)
        self.expr = value
        self.label = self.getLabel() + pathsep + self.attrs.pop('name')

class JumpEvent(Node):
    def process(self):
        self.jumplabel = sceneid + pathsep + slugify(self.attrs.pop('path').replace("/", pathsep))

    def toRpy(self):
        return f"jump {self.jumplabel}"

class LockoutChoice(Node):
    pass

class Macro(NodeContainer, Node):
    def process(self):
        self.name = self.attrs.pop('name')
        self.label = self.getLabel() + pathsep + self.name

class NHSceneChange(Node):
    def process(self):
        self.jumplabel = slugify(self.attrs.pop('scene'))

    def toRpy(self):
        return f"jump {self.jumplabel}"

class NormalEndMacro(Node):
    pass

class ParallelEvent(NodeBody, Node):
    # Or "DiscreteEvent"
    # Seems to just be a bunch of logic for interrupts?
    def process(self):
        if 'name' in self.attrs and not self.attrs['name'].startswith("_"):
            self.label = self.getLabel() + pathsep + self.attrs.pop('name')
        else:
            self.label = None

    def toRpy(self):
        if self.label:
            return NodeBody.toRpy(self)  #  + '\nextend ""'
        else:
            return NodeContainer.toRpy(self)  #  + '\nextend ""'

class Transitions(Node):
    pass

class Styles(Node):
    pass

class SettingChange(Node):
    pass

class SilhouetteMacro(Node):
    def toRpy(self):
        lines = []

        lines.append("# Start SilhouetteMacro")
        # Fade out last actor
        lastActor = self.attrs.pop('lastActor', None)
        fadedur = self.attrs.pop('fadeTime', 0.5)
        if lastActor:
            lines.append(f"show {last_image_for_tag[lastActor]} as {lastActor}:  # SM0")
            lines.append(f"    linear {fadedur} alpha 0.0")

        # Silhouette fade in + first line of text
        silactor_id = self.attrs.pop('silActor')
        silImage = slugify(self.attrs.pop('silImage'))

        # Other character is always opposite cousin. 
        cousinx = self.attrs.pop('cousinX')
        self.attrs['axtorX'] = f"{int(100*(-1 * p2f(cousinx)))}%"

        lines.append(f"show {silImage} as {silactor_id}:  # SM1")
        last_image_for_tag[silactor_id] = silImage


        self.attrs['actorY'] = self.attrs.get("actorY", '0%')

        transforms = []
        transforms.append("    default")
        for macroattr, prop in {
            "actorScaleX": "scaleX",
            "actorScaleY": "scaleY",
            "actorY": "y",
            "axtorX": "x"
        }.items():
            if macroattr in self.attrs:
                transforms.append(f"    {transformation[prop](self.attrs[macroattr], None)}")
                self.attrs.pop(macroattr)

        lines += transforms

        lines.append(f"    alpha 0.0")
        lines.append(f"    linear {fadedur} alpha 1.0")

        char = self.attrs.pop('actorName')
        firstText = self.attrs.pop('firstText')

        secondtext = self.attrs.pop('secondText', None)

        if secondtext:
            lines.append(f'{fixname(char)} "{textToRpyInterp(TextStore[firstText])}"')

        # Cousin move

        scalex = (1.0 if p2f(cousinx) < 0 else -1.0)

        cousin_id = self.attrs.pop('cousinActor')
        lines.append(f"show {last_image_for_tag[cousin_id]} as {cousin_id}:  # SM1.5")
        lines.append("    " + transformation['scaleX'](scalex, cousin_id))
        lines.append("    linear 0.5 " + transformation['x'](cousinx, cousin_id))

        # Silhouette replaced with real + second line of text extend

        realActor = self.attrs.pop('realActor')
        realImage = slugify(self.attrs.pop('realImage'))

        last_image_for_tag[silactor_id] = silImage
        lines.append(f"show {silImage} as {silactor_id}:  # SM2")
        lines.append(f"    linear {fadedur} alpha 0.0")

        lines.append(f"show {realImage} as {realActor} at default:  # SM3")
        lines += transforms
        lines.append(f"    linear {fadedur} alpha 1.0")

        last_image_for_tag[realActor] = realImage

        if secondtext:
            if self.attrs.pop('appendSecond', False):
                lines.append(f'extend " {textToRpyInterp(TextStore[secondtext])}"')
            else:
                lines.append(f'{fixname(actor_id)} "{textToRpyInterp(TextStore[secondtext])}"')
        else:
            lines.append(f'{fixname(char)} "{textToRpyInterp(TextStore[firstText])}"')

        lines.append("# End SilhouetteMacro")
        return "\n".join(lines)

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
        self.text = self.attrs.pop('text', None)
        if self.text:
            self.text = re.sub(r"(\@[^ ]+)", lambda m: TextStore[m.group(1)], self.text)
        self.char = self.attrs.pop('char', None)  # re.sub(r"\@([^ ]+)", lambda m: TextStore[m.group(1)], self.attrs['char'])

        # todo
        # self.transform = self.attrs.pop('transform', None)
        self.extend = toPyValue(self.attrs.pop('append', False))

        # self.letter_class = self.attrs.pop('letterClass', None)
        # self.letter_delay = self.attrs.pop('letterDelay', None)

    def toRpy(self):
        if not self.char or self.text is None:
            return "# Blank text event"
        nw = "" # ""{nw}" if self.attrs.get('auto') else ""
        if self.extend:
            return f'extend " {textToRpyInterp(self.text)}{nw}"'
        else:
            return f'{fixname(self.char)} "{textToRpyInterp(self.text)}{nw}"'


class VarEnsure(Node):
    def process(self):
        self.storeName = self.attrs.pop('storeName')
        self.varName = self.attrs.pop('varName')
        self.value = toPyValue(self.attrs.pop('value'))
        AllStores.add(self.storeName)

    def toRpy(self):
        return f'$ if not {self.storeName}.__dict__.get({self.varName!r}): {getStoreVarName(self.storeName, self.varName)} = {self.value!r}'


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
        lines.append(f'    "{yes_text}":')
        lines.append(f'        $ st_{self.store_name}.{self.var_name} = True')
        lines.append(f'    "{no_text}":')
        lines.append(f'        $ st_{self.store_name}.{self.var_name} = False')
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
