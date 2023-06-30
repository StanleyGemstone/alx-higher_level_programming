#!/usr/bin/bash
vi $1
chmod u+x $@
git add ..
git commit -m "0x11-python-network_1"
git push
clear
echo "$@ has been pushed"
