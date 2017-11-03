# pi-screen

Brings up a web browser and cycles through a list of webpages on a Raspberry Pi.


## Requirements

### Python

The script is currently working with Python 2.7 and requires all the packages in `requirements.txt`.

```
pip install -r requirements.txt
```

### Iceweasel & Geckodriver

The script makes use of [Iceweasel](https://wiki.debian.org/Iceweasel) as Chrome doesn't supported ARM architecture, therefore we need Firefox's webdriver e.g. [geckodriver](https://github.com/mozilla/geckodriver/releases).

```
apt-get update && apt-get install iceweasel -y

wget https://github.com/mozilla/geckodriver/releases/download/v0.15.0/geckodriver-v0.15.0-arm7hf.tar.gz

tar -C /usr/local/bin -xvf geckodriver-v0.15.0-arm7hf.tar.gz
```

Due to the current version of iceweasel being `0.45`, the latest version of geckodriver does not support it so we install version `0.15.0`.


## Usage

In order to run the script you need to copy the `example_config.yaml`:

```
cp example_config.yaml config.yaml
```

You can then edit `config.yaml` to include or exclude the webpages or local files you want, as well as changing the sleep time between page changes.


To then run the script, ensure `screen.py` and `config.yaml` are in the same directory:

```
python screen.py
```

If any changes are to be made, you just need to amend the yaml file and then restart the script.
