#include "simpletools.h"
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>

int arr_size = 50;
int rand_num;

float avg_array(int rand_array[], int arr_size){
 int sum =0;
 
 for (int i = 0; i < arr_size; i++){
   sum += rand_array[i];
} 
  return (float)sum/arr_size;
}
  
float std_deviation(int rand_array[], int arr_size, int avg){
  
  float values =0;
 
  for (int i = 0; i < arr_size; i++) {
        values += pow(rand_array[i] - avg, 2);
    }
 
   float variance = values / arr_size;
    
   return sqrt(variance);
} 

int main() // main function
{
  int i;
  int rand_array[arr_size];
  srand(time(NULL));
  
  pause(1000); 
  
  for (i = 0; i < 50; i++){
    pause(500);
    rand_array[i] = rand() % 100;
    
  }    
  float avg= avg_array(rand_array, arr_size);
   printf("Average: %.2f\n", avg);
  
  float deviation =  std_deviation(rand_array, arr_size, avg);
  printf("Deviation: %.2f\n", deviation);
  
  return 0;
}

