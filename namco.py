import re
import textwrap
import collections
import nc_hardcoded
from bs4 import NavigableString

TextStore = nc_hardcoded.TextStore.copy()
ActorPrevStore = collections.defaultdict(default=None)
JumpLabelStore = []

# Abstract tree handlers

class Node():
    def __init__(self, tag_name, attrs={}, children=[], text=""):
        super().__init__()
        self.__dict__.update(attrs)  # helper
        self.attrs = self.__dict__

        self.kind = tag_name
        self.attrs = attrs
        self.children = children
        self.text = text
        self.preprocess()

    def preprocess(self):
        pass

    @classmethod
    def fromTag(cls, tag):
        node_cls = NODE_TYPES.get(tag.name, cls)
        children = []
        text = ""
        for child in tag.contents:
            if isinstance(child, NavigableString):
                text += str(child).strip()
            elif child.name in PROPERTY_NODES:
                assert child.name not in tag.attrs
                tag.attrs[child.name] = child.value
            else:
                children.append(Node.fromTag(child))
        try:
            return node_cls(tag.name, tag.attrs, children, text)
        except:
            print(node_cls)
            raise

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
        
class NoScript(Node):
    def toRpy(self):
        print(self.__class__.__name__, "Noscript")
        return f"# Pass ({self.kind})\n"

class NodeContainer(Node):
    def toRpy(self, label):
        return label + "\n" + textwrap.indent(NodeBody.toRpy(self), "    ")

class NodeBody(Node):
    def toRpy(self):
        return f"# <{self.__class__.__name__} {self.attrs} {self.kind} '{self.text}'>\n" + "\n".join([s for s in [c.toRpy() for c in self.children] if s])
        
# Actual stuff

class Scene(NodeContainer, Node):
    def preprocess(self):
        self.id = self.attrs["id"].replace('.', '_')
        global sceneid
        sceneid = self.id

    def toRpy(self):
        new_sublabel = self.id.replace('.', '_')
        return NodeContainer.toRpy(self, f"label {new_sublabel}:")
        
class Assets(NoScript, Node):
    pass  # Assets are handled when parsed

class Events(NodeBody, Node):
    pass  # Events is a plain container, doesn't have attrs.
    # TODO: Events can have strings in it?

class ActorCreate(Node):
    pass

class ActorCrossfade(Node):
    pass

class ActorDepth(Node):
    pass

class ActorDestroy(Node):
    pass

class ActorEvent(Node):
    pass

class ActorFade(Node):
    pass

class ActorFlip(Node):
    pass

class ActorImage(Node):
    pass

class ActorMove(Node):
    pass

class ActorReset(Node):
    pass

class ActorScale(Node):
    pass

class ActorTransform(Node):
    pass

class AudioCreate(Node):
    pass

class AudioDestroy(Node):
    pass

class AudioEvent(Node):
    pass

class AudioOneShot(Node):
    pass

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

class ExplorationMacro(Node):
    pass

class FadeEvent(Node):
    pass

class GameOver(Node):
    pass

class HardSwap(Node):
    pass

class IfEqual(Node):
    pass

class IfFalse(Node):
    pass

class IfGTE(Node):
    pass

class IfLTE(Node):
    pass

class IfTrue(Node):
    pass

class JumpEvent(Node):
    pass

class LockoutChoice(Node):
    pass

class Macro(Node):
    pass

class NHSceneChange(Node):
    pass

class NormalEndMacro(Node):
    pass

class ParallelEvent(Node):
    pass

class SettingChange(Node):
    pass

class SilhouetteMacro(Node):
    pass

class SuperSecretMacro(Node):
    pass

class TextAsset(NoScript, Node):
    def preprocess(self):
        value_txt = None
        for value in self.children:
            if value.attrs['key'] == "en":
                value_txt = value.text
        assert value_txt is not None, self
        TextStore[self.key] = value_txt

class TextEvent(Node):
    def preprocess(self):
        self.text = re.sub(r"\@([^ ]+)", lambda m: TextStore[m.group(1)], self.attrs['text'])
        self.char = self.attrs['char']  # re.sub(r"\@([^ ]+)", lambda m: TextStore[m.group(1)], self.attrs['char'])

    def toRpy(self, sublabel):
        if not self.char:
            return "# Blank text event"
        return f'{fixname(self.char)} "{textToRpyInterp(self.text)}"'

class VarEnsure(Node):
    pass

class VarInc(Node):
    pass

class VarSet(Node):
    pass

class YesNoChoice(Node):
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
}
PROPERTY_NODES = [
    "depth",
    "id",
    "image",
    "opacity",
    "scaleX",
    "scaleY",
    "styles",
    "transitions",
    "x",
    "y",
]
