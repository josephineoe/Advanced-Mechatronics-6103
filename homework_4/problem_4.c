#include "simpletools.h" // Include simpletools

int main() // main function
{
  int fahr, celsius, lower, upper, step; //or use float for fahrand celsius
  lower=20; upper=120; step=1;
  pause(500);
  printf("Program Running!\n");
  printf("Temp in F\t Temp in C\n");
  while(fahr<=upper)
{
  celsius=5*(fahr-32)/9;
  printf(" %3d\t %4d\n", fahr, celsius); // 3 digit wide and 4 digit wide output
  // printf(%3.0f %6.1f\n", fahr, celsius);
  // x.yffloat x digits long and y after decimal
  
  fahr=fahr+step;
}
}