#include <iostream>
#include <fstream>
#include <cmath>
#include <vector>

using namespace std;


#define width 500
#define height 500

typedef struct pixel{
  int r,g,b;
} pixel;
pixel board[height][width];

typedef int point[4];

void clear(){
  for (int i =0; i<height; i++){
    for (int j=0; j<width; j++){
      board[i][j].r = 255;
      board[i][j].g = 255;
      board[i][j].b = 255;
    }
  }
}
//plots a point at x,y with colors r,g,b
void plot(int x, int y, int r, int g, int b){
  board[y][x].r = r;
  board[y][x].g = g;
  board[y][x].b = b;
}
int drawOct1(int x0, int y0, int x1, int y1){
  int a = 2*(y0-y1);
  int b = -2*(x0-x1);
  int d = a + b/2;
  while ( x0 < x1 ){
    plot(x0,y0,0,0,0);
    if (d){
      y0++;
      d+=b;
    }
    x0++;
    d+=a;
  }
}
int drawOct2(int x0,int y0, int x1, int y1){
  int a = 2*(y0-y1);
  int b = -2*(x0-x1);
  int d = a/2 + b;
  while ( y0 < y1 ){
    plot(x0,y0,0,0,0); 
    if (d){
      x0++;
      d+=a;
    }
    y0++;
    d+=b;
  }
}
int drawOct8(int x0, int y0, int x1, int y1){
  int a = 2*(y0-y1);
  int b = -2*(x0-x1);
  int d = a + b/2;
  while ( x0 < x1 ){
    plot(x0,y0,0,0,0);
    if (d){
      y0--;
      d-=b;
    }
    x0++;
    d+=a;
  }
}
int drawOct7(int x0, int y0, int x1, int y1){
  int a = 2*(y0-y1);
  int b = -2*(x0-x1);
  int d = a/2 + b;
  while ( y0 > y1 ){
    plot(x1,y1,0,0,0); 
    if (d){
      x1--;
      d-=a;
    }
    y1++;
    d+=b;
  }
}
//draws from x0,y0 to x1, y1
int draw(int x0, int y0, int x1, int y1){
  double slope;
  slope = ((double)y1-(double)y0)/((double)x1-(double)x0);
  //if positive
  if (slope > 0){
    if (slope > 1){//if steep
      if (x0 < x1){//if left to right
	drawOct2(x0,y0,x1,y1);
      }else{//if right to left
	drawOct2(x1,y1,x0,y0);
      }
    }else{//else if not steep
      
      if (x0 < x1){//if left to right
	drawOct1(x0,y0,x1,y1);
      }else{//if right to left
	drawOct1(x1,y1,x0,y0);
      }
    }
  }else{
    if (slope < -1){//if steep
      if (x0 < x1){//if left to right
	drawOct7(x0,y0,x1,y1);
      }else{//if right to left
	drawOct7(x1,y1,x0,y0);
      }
    }else{//else if not steep
      if (x0 < x1){//if left to right
	drawOct8(x0,y0,x1,y1);
      }else{//if right to left
	drawOct8(x1,y1,x0,y0);
      }
    }
  }
}

//incase of matrix math
#define PT_SIZE 4
vector<int> v;
//vector form: x0,y0,z0,1,x1,y1,z1,1...xi,yi,zi,1,xj,yj,zj,1...etc
//matrix of edges: p1-p2, p3-p4, p5-p6, etc
void add_point(int x,int y,int z){
  v.push_back(x);
  v.push_back(y);
  v.push_back(z);
  v.push_back(1);
}
void add_edge(int x0, int y0, int z0,int x1, int y1, int z1){
  add_point(x0,y0,z0);
  add_point(x1,y1,x1);
}
void draw_edges(){
  int points = v.size()/4;
  for (int i=0;i<points;i+=2){
    //could go for optimization here but lazy.
    int x0 = v[PT_SIZE*i];
    int y0 = v[PT_SIZE*i+1];
    int x1 = v[PT_SIZE*i+PT_SIZE];
    int y1 = v[PT_SIZE*i+PT_SIZE+1];
    draw(x0,y0,x1,y1);
    //int z0 = v[PT_SIZE*i+2];
    //int z1 = v[PT_SIZE*i+PT_SIZE+2];
    //and then theres that 1.
  }
}
//////////////
int main(){
  ofstream stream;
  stream.open("pic.ppm");
  stream << "P3\n";
  stream << "#stuff\n";
  stream << "500 500\n";
  stream << "255\n";  
  clear();
  
  add_edge(250,250,0,350,300,0);
  add_edge(250,250,0,300,350,0);
  add_edge(250,250,0,350,200,0);
  add_edge(250,250,0,300,150,0);
  add_edge(250,250,0,150,200,0);
  add_edge(250,250,0,200,150,0);
  add_edge(250,250,0,150,300,0);
  add_edge(250,250,0,200,350,0);

  draw_edges();

  int i,j;
  for (i=0;i<height;i++){
    for (j=0;j<width;j++){
      stream << (board[i][j]).r << " ";
      stream << (board[i][j]).g << " ";
      stream << (board[i][j]).b << " ";
    }
    //if not the last row
    if (i != height-1)
      stream << "\n";
  }
  stream.close();
  cout << "done\n";
}
