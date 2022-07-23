#!/bin/bash
DISPLAY=:0
cd ~/programs/misc/mediumstats/
poetry run python3 getstats.py
