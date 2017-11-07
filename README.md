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


## Config

In order to run the script, make a copy of `example_config.yaml`:

```
cp example_config.yaml config.yaml
```

Edit `config.yaml` to include or exclude the webpages or local files you want, as well as changing the sleep time between page changes.

### auth_links

While it's a little fiddly as most login forms wildy differ, you can use this script to login to dashbaords that require credentials.

To use the `auth_links` feature, you will need to inspect the login form using your web browser (right click and choose inspect), and find the type and name of the element for both the username and password field. Once you have found these, put them the copied `config.yaml`. See the `example_config.yaml` for an example of how to do this.


## Usage

To run the script, ensure `screen.py` and `config.yaml` are in the same directory:

```
python screen.py
```

If any changes are to be made, you just need to amend the yaml file and then restart the script.


## Getting Started

If you're looking to deploy and run this script quickly, you can use the `setup.sh` script which will:

- Install Iceweasel
- Clone the repo
- install the Python packages
- Download and move the geckodriver binary to `/usr/local/bin`
- Create LXDE autostart entry to run the script on start up

```
sudo ./setup.sh
```

the only thing you'll need to do it edit `config.yaml` to include whatever you want to display.
