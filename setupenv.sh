#!/usr/bin/env bash

V_ENV=".venv"   # directory to put the virtual env in

# Create the virtual env and point pip at our private PyPi in Artifactory
#
python3.6 -m venv ${V_ENV}
cat <<EOF > ${V_ENV}/pip.conf
[global]
index-url = https://artifactory-fpark1.ext.net.nokia.com/artifactory/api/pypi/NFVFP-pypi-local/simple
trusted-host = artifactory-fpark1.ext.net.nokia.com
disable-pip-version-check = true

EOF

source ${V_ENV}/bin/activate
pip3 install --upgrade pip setuptools wheel twine
deactivate

# Create shortcuts to make activating easier
echo "source ${V_ENV}/bin/activate" > activate-3
chmod +x activate-3
