#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <fcntl.h>
#include <unistd.h>

int main() {
    int fd;
    int r, g, b;
    char line[256];
    
    fd = open( "pic.ppm", O_CREAT | O_TRUNC | O_WRONLY, 0664 );
    
    sprintf( line, "P3\n500 500\n255\n" );
    write( fd, line, strlen(line) );
    
    for( int i = 0; i < 500; i++ ) {
        for( int j = 0; j < 500; j++ ) {
            r = 255;
            g = j%255;
            b = i%255;
            
            sprintf( line, "%d %d %d ", r, g, b );
            write( fd, line, strlen(line) );
        }
    }
    
    close( fd );
    
    return 0;
}