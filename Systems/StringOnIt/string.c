#include <stdlib.h>
#include <stdio.h>
#include <string.h>

int slen(char t[]);
char *scpy(char *dest, char *source);
char *sncpy(char *dest, char *source, int n);
char *scat(char *s1, char *s2);
int scmp(char *s1, char *s2);
int sncmp(char *s1, char *s2, int n);
char *schr(char *s, char c);
char *sstr(char *s, char *key);

int main(){
  char s[10]="hello";
  printf("%s: %d\n",s,slen(s)); //testing for slen
  char cpy[15]="aba";
  printf("After scpy, %s became: ",cpy);
  scpy(cpy,s);
  printf("%s\n",cpy);
  char ncpy[15]="abalaba";
  printf("After sncpy (n=3), %s became: ",ncpy);
  sncpy(ncpy,s,3);
  printf("%s\n",ncpy);
  char cat[15]="AddOn";
  printf("After scat, %s became: ",cpy);
  scat(cpy,cat);
  printf("%s\n",cpy);
  char s2[18]="hello";
  char s3[5]="po";
  char s4[5]="bao";
  printf("scmp %s and %s: %d\n",s,s2,scmp(s,s2));
  printf("scmp %s and %s: %d\n",s,cpy,scmp(s,cpy));
  printf("scmp %s and %s: %d\n",s,s3,scmp(s,s3));
  printf("scmp %s and %s: %d\n",s,s4,scmp(s,s4));
  printf("schr %s and %c: %s\n",s,'l',schr(s,'l'));
  printf("schr %s and %c: %s\n",s,'t',schr(s,'t'));
  char s5[5]="el";
  printf("sstr %s and %s: %s\n",s,s5,sstr(s,s5));
  printf("sstr %s and %s: %s\n",s,s3,sstr(s,s3));
  return 0;
}

int slen(char t[]){
    int x=0;
    while(t[x]){
      x++;
    }
    return x;
}

char *scpy(char *dest, char *source){
  int x=0;
  while(source[x]){
    dest[x]=source[x];
    x++;
  }
  return dest;
}

char *sncpy(char *dest, char *source, int n){
  int x=0;
  while(source[x]&&x<n){
    dest[x]=source[x];
    x++;
  }
  if(x==n){
    dest[x]=0;
  }
  return dest;
}

char *scat(char *s1, char *s2){
  int x=0;
  int y=slen(s2);
  while(s2[x]){
    s1[y+x]=s2[x];
    x++;
  }
  return s1;
}

int scmp(char *s1, char *s2){
  int x=0;
  while(s1[x]==s2[x]&&s1[x]){
    x++;
  }
  return s1[x]-s2[x];
}

//unchecked
int sncmp(char *s1, char *s2, int n){
  int x=0;
  while(s1[x]==s2[x]&&s1[x]&&x<n){
    x++;
  }
  return s1[x]-s2[x];
}

char *schr(char *s, char c){
  int x=0;
  while(s[x]!=c&&s[x]!=0){
    x++;
  }
  if(s[x]==c){
    return &s[x];
  }else{
    return 0;
  }
}

//unchecked
char *sstr(char *s, char *key){
  int x=0;
  while(&s[x]!=key&&s[x]!=0){
    x++;
  }
  if(sncmp(&s[x],key,slen(key))){
    return &s[x];
  }else{
    return 0;
  }
}
