#include "simpletools.h"

static volatile int a, b;

int main(){  
  int a = 3;
  int b = 4;
  
  int add = addition(a, b);
  print("A+B = %d\n", add);
  int sub = subtraction(a, b);
  print("A-B = %d\n", sub);
  int mult = multiplication(a, b);
  print("A*B = %d\n", mult);
  int div = division(a, b);
  print("A/B = %d\n", div);
  
}  
