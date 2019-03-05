rm -rf ../pibakesoftware/html
rm -rf ../uuid/target
cd ../pibakesoftware
pdoc --html connect.py write.py util.py temperature.py
cd ../uuid
cargo doc --no-deps --open