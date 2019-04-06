# Make sure you install modules in requirements.txt and Rust (cargo) before you run this
# If you don't install requirements.txt, you'll get errors

rm -rf pibakesoftware/html
rm -rf uuid/target
pydoc -w pibakesoftware
pydoc -w pibakesoftware.__main__
pydoc -w pibakesoftware.connect
pydoc -w pibakesoftware.read
pydoc -w pibakesoftware.temperature
pydoc -w pibakesoftware.write
pydoc -w pibakesoftware.util
cd uuid
cargo doc --no-deps