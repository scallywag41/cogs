#!/bin/bash

cat << EOF > /etc/systemd/system/milton.service
[Unit]
Description="Milton Bot Process"
Documentation=http://www.github.com/scallywag41/

[Service]
ExecStart=cd /opt/milton
ExecStart=/opt/milton/milton.bash
Restart=on-failure
RestartSec=10
Type=simple
PIDFile=/var/tmp/milton.pid

[Install]
WantedBy=multi-user.target
EOF 

#systemctl enable milton.service
#systemctl start milton.service

