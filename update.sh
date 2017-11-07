#!/usr/bin/env bash

# Debug
set -x

REPO_BASE=/opt
REPO_PATH=$REPO_BASE/ras-pi

# Update git repo
cd $REPO_PATH
git pull

cp $REPO_PATH/screen.py ~/screen/screen.py
cp $REPO_PATH/config.yaml ~/screen/config.yaml

exit 0
