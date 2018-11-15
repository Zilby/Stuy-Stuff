all: picmaker.o
	gcc -o picmaker picmaker.o
	make run
picmaker.o: picmaker.c
	gcc -c picmaker.c
clean:
	rm *.o
run:
	./picmaker