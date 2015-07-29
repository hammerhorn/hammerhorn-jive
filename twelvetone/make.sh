#!/bin/sh
gcc -o tonerow -O3 src/tonerow.c

strip -s tonerow

cd src

javac listfreqs.java

jar cvmf MANIFEST.MF listfreqs.jar listfreqs.class Angle.class displacement.class Keyboard.class MyMath.class Note.class Wave.class Thing.class Scalar.class Unit.class MyVector.class Velocity.class TuiTeX.class



mv *.jar ..

cd -

chmod +x listfreqs.jar *.pl *.py *.sh
rm -f src/*.class

./prefs.py -s bash
