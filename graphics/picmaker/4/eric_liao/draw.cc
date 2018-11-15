#include <iostream>
#include <fstream>
#include <stdlib.h>
#include <stdio.h>
#include <math.h>

#define pi 3.14159265

using namespace std;
typedef struct pixel{
  int r;
  int g;
  int b;
} pixel;

int height=500;
int width=500;
pixel pic[500][500];
/* backgrounds */
void bg1(){
  int i;
  int j;
  for (i=width-1; i > -1; i--){
    for(j=height-1; j > -1; j--){
      pic[i][j].r = sqrt(pow((double)i-width/2,2)+pow((double)j-height/2,2)) / 2;
      pic[i][j].g = sqrt(pow((double)i-width/2,2)+pow((double)j-height/2,2)) / 4;
      pic[i][j].b = sqrt(pow((double)i-width/2,2)+pow((double)j-height/2,2)) / 2;
    }
  }
}


//special case for draw_flower(rt 2)
void ubercool(int radius, double edges, int thickness){
  double degrees = 0;
  while ( degrees < 5200 ){
    double radians = degrees/180*pi;
    double x = radius * cos(radians) * cos(edges * radians);
    double y = radius * sin(radians) * cos(edges * radians);
    
    int start_x = x-thickness;
    int start_y = y-thickness;
    while ( start_x++ < x + thickness ){
      while ( start_y++ < y + thickness ){
	pic[(int)start_y+height/2][(int)start_x+width/2].r = 255;
      }
    }
    degrees+= 0.03;
  }
}
void draw_flower(int radius, int edges, int thickness){
  double degrees = 0;
  while ( degrees < 360 ){
    double radians = degrees/180*pi;
    double x = radius * cos(radians) * cos(edges * radians);
    double y = radius * sin(radians) * cos(edges * radians);
    
    int start_x = x-thickness;
    int start_y = y-thickness;
    while ( start_x++ < x + thickness ){
      while ( start_y++ < y + thickness ){
	pic[(int)start_y+height/2][(int)start_x+width/2].r = 255;
      }
    }
    degrees+= 0.03;
  }
  
}
void fill_flower(int radius,int edges){
  while ( radius-- > 0 ){
    double degrees = 0;
    while ( degrees < 360 ){
      double radians = degrees/180*pi;
      double x = radius * cos(radians) * cos(edges * radians);
      double y = radius * sin(radians) * cos(edges * radians);
      pic[(int)y+height/2][(int)x+width/2].r = radius;
      pic[(int)y+height/2][(int)x+width/2].g = radius/2;
      pic[(int)y+height/2][(int)x+width/2].b = radius/2;
      degrees+= 0.03;
    }
    //cout<< radius << "\n";
  }
}
void rotate_flower(int radius,int edges,double angle){
  while ( radius-- > 0 ){
    double degrees = 0;
    while ( degrees < 360){
      double radians = degrees/180*pi;
      double x = radius * cos(radians + angle/edges) * cos(edges * radians);
      double y = radius * sin(radians + angle/edges) * cos(edges * radians);
      pic[(int)y+height/2][(int)x+width/2].b = radius;
      pic[(int)y+height/2][(int)x+width/2].g = radius/2;
      pic[(int)y+height/2][(int)x+width/2].r = radius/2;
      degrees+= 0.03;
    }
    //cout<< radius << "\n";
  }
}

int main(){
  ofstream stream;
  stream.open("pic.ppm");
  //pbm header
  stream << "P3\n";
  stream << "#lol fancy image\n";
  stream << "500 500\n";
  stream << "255\n";
  //int max: 2,147,483,647, 10 digits.
  char* h = (char*)calloc(11,sizeof(char));
  char* w = (char*)calloc(11,sizeof(char));
  
  //fill_flower(250,5);
  //rotate_flower(250,5,72);
  //fill_flower(250,1);
  bg1();
  ubercool(240,1.41421356237,1);
  
  int i,j;
  for (i=0;i<height;i++){
    for (j=0;j<width;j++){
      stream << (pic[i][j]).r << " ";
      stream << (pic[i][j]).g << " ";
      stream << (pic[i][j]).b << " ";
    }
    //if not the last row
    if (i != height-1)
      stream << "\n";
  }
  
  stream.close();
  cout << "lol\n";
}

