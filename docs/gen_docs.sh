# Make sure you install modules in requirements.txt and Rust (cargo) before you run this
# If you don't install requirements.txt, you'll get errors

rm -rf pibakesoftware/html
rm -rf uuid/target
pdoc --html --overwrite pibakesoftware/__init__.py
#pdoc --html --overwrite pibakesoftware/__main__.py
pdoc --html --overwrite pibakesoftware/connect.py
#pdoc --html --overwrite pibakesoftware/read.py
pdoc --html --overwrite pibakesoftware/temperature.py
pdoc --html --overwrite pibakesoftware/write.py
pdoc --html --overwrite pibakesoftware/util.py
cd uuid
cargo doc --no-deps