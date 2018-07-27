#!/bin/bash

docker build -t frankjoshua/idego .
docker run --rm --privileged -v /run/dbus:/run/dbus -v /run/systemd:/run/systemd -v /sbin/shutdown:/sbin/shutdown -p 5000:5000 --name idego frankjoshua/idego