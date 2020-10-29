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

class TextAsset(Node):
    pass

class TextEvent(Node):
    pass

class VarEnsure(Node):
    pass

class VarInc(Node):
    pass

class VarSet(Node):
    pass

class YesNoChoice(Node):
    pass

class Assets(Node):
    pass

class Scene(Node):
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
    "events",
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
