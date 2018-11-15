OBJECTS= main.o graphics_utils.o draw.o display.o matrix.o utils.o
DEBUG= -DDEBUG -g
WARNINGS_QUIET= -Wall -Wno-unused-variable -Wno-unused-function
WARNINGS_ALL= -Wall -Wpadded 
CFLAGS=$(WARNINGS_QUIET)

CC= gcc

all: build clean

build: $(OBJECTS)
	$(CC) $(DEBUG) -o main $(OBJECTS)

main.o: main.c main.h graphics_utils.h display.h draw.h matrix.h
	$(CC) -c main.c

draw.o: draw.c draw.h graphics_utils.h display.h matrix.h utils.h
	$(CC) $(DEBUG) $(CFLAGS) -c draw.c

display.o: display.c display.h graphics_utils.h utils.h
	$(CC) $(DEBUG) $(CFLAGS) -c display.c

matrix.o: matrix.c matrix.h utils.h
	$(CC) $(DEBUG) $(CFLAGS) -c matrix.c

graphics_utils.o: graphics_utils.c graphics_utils.h
	$(CC) $(DEBUG) $(CFLAGS) -c graphics_utils.c

utils.o: utils.c utils.h
	$(CC) $(DEBUG) $(CFLAGS) -c utils.c

clean:
	rm -f *.o
