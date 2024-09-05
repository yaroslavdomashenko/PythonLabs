from enum import Enum

class LangSet(Enum):
    lang = 1
    confidence = 2
    all = 3

class OutResult(Enum):
    screen = 1
    file = 2
