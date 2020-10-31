#!/bin/bash

# Bash "strict mode", to help catch problems and bugs in the shell
# script. Every bash script you write should include this. See
# http://redsymbol.net/articles/unofficial-bash-strict-mode/ for
# details.
set -euo pipefail

rm /etc/apt/sources.list && touch /etc/apt/sources.list

echo "
deb http://deb.debian.org/debian buster main contrib non-free
deb-src http://deb.debian.org/debian buster main contrib non-free

deb http://deb.debian.org/debian-security buster/updates main contrib non-free
deb-src http://deb.debian.org/debian-security buster/updates main contrib non-free
deb http://security.debian.org/ buster/updates contrib non-free main

deb http://deb.debian.org/debian/ buster-updates main contrib non-free
deb-src http://deb.debian.org/debian/ buster-updates main contrib non-free

deb http://ftp.debian.org/debian buster-backports main contrib non-free
deb-src http://ftp.debian.org/debian buster-backports main contrib non-free
    " | tee -a /etc/apt/sources.list

# Tell apt-get we're never going to be able to give manual
# feedback:
export DEBIAN_FRONTEND=noninteractive

# Update the package listing, so we know what package exist:
apt-get update

# Install security updates:
apt-get -y upgrade

# Install a new package, without unnecessary recommended packages:
apt-get -y install --no-install-recommends syslog-ng

# Delete cached files we don't need anymore:
apt-get clean
rm -rf /var/lib/apt/lists/*