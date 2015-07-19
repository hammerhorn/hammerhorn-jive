# Builds the 3 separate executables: 'cloop', 'c++loop', 'f90loop'.

all: cloop c++loop f90loop

cloop: cloop.o cjh.o
	gcc -O2 cloop.o cjh.o -o cloop

c++loop: c++loop.o cjh.o
	gcc -O2 c++loop.o cjh.o -o c++loop

f90loop: f90loop.o cjh.o
	gcc -O2 f90loop.o cjh.o -o f90loop

cloop.o: cloop.c 
	gcc -O2 -c cloop.c

c++loop.o: c++loop.c
	gcc -O2 -c c++loop.c

f90loop.o: f90loop.c
	gcc -O2 -c f90loop.c

cjh.o: cjh.c
	gcc -O2 -c cjh.c
