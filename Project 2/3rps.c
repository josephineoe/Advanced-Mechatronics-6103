#include "simpletools.h"                      // Include simpletools
#include "imu_sensor.h"
#include "servo.h"


#define RPS_LEG1_PIN 12
#define RPS_LEG2_PIN 13
#define RPS_LEG3_PIN 14

#define GANTRY_PIN1 15
#define GANTRY_PIN2 16

//const int RPS_LEG_PINS[] = {12, 13, 14};

void sensor_cog(void *par1);
void rps_cog1(void *par1);
void rps_cog2(void *par1);
void rps_cog3(void *par1);


//sensors
int16_t gyro_offsets[3];

//motors
//static volatile int leg1cog, leg2cog, leg3cog;
unsigned int servo1_stack_size[256];                 // Stack vars 
unsigned int servo2_stack_size[256];                 // Stack vars
unsigned int servo3_stack_size[256];                 // Stack vars
unsigned int sensor_stack_size[40+25];                 // Stack vars
 
int main()                                    // main function
{ 
   // Initialize IMU
   mpu6050_init(); 
   
   //start cogs (lol)
   cogstart(sensor_cog, NULL, sensor_stack_size, sizeof(sensor_stack_size));
   cogstart(rps_cog1, NULL, servo1_stack_size, sizeof(servo1_stack_size));
   cogstart(rps_cog2, NULL, servo2_stack_size, sizeof(servo2_stack_size));
   cogstart(rps_cog3, NULL, servo3_stack_size, sizeof(servo3_stack_size));
   
   //calibrate
   void calibrate_gyro(volatile int samples, volatile int16_t *offsets);
 while(1){
 }                     
 /*  while(1){
   //ground zero
   pulse_out(RPS_LEG1_PIN, 1700); 
   pause(20);
   pulse_out(RPS_LEG1_PIN, 1500);
   
   pulse_out(RPS_LEG2_PIN, 1700); 
   pause(20);
   pulse_out(RPS_LEG2_PIN, 1500);
   
   pulse_out(RPS_LEG3_PIN, 1700); 
   pause(20);
   pulse_out(RPS_LEG3_PIN, 1500);
    }*/  
  // servo_set(RPS_LEG_PINS[3], 1400);
   //servo_set(RPS_LEG2_PIN, 1400);
   //servo_set(RPS_LEG3_PIN, 1400);
   //pause(750);
   //servo_set(RPS_LEG_PINS[3], 1600);
   //servo_set(RPS_LEG2_PIN, 1600);
   //servo_set(RPS_LEG3_PIN, 1600);
   //pause(500);  
   //servo_disable(RPS_LEG_PINS[3]);
   //servo_disable(RPS_LEG2_PIN);
   //servo_disable(RPS_LEG3_PIN);                   
}

// Function that can continue on its 
// own if launched into another cog.

void sensor_cog(void *par1){
     while(1) {
          current_pos();
          pause(50);
             }
  }
  
void rps_cog1(void *par1){
     while(1) {
          pulse_out(RPS_LEG1_PIN, 1700); //1ms 1000-1500 anti clockwise
          pause(500);
          pulse_out(RPS_LEG1_PIN, 1500);
             }
  }  
  
void rps_cog2(void *par1){
     while(1) {
          pulse_out(RPS_LEG2_PIN, 1700); //1ms 1000-1500 anti clockwise
          pause(500);
          pulse_out(RPS_LEG2_PIN, 1500);
             }
  }  
  
void rps_cog3(void *par1){
     while(1) {
          pulse_out(RPS_LEG3_PIN, 1700); //1ms 1000-1500 anti clockwise
          pause(500);
          pulse_out(RPS_LEG3_PIN, 1500);
             }
  }  