all: addup addup++ addup_f90

addup: src/addup.c
	gcc -O2 src/addup.c -o addup
	strip -s addup

addup++: src/addup.cpp
	g++ -O2 src/addup.cpp -o addup++
	strip -s addup++

addup_f90: src/addup.f90
	gfortran -O2 src/addup.f90 -o addup_f90
	strip -s addup_f90
