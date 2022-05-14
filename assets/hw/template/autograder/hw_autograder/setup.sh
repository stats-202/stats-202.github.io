#!/usr/bin/env bash

apt-get update
apt-get install -y python3.6 python3-pip python3-dev r-base
pip3 install -r /autograder/source/tests-python/requirements.txt
while read -r package;
do
  Rscript -e "install.packages('"$package"', repos='"https://ftp.osuosl.org/pub/cran/"')";
done < "/autograder/source/tests-R/requirements.txt"