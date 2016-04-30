#!/bin/bash

###
### set da shizzle up
###

presteps() {

dnf -y install wget
dnf -y install unzip
dnf -y install git
dnf -y install gcc
dnf -y install libffi-devel
dnf -y install redhat-rpm-config
dnf -y install make

dnf -y copr enable -y mstuchli/Python3.5
dnf -y install -y python35-python3
wget https://bootstrap.pypa.io/get-pip.py
/usr/bin/python3.5 get-pip.py

dnf -y install http://download1.rpmfusion.org/free/fedora/rpmfusion-free-release-23.noarch.rpm
dnf -y install ffmpeg
dnf -y install opus-devel

pip3.5 install youtube_dl
pip3.5 install imgurpython
pip3.5 install discord.py
pip3.5 install git+https://github.com/Rapptz/discord.py@async

pip3 install --upgrade git+https://github.com/Rapptz/discord.py@async

}

###
### important shit
###

poststeps() {

cp /root/projects/cogs/milton.service /etc/systemd/system/milton.service
systemctl enable milton.service
systemctl start milton.service

cp /root/projects/cogs/fitz.service /etc/systemd/system/fitz.service
systemctl enable fitz.service
systemctl start fitz.service

systemctl daemon-reload

}

#presteps
poststeps
