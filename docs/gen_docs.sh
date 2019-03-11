# Make sure you install modules in requirements.txt and Rust (cargo) before you run this
# If you don't install requirements.txt, you'll get errors

rm -rf ../pibakesoftware/html
rm -rf ../uuid/target
cd ../pibakesoftware
pdoc --html connect.py write.py util.py temperature.py
cd ../uuid
cargo doc --no-deps --open