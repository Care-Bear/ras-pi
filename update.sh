#!/usr/bin/env bash

# Debug
set -x

REPO_BASE=/opt
REPO_PATH=$REPO_BASE/ras-pi

SCREEN_PATH=/opt/screen

# Update git repo
cd $REPO_PATH
git pull

cp $REPO_PATH/screen.py $SCREEN_PATH/screen.py
cp $REPO_PATH/config.yaml $SCREEN_PATH/config.yaml

exit 0
