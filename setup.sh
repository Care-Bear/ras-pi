#!/usr/bin/env bash

set -eu

# Variables
GECKODRIVER_VERSION="v0.15.0"
GIT_REPO="git@github.com:Care-Bear/ras-pi.git"
REPO_BASE="/opt"
REPO_PATH="$REPO_BASE/ras-pi"
LXDE_PATH="/home/pi/.config/lxsession/LXDE-pi/autostart"
LXDE_ENTRY="@/usr/bin/python /opt/ras-pi/screen.py"

# Install iceweasel
apt-get update
apt-get install iceweasel -y

# Clone ras-pi repo and install Python packages
if [ ! -d $REPO_PATH ]; then
    echo "The 'ras-pi' repo is not present, cloning now to '$REPO_PATH'"
    cd $REPO_BASE
    git clone $GIT_REPO
    pip install -r requirements.txt
fi

# Copy config.yaml from example_config.yaml if not present
if [ ! -f $REPO_PATH/config.yaml ]; then
    echo "'config.yaml' is not present, copying now from 'example_config.yaml'"
    cp $REPO_PATH/example_config.yaml $REPO_PATH/config.yaml
fi

# Download geckodriver binary
if [ ! -f /usr/local/bin/geckodriver ]; then
    echo "The 'geckodriver' binary is not present, downloading"
    wget https://github.com/mozilla/geckodriver/releases/download/$GECKODRIVER_VERSION/geckodriver-$GECKODRIVER_VERSION-arm7hf.tar.gz
    tar -C /usr/local/bin -xvf geckodriver-$GECKODRIVER_VERSION-arm7hf.tar.gz
    rm geckodriver-$GECKODRIVER_VERSION-arm7hf.tar.gz
fi

# Create LXDE autostart entry for running script on start up
if grep -q "$LXDE_ENTRY" $LXDE_PATH; then
   echo "$LXDE_ENTRY" >> $LXDE_PATH
fi

exit 0
