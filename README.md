# GuessWithKanji

**Japanese vocabulary ordered so you can guess the meaning and reading of each word from kanji you've already met.**

![How GuessWithKanji works. A word arrives right after its kanji, so you can guess it](docs/explainer.gif)

An Anki add-on that orders a Japanese deck's new cards so that each word arrives **guessable**. Its kanji, read the way
they are read in that word, came up in cards you just studied, and its meaning follows from what those kanji mean. You
stop memorizing a share of your words and start guessing them right on first sight.

```
電車 でんしゃ  train      (studied)
天気 てんき    weather    (studied)
電気 でんき    ?          電 read でん, met 2 cards ago, and 気 read き, met 1 card ago
                          electric + spirit -> electricity, so it's guessable and comes next
```

**No extra software needed.** Install the add-on and it works on its own. [Ollama](https://ollama.com) is an optional
upgrade for sharper meaning judgments and model labels (see [Install](#install)).

## How much faster

A card you guess right the first time you see it is a free card, because you never have to learn it. The table counts
only the cards you have to learn, and asks how many it takes to reach a number of words, in the deck's own order
(normal Anki) and in GuessWithKanji's order. The speed-up is normal Anki's cards divided by GuessWithKanji's, so 75%
fewer cards is 4× faster, since each card you learn gets you four words instead of one. The guess rate is how often you
get a guessable word right once its kanji readings are learned.

The table shows the speed-up and the cards learned (normal Anki → GuessWithKanji), with Anki's default FSRS at 90%
retention and a kanji reading learned after one sighting.

| Deck | Guess rate | 100 words | 500 words | 1,000 words | 2,000 words |
|---|---|---|---|---|---|
| JLPT N5–N1 vocabulary (7,727 words) | 100% | **6.2×** (100 → 16) | **4.6×** (470 → 102) | **4.1×** (903 → 221) | **3.2×** (1,610 → 511) |
|  | 80% | **2.9×** (100 → 35) | **2.6×** (478 → 185) | **2.4×** (926 → 385) | **2.1×** (1,691 → 816) |
|  | 50% | **1.8×** (100 → 56) | **1.6×** (484 → 302) | **1.6×** (951 → 609) | **1.4×** (1,807 → 1,247) |
|  | 33% | **1.4×** (100 → 70) | **1.3×** (492 → 365) | **1.3×** (971 → 741) | **1.2×** (1,873 → 1,508) |
|  | 25% | **1.3×** (100 → 78) | **1.2×** (492 → 399) | **1.2×** (974 → 801) | **1.2×** (1,890 → 1,620) |
| Core 6k Optimized (5,999) | 100% | **5.4×** (98 → 18) | **4.1×** (450 → 110) | **3.8×** (859 → 225) | **2.8×** (1,560 → 560) |
|  | 80% | **2.7×** (98 → 36) | **2.4×** (460 → 188) | **2.3×** (884 → 383) | **1.9×** (1,643 → 852) |
|  | 50% | **1.7×** (99 → 58) | **1.5×** (475 → 308) | **1.5×** (926 → 606) | **1.4×** (1,777 → 1,278) |
|  | 33% | **1.4×** (99 → 72) | **1.3×** (484 → 370) | **1.3×** (954 → 742) | **1.2×** (1,861 → 1,520) |
|  | 25% | **1.3×** (99 → 75) | **1.2×** (490 → 398) | **1.2×** (966 → 802) | **1.1×** (1,886 → 1,641) |
| Core 2k (2,000) | 100% | **3.7×** (99 → 27) | **2.4×** (472 → 199) | **1.6×** (867 → 530) | **1.0×** (1,575 → 1,517) |
|  | 80% | **2.3×** (100 → 44) | **1.8×** (480 → 264) | **1.4×** (900 → 628) | **1.0×** (1,672 → 1,617) |
|  | 50% | **1.7×** (100 → 60) | **1.4×** (488 → 342) | **1.2×** (939 → 756) | **1.0×** (1,793 → 1,751) |
|  | 33% | **1.3×** (100 → 76) | **1.2×** (492 → 403) | **1.1×** (961 → 847) | **1.0×** (1,866 → 1,842) |
|  | 25% | **1.3×** (100 → 79) | **1.2×** (493 → 425) | **1.1×** (967 → 874) | **1.0×** (1,893 → 1,870) |
| Kaishi 1.5k (1,500) | 100% | **3.5×** (97 → 28) | **2.2×** (456 → 209) | **1.3×** (870 → 694) | – |
|  | 80% | **2.4×** (98 → 41) | **1.8×** (466 → 265) | **1.2×** (898 → 751) | – |
|  | 50% | **1.6×** (98 → 60) | **1.4×** (481 → 350) | **1.1×** (940 → 841) | – |
|  | 33% | **1.3×** (99 → 76) | **1.2×** (486 → 402) | **1.1×** (956 → 898) | – |
|  | 25% | **1.2×** (99 → 81) | **1.1×** (492 → 433) | **1.0×** (970 → 929) | – |
| Tango N5, AnkiWeb (1,160) | 100% | **2.4×** (96 → 40) | **1.3×** (475 → 354) | **1.1×** (906 → 845) | – |
|  | 80% | **1.9×** (97 → 50) | **1.3×** (479 → 382) | **1.1×** (922 → 873) | – |
|  | 50% | **1.4×** (98 → 70) | **1.1×** (489 → 431) | **1.0×** (951 → 927) | – |
|  | 33% | **1.2×** (99 → 81) | **1.1×** (494 → 454) | **1.0×** (971 → 950) | – |
|  | 25% | **1.2×** (99 → 86) | **1.1×** (495 → 465) | **1.0×** (973 → 963) | – |

#### What this shows

- **Big decks keep the lead.** JLPT and Core 6k reach 2,000 words with about half the cards learned at an 80% guess
  rate, because their kanji repeat across thousands of words.
- **Small decks front-load it.** Kaishi, Core 2k and Tango save the most in their first few hundred words. By the time
  most of the deck is started, both orders have had the same chances to guess.
- **Even a poor guesser gains.** At a 25% guess rate the first 500 words still take 6–19% fewer cards.
- **Reviews come on top.** Free cards still come back for review. In the same simulation run for a year, the big decks
  need 30% fewer card showings by 1,000 words started and 14–20% fewer by 4,000–6,000 (the saving comes early), and
  forgotten reviews fall by about 70%.

#### How it was measured

Each deck was imported fresh (no prior knowledge), with guessability from the built-in heuristics alone (reading
frequency plus EmbeddingGemma meaning similarity). Then a learner was simulated day by day for 100 days at 20 new cards
a day under FSRS-6 (the same formulas as py-fsrs, checked to 15 decimal places), every review done, 4 simulated
learners averaged. Every day a word is shown counts as a sighting of its kanji readings, and each reading has an FSRS
memory of its own. GuessWithKanji's order was planned once at the start (the add-on plans again after every session).
The decks are not part of this repository. Kaishi 1.5k comes from its GitHub release and the others from AnkiWeb. The
tools are `tools/import_deck.py`, `tools/fsrs_sim.py` and `tools/free_cards.py`.

## What it does

- **Reads your deck.** Any note type with a word field works. Fields are found by name and by what they hold (a short
  Japanese word, kana for the reading, English for the meaning), so `Vocabulary-Kanji`, `Word Reading` or a word
  written with furigana (`漢字[かんじ]`) all work, and a reading field that holds a sentence is ignored. Your study
  history says which kanji readings you have met and when.
- **Splits each word into patterns,** a kanji plus the reading it has in that word (だん in both 相談 and 面談), with
  the regular sound changes (rendaku, small tsu). The split matches JmdictFurigana for 99.0% of 17,854 common words.
- **Judges guessability** from several sources, weighted when they disagree.
  - **Heuristic** (code, tunable). How common the word's reading of each kanji is (in the dictionary, your deck, or
    both), and how close the word's meaning is to its kanji's meanings (embedding cosine with EmbeddingGemma, or plain
    word overlap when no embedding model is running). Tuned on 2,038 labelled words, it scores an AUC of 0.83 for
    meaning with EmbeddingGemma (0.73 with word overlap) and 0.83 for reading.
  - **Model labels.** Any model behind an OpenAI-style API (Gemma 4 through Ollama by default) labels words in
    batches, a daily cap at a time (100 a day by default), resumable, with a JSON schema that names the batch's words.
    Gemma 4 12B agreed with a larger cloud model's labels on 86% of readings and 79% of meanings over 1,839 words.
  - **Crowd and deck labels.** You (or a group) label words while reviewing (Shift+G or right-click), share labels as
    a file, or ship them inside a deck you publish.
- **Plans the path.** A greedy order over your new cards makes as many words as possible guessable on arrival. When
  nothing is guessable yet it brings in an opener, one new kanji reading at a time and a plain word first (見る before
  見っともない, 取る and 戻る before 取り戻す). It writes the order into Anki's new-card queue and plans again after
  each review session.
- **Options.** `deck_every` keeps part of a deck's own order (every n-th card), `need` asks for several sightings
  before a kanji reading counts, and pattern spacing brings a learned reading back at growing gaps.
- **Dashboard.** It shows your free cards (cards studied, how many arrived guessable, words you could guess now), words
  guessable on arrival (deck order vs path), the next cards and why, your patterns, and words whose kanji have another
  common reading (could be confused).
- **Sentry tracing** (optional). Each labelling job is one trace in Sentry's AI agent format, a transaction per batch
  with its tokens, timing and unreadable words, plus a span per embedding call.

## Install

**No extra software needed.** Install the `.ankiaddon` from the
[releases](https://github.com/BlaiseLabs/GuessWithKanji/releases) (double-click it, or in Anki use Tools > Add-ons >
Install from file), or copy the `guesswithkanji` folder into Anki's add-ons folder (Tools > Add-ons > View Files), then
restart Anki. Tools > GuessWithKanji > Dashboard plans for the first time.

Your deck options must let positions decide, so set the new card gather order to "Deck" or "Ascending position" and
the sort order to "Order gathered" or "Card type, then order gathered". The dashboard warns when they don't.

#### Optional, a local model for sharper judgments

Without a model, meanings are judged by word overlap and everything works. A local model adds two things, sharper
meaning judgments (embeddings) and "Label with model", where a model judges each word. The easiest way is
[Ollama](https://ollama.com), which is free and runs on your own computer. Install it, then pull the two models.

```
ollama pull embeddinggemma        # meaning similarity (300M, runs anywhere)
ollama pull gemma4:12b-it-qat     # the labelling model (or any model, set it in the settings)
```

Ollama isn't required for this. Both settings accept any server with an OpenAI-style API, so LM Studio, llama.cpp's
server, vLLM, or a cloud API such as OpenAI's (with an API key) work too. Set `embeddings` and `llm` (address, model,
key) in the settings. Thinking models answer with `reasoning_effort` set to `"none"` by default, and batches of 20
words fit Ollama's default 4,096-token context.

## Settings

Tools > GuessWithKanji > Settings (see `guesswithkanji/config.md`). The ones that matter most are `search` (which
notes), `path.window` (how many cards back a kanji still counts as fresh), `guessable` (the levels a word needs),
`sources` (how much crowd, model and heuristic labels weigh), `llm.per_day`, `free` (how the dashboard counts free
cards) and `sentry_dsn`.

## Sharing labels

Labels are keyed by word and reading, so they work with any copy of a deck, and across decks that share words.

- **In a deck you publish.** Tools > GuessWithKanji > Write labels into the deck puts your votes (and the model's labels)
  into the notes as tags, `guesswithkanji::reading::yes` and `guesswithkanji::meaning::partly`, and into `_guesswithkanji.json` in
  the deck's media (Anki keeps media files starting with `_` and exports them with the deck). Share the deck on
  AnkiWeb as usual, and anyone who installs it and GuessWithKanji gets the labels, counted as the source `deck`.
- **As a file.** Tools > GuessWithKanji > Export labels writes `{"schema": "guesswithkanji-labels/1", "labels": [...]}`,
  and Import merges a file someone else exported (records already present are skipped). Several people's votes on the
  same word are averaged, one vote per person. Here's one record.

```json
{"word": "入口", "reading": "いりぐち", "reading_guessable": "yes", "meaning_guessable": "yes",
 "why_meaning": "enter + mouth", "helpers": ["入る", "出口"], "source": "crowd", "by": "a name"}
```

To go by people's votes only, set `"sources": {"crowd": 1, "deck": 1, "llm": 0, "heuristic": 0}`. There is no
central place to pool votes yet, so share files, or ask a deck's author to write them into the deck.

## Without Anki open

```
python tools/cli.py reorder collection.anki2      # close Anki first, or work on a copy
python tools/cli.py label collection.anki2 --n 100
python tools/import_deck.py deck.apkg out.anki2    # a shared deck into a collection of its own, fields shown
python tools/deck_report.py out.anki2 --files dir # what the path changes for a new learner
python tools/fsrs_sim.py out.anki2 --files dir --out sim.json   # the simulation behind the table above
python tools/fsrs_sim.py out.anki2 --files dir --out sim.json --params my_fsrs.json --retention 0.85   # with your FSRS
```

## Development

```
pip install aqt pytest
bash tools/fetch_raw.sh             # KANJIDIC2, JMdict, JmdictFurigana into raw/ (EDRDG and Doublevil downloads)
python tools/build_data.py          # rebuilds guesswithkanji/data/ and tools/common_words.json
python tools/make_demo.py demo.anki2 --n 2000 --study 150   # a demo deck from JMdict's common words
python -m pytest -q                 # core + a real Anki collection
GP_DEMO=demo.anki2 bash e2e/run.sh  # a real Anki under Xvfb, driven like a learner (menu, keyboard, dialogs)
bash tools/package.sh               # build/guesswithkanji.ankiaddon
manim -qh docs/video/explainer.py Explainer   # the explainer video (Manim Community 0.19)
```

## Data and credits

- KANJIDIC2 and JMdict, by the Electronic Dictionary Research and Development Group (EDRDG), CC BY-SA 4.0, for kanji
  meanings and readings, the dictionary reading counts and the demo deck. JmdictFurigana (Doublevil, CC BY-SA 4.0)
  for checking the reading splitter. The derived files in `guesswithkanji/data/` are shared under CC BY-SA 4.0.
- FSRS, by the open-spaced-repetition project. `tools/fsrs_sim.py` reimplements the FSRS-6 formulas of py-fsrs.
- Gemma and EmbeddingGemma (Google) through Ollama for the model labels and meaning similarity.

## Licence

The code is MIT (see `LICENSE`). The data in `guesswithkanji/data/` is CC BY-SA 4.0 (see `guesswithkanji/data/SOURCES.md`).
