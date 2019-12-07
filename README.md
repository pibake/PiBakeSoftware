# PiBakeSoftware [![Build Status](https://travis-ci.com/pibake/PiBakeSoftware.svg?branch=master)](https://travis-ci.com/pibake/PiBakeSoftware)

The temperature sensing module software. We like to call it "the software." Don't let developers or engineers name projects. You get a lame project name like this one. 

"The software" is supposed to get the temperature for the temperature sensor (DS18B20) which is attached to a Raspbery Pi 3, grab some other data, store that into a JSON file, and make a request to our server. "The software" does this every minute.

We also have a utility wriiten in Rust that supposed to generate a UUID and store said UUID into a file. Since we couldn't get the UUID out of said file, we made another UUID generator in Python, pushing the Rust UUID generator into deprecation. In the future, I'd like to play with `pyo3` which are Rust Python bindings. We were on a time crunch so playing with items like that didn't have precedence over "the software."

## Installtion

If you don't have a Raspberry Pi 3, please purchase one (an emualtor might be in the works).
If you don't have Python and Rust installed, please install both.
If you don't have [git](https://git-scm.com/), please install it.

Clone the repo and navigate to the root directory of the project:

`git clone https://github.com/pibake/PiBakeSoftware ; cd PiBakeSoftware`

Currently, we are using pip to install the dependencies for the project. To install the denpendencies:

`pip3 install -r requirements.txt`

## Running

`python3 -m pibakesoftware`

## Troubleshooting

"The software" will fail on its own on purpose. Don't have the DS18B20? Get one and connect it to the Raspberry Pi. Don't have an internet connection? Call an ISP. We did our best on error handling. If you find yourself stuck, run `echo $?` and you'll get a return code. File an issue in GitHub and we'll happily assist you on your troubles.

## Contributing

A contributing file is on it's way.
