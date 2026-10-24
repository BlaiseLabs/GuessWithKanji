#!/bin/bash
# build/guesswithkanji.ankiaddon: the add-on folder zipped (no caches, no user files)
set -e
cd "$(dirname "$0")/.."
mkdir -p build
rm -f build/guesswithkanji.ankiaddon
(cd guesswithkanji && zip -qr ../build/guesswithkanji.ankiaddon . -x "__pycache__/*" "*/__pycache__/*" "user_files/*" "meta.json")
zip -qj build/guesswithkanji.ankiaddon LICENSE
ls -la build/guesswithkanji.ankiaddon
