all: mixtool mixtool++ mixtool_f90

mixtool: src/mixtool.c
	gcc -O2 -o mixtool src/mixtool.c
	strip -s mixtool

mixtool++: src/mixtool.cpp
	g++ -O2 -o mixtool++ src/mixtool.cpp
	strip -s mixtool++

mixtool_f90: src/mixtool.f90
	gfortran -O2 -o mixtool_f90 src/mixtool.f90
	strip -s mixtool_f90
