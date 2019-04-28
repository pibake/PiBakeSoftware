#!/bin/bash
#
# Make sure you install modules in requirements.txt before you run this
# If you don't install requirements.txt, you'll get errors
#
# Also be sure to run this in the parent directory
# Written by Wyatt J. Miller, 2019

sudo apt install -y graphviz
pyreverse -o png pibakesoftware