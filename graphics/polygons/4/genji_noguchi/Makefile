all: main.o graphics.o raster.o matrix.o mesh.o vect4.o loader.o
	g++ main.o graphics.o raster.o matrix.o mesh.o vect4.o loader.o

main.o: main.cpp
	g++ -c main.cpp

graphics.o: graphics.cpp graphics.h
	g++ -c graphics.cpp

raster.o: raster.cpp raster.h
	g++ -c raster.cpp

mesh.o: mesh.cpp mesh.h
	g++ -c mesh.cpp

matrix.o: matrix.cpp matrix.h
	g++ -c matrix.cpp

vect4.o: vect4.cpp vect4.h
	g++ -c vect4.cpp

loader.o: loader.cpp loader.h
	g++ -c loader.cpp



display:
	display out.ppm

clean:
	rm *.o
	rm a.out
	rm *.ppm
