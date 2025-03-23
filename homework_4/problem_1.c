#include "simpletools.h"
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>
 
//problem 1
int main()                                    // Main function
{
  float w, r, t;
  print("Enter the angular velocity of a wheel (in rad/s)");
  scanf("%f", &w); 

  print("Enter the wheel radius (in m)");
  scanf("%f", &r); 

  print("Enter the travel duration (s)");
  scanf("%f", &t); 
  
  print("User, you have entered w= %0.1f, r=%0.1f and t=%0.1f)", w, r, t);

  float v = r*w;
  float s = v*t;
  
  print("The linear velocity and distance is v=%0.1f and s=%0.1f)", v, s);
  
}
