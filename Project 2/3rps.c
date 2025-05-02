#include "simpletools.h"                      // Include simpletools
#include "adcDCpropab.h" 
#include "imu_sensor.h"


#define RPS_LEG1_PIN 12
#define RPS_LEG2_PIN 13
#define RPS_LEG3_PIN 14
#define GANTRY_PIN1 15
#define GANTRY_PIN2 16

float total_duration = 17900; //~ milliseconds (17.9 seconds)
float total_distance = 0.095; //meters
float full_speed = 1700; //pulses per millisecond (1.7 pulses per second)

//const int RPS_LEG_PINS[] = {12, 13, 14};

void sensor_cog(void *par0);
void rps_cog1(void *par1);
void rps_cog2(void *par2);
void rps_cog3(void *par3);
void gantry_cog1(void *par4); //pending
void gantry_cog2(void *par5); //not written yet
void input_cog(void *par6);

//sensors
int16_t gyro_offsets[3];

//motors
//static volatile int leg1cog, leg2cog, leg3cog;
unsigned int servo1_stack_size[256];                 // Stack vars 
unsigned int servo2_stack_size[256];                 // Stack vars
unsigned int servo3_stack_size[256];                 // Stack vars
unsigned int gantry1_stack_size[256];                 // Stack vars
 
int main()                                    // main function
{ 
   // Initialize IMU
   mpu6050_init(); 
   
   //start cogs (lol)
   /*cogstart(rps_cog1, NULL, servo1_stack_size, sizeof(servo1_stack_size));
   cogstart(rps_cog2, NULL, servo2_stack_size, sizeof(servo2_stack_size));
   cogstart(rps_cog3, NULL, servo3_stack_size, sizeof(servo3_stack_size));*/
   
   cogstart(gantry_cog1, NULL, gantry1_stack_size, sizeof(gantry1_stack_size));
   
   //calibration....
   
   
 while(1){ 
        //print current roll and pitch
          current_pos();
          pause(500);
          }
                                                  
}

// Function that can continue on its 
// own if launched into another cog.
  
void rps_cog1(void *par1){
     while(1) {
          pulse_out(RPS_LEG1_PIN, 1700); //1ms 1000-1500 anti clockwise
          pause(1500);
          pulse_out(RPS_LEG1_PIN, 1500);
          pause(2500);
          pulse_out(RPS_LEG1_PIN, 1300);
          pause(1500);
             }
  }  
  
void rps_cog2(void *par2){
     while(1) {
          pulse_out(RPS_LEG2_PIN, 1700); 
          pause(1500);
          pulse_out(RPS_LEG2_PIN, 1500);
          pause(2500);
          pulse_out(RPS_LEG2_PIN, 1300);
          pause(1500);
             }
  }  
  
void rps_cog3(void *par3){
     while(1) {
          pulse_out(RPS_LEG3_PIN, 1700); 
          pause(20);
          pulse_out(RPS_LEG3_PIN, 1500);
          pause(20);
          pulse_out(RPS_LEG3_PIN, 1300);
          pause(20);
             }
  }  
 
void gantry_cog1(void *par4){
  while(1){
    for(int i=0; i<100;i++){
    pulse_out(GANTRY_PIN1, 1600); //RIGHT                      
    pause(20); 
  }    
    for(int i=0; i<10;i++){
    pulse_out(GANTRY_PIN1, 1500); //stop                      
    pause(20); 
  }    
  for(int i=0; i<100;i++){
    pulse_out(GANTRY_PIN1, 1400); //left                      
    pause(20); 
  }       
}
}
  
void input_cog(void *par6){
  pause(1000);                                      // Wait 1 s for Terminal app
  adc_init(21, 20, 19, 18);                         // CS=21, SCL=20, DO=19, DI=18

  float lrV, udV;                                   // Voltage variables

    while(1)                                          // Loop repeats indefinitely
    {
      udV = adc_volts(2);                             // Check A/D 2                
      lrV = adc_volts(3);                             // Check A/D 3
   
      putChar(HOME);                                  // Cursor -> top-left "home"
      print("Up/Down = %.2f V %c\n", udV, CLREOL);    // Display voltage
      print("Left/Right = %.2f V %c\n", lrV, CLREOL); // Display voltage
      pause(100);                                     // Wait 1/10 s        
   }     
 }
 
