"""A shared deck (.apkg) into a fresh collection of its own, with no study history, and a look at its note types:
the fields GuessWithKanji would pick, and a sample note.

    python3 tools/import_deck.py DECK.apkg OUT.anki2 [--show 2]"""
import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from guesswithkanji.core.ankiio import detect_fields, word_reading  # noqa: E402
from guesswithkanji.core.kana import clean  # noqa: E402


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("apkg")
    ap.add_argument("out")
    ap.add_argument("--show", type=int, default=2)
    a = ap.parse_args()
    from anki.collection import Collection
    from anki.import_export_pb2 import ImportAnkiPackageOptions, ImportAnkiPackageRequest
    Path(a.out).unlink(missing_ok=True)
    col = Collection(a.out)
    col.import_anki_package(ImportAnkiPackageRequest(package_path=str(Path(a.apkg).resolve()),
                                                     options=ImportAnkiPackageOptions(with_scheduling=False)))
    print("%s: %d notes, %d cards" % (a.out, col.note_count(), col.card_count()))
    for nt in col.models.all():
        n = col.db.scalar("select count() from notes where mid = ?", nt["id"])
        if not n:
            continue
        names = [f["name"] for f in nt["flds"]]
        r = detect_fields(names)
        print("\nnote type %r: %d notes, %d card types" % (nt["name"], n, len(nt["tmpls"])))
        print("  fields:", names)
        print("  GuessWithKanji picks:", r)
        for nid in col.db.list("select id from notes where mid = ? order by id limit ?", nt["id"], a.show):
            note = col.get_note(nid)
            vals = {k: clean(v)[:60] for k, v in note.items()}
            print("  sample:", vals)
            if "word" in r:
                print("    -> word/reading:", word_reading(note[r["word"]], note[r["reading"]] if "reading" in r else ""))
    col.close()


if __name__ == "__main__":
    main()
