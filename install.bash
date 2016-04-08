#!/bin/bash

###
### set da shizzle up
###

cp /opt/projects/milton.service /etc/systemd/system/milton.service
#systemctl enable milton.service
#systemctl start milton.service

cp /opt/projects/fitz.service /etc/systemd/system/fitz.service
#systemctl enable fitz.service
#systemctl start fitz.service

systemctl daemon-reload
