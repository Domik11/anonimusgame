#!/usr/bin/env bash
apt upgrade
apt update
pkg install python
pkg install python2
pip install pip
pip install colorama
python -m pip install -U requests
clear
python game.py
