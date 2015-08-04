#!/bin/sh
make
ant compile
ant jar
ant clean
chmod +x *.jar
