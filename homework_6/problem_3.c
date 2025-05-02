#include "simpletools.h"                      // Include simple tools


static volatile int new_count;
void counting(void *par1);
unsigned int stack[40+25];


int main()                                    // Main function
{ 

  int i;
  new_count = 1000;
  int count_array[300] = {};
  cogstart(&counting, NULL, stack, sizeof(stack));
 
    for (i = 0; i <= 300; i++){
      pause(1000);
      count_array[i] = new_count;
      print("count_array[%d] = %d/n", i, count_array[i]); 
   }       
   
    if (count_array[0] == 1001 && count_array[300] == 1300){
      print("it's all good");
    }      
    else {
      print("bad bad bad");
    }     
}

void counting(void *par1)
{ 
  while(1)
  {
    pause(1000);
    new_count++;
  }
}   