#include <Arduino.h>

volatile int btnCount = 0; 

void setup() {
    Serial.begin(9600);
    pinMode(2, INPUT_PULLUP); 
    attachInterrupt(digitalPinToInterrupt(2), int1_ISR, FALLING);
}

void loop() {
    Serial.println(btnCount);  
    delay(500); 
}

void int1_ISR() {
    btnCount++;  
}

