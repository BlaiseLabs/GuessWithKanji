"""A deck's words as the planner sees them, and the guessability each one ends up with."""
from dataclasses import dataclass, field

from .align import split
from .kana import has_kanji
from .labels import combine, key


@dataclass
class Item:
    nid: int
    word: str
    reading: str
    meaning: str = ""
    cids: list = field(default_factory=list)
    new: bool = True              # no card of the note has been studied
    first: float = 0.0            # when the note was first studied (revlog ms), 0 for new notes
    mature: bool = False          # a card of the note has an interval of mature_days or more
    pos: int = 0                  # the note's place in the new queue (its lowest card due), for new notes
    split: list = None
    has_kanji: bool = False
    key: str = ""
    reading_g: float = None       # combined levels, 0..1 (None: nothing judged it)
    meaning_g: float = None
    sources: dict = None

    def __post_init__(self):
        self.has_kanji = has_kanji(self.word)
        self.split = split(self.word, self.reading) if self.has_kanji and self.reading else None
        self.key = key(self.word, self.reading)

    @property
    def pieces(self):
        return ["%s:%s" % p for p in self.split or []]


def judge(items, store, heur, cfg, deck=None):
    """fill each item's reading_g / meaning_g from the stored labels, the labels the deck carries and the heuristic's
    levels"""
    weights = cfg.get("sources", {"crowd": 3, "deck": 3, "llm": 2, "heuristic": 1})
    latest = store.latest() if store else {}
    for it in items:
        per = dict(latest.get(it.key, {}))
        if deck and it.key in deck:
            per["deck"] = deck[it.key]
        if it.key in heur:
            r, m = heur[it.key]
            per["heuristic"] = [{"reading_guessable": r, "meaning_guessable": m}]
        it.reading_g, it.meaning_g, it.sources = combine(per, weights)


def guessable(it, cfg):
    """judged guessable in both reading and meaning (the words the path tries to make free)"""
    t = cfg.get("guessable", {})
    return bool(it.split) and (it.reading_g or 0) >= t.get("reading", 0.6) and (it.meaning_g or 0) >= t.get("meaning", 0.6)
