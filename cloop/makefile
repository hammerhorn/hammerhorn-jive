all: cloop c++loop f90loop
	rm -f *.o

cloop: cloop.o cjh.o
	gcc -O2 cloop.o cjh.o -o cloop
	strip -s cloop

c++loop: c++loop.o cjh.o
	gcc -O2 c++loop.o cjh.o -o c++loop
	strip -s c++loop

f90loop: f90loop.o cjh.o
	gcc -O2 f90loop.o cjh.o -o f90loop
	strip -s f90loop

cloop.o: src/cloop.c
	gcc -O2 -c src/cloop.c -o cloop.o

c++loop.o: src/c++loop.c
	gcc -O2 -c src/c++loop.c -o c++loop.o

f90loop.o: src/f90loop.c
	gcc -O2 -c src/f90loop.c -o f90loop.o

cjh.o: src/cjh.c
	gcc -c src/cjh.c -o cjh.o
