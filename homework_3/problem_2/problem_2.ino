#include <stdio.h>

void setup() {
  DDRD |= bit(DDD4); // Set pin 4 (PORTD4) as output
}

void loop() {
  bitSet(PORTD, PD4); // Turn LED on
  delay(500);
  bitClear(PORTD, PD4); // Turn LED off
  delay(500);
}