#!/bin/bash

sudo apt -y update && sudo apt -y upgrade 

sudo apt install python3 python3-pip

pip3 install flask RPi.GPIO