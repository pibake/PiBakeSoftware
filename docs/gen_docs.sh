#!/bin/bash
#
# Make sure you install modules in requirements.txt and Rust (cargo) before you run this
# If you don't install requirements.txt, you'll get errors
#
# Written by Wyatt J. Miller, 2019

rm -rf pibakesoftware/html
rm -rf uuid/target
pydoc -w pibakesoftware
pydoc -w pibakesoftware.__main__
pydoc -w pibakesoftware.connect
pydoc -w pibakesoftware.read
pydoc -w pibakesoftware.temperature
pydoc -w pibakesoftware.write
pydoc -w pibakesoftware.util
pydoc -w pibakesoftware.uuid_gen
cd uuid
cargo doc --no-deps