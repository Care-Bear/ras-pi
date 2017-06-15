#!/bin/bash

#debug
set -x


# update git repo

cd ~/repo
git pull

cp ~/repo/screen.py ~/screen/screen.py
cp  ~/repo/screen.json ~/screen/screen.json