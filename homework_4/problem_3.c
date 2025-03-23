#include "simpletools.h"
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>
 
//problem 3

float computeBMI(float height, float weight){
 
 return (weight*703)/( height*height);  
}  

int main()                                    // Main function
{
  float height, weight;
  print("How tall are you boss (in feet and inches)");
  scanf("%f", &height); 

  print("How much do you weight (in pounds)");
  scanf("%f", &weight); 
  
  float bmi = computeBMI(height, weight);
  print("Your BMI is : %0.2f)", bmi);
  
}
