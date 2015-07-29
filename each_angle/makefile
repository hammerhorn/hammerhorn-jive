all: each_angle each_angle++ each_angle_f90

each_angle: each_angle.c
	gcc -O2 each_angle.c -o each_angle
	strip -s each_angle

each_angle++: each_angle.cpp
	g++ each_angle.cpp -o each_angle++
	strip -s each_angle

each_angle_f90: each_angle.f90
	gfortran each_angle.f90 -o each_angle_f90
	strip -s each_angle_f90
