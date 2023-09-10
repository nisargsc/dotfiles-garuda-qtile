#!/bin/bash

# This script requires the colorpicker package
echo -n "primary_color = \"$(colorpicker -o -q -d)\"" >> $HOME/.config/qtile/theme.py

