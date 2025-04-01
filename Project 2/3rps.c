#include "simpletools.h"                      // Include simpletools
#include "imu_sensor.h"
#include "servo.h"
#include "mstimer.h"


#define RPS_LEG1_PIN 12
#define RPS_LEG2_PIN 13
#define RPS_LEG3_PIN 14

void sensor_cog(void *par1);
void rps_motor1(void *par1);                        // Forward declaration
void rps_motor2(void *par2);                        // Forward declaration
void rps_motor3(void *par3);                        // Forward declaration

//sensors
int16_t gyro_offsets[3];

static volatile int t;                     // Global vars for cogs to share

//motors
static volatile int cog1;
unsigned int servo_stack_size[300];                 // Stack vars 


  
int main()                                    // main function
{ 
   // Initialize IMU
   mpu6050_init(); 
   
   //start cogs
   cogstart(&rps_motor1, NULL, servo_stack_size, sizeof(servo_stack_size));
   cogstart(&rps_motor2, NULL, servo_stack_size, sizeof(servo_stack_size));
   cogstart(&rps_motor3, NULL, servo_stack_size, sizeof(servo_stack_size));
   
   //calibrate
   void calibrate_gyro(volatile int samples, volatile int16_t *offsets);
   
   // run all the cogs (lol)  
  // Launch rps_motor1 function in another cog (processor).   
  cog1 = cog_run(rps_motor1, servo_stack_size); 
  if (cog1 == -1) {
    print("Failed to start cog!\n");
                  }
   //cog_run(rps_motor2, servo_stack_size);
   //cog_run(rps_motor3, servo_stack_size);
                    
   servo_set(RPS_LEG1_PIN, 1600);
   pause(2500);
   
  // Main loop
    while(1) {
          current_pos();
          pause(t);
             }            
}

// Function that can continue on its 
// own if launched into another cog.

void sensor_cog(void *par1){
     while(1) {
          current_pos();
          pause(t);
             }
  }
void rps_motor1(void *par1)                         // current_pos keeps running
{
    while(1){
    servo_set(RPS_LEG1_PIN, 1600);
    servo_disable(RPS_LEG1_PIN);
  }                       
}

void rps_motor2(void *par1)                         // current_pos keeps running
{
    while(1){
    servo_set(RPS_LEG2_PIN, 1600);
    servo_disable(RPS_LEG2_PIN);
  }                       
}

void rps_motor3(void *par1)                         // current_pos keeps running
{
    while(1){
    servo_set(RPS_LEG3_PIN, 1600);
    servo_disable(RPS_LEG3_PIN);
  }                       
}
