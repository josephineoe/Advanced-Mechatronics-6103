#include "simpletools.h"                      // Include simpletools
#include "imu_sensor.h"
#include "servo.h"

#define RPS_LEG1_PIN 12
#define RPS_LEG2_PIN 13
#define RPS_LEG3_PIN 14

void rps_motor1(void *par1);                        // Forward declaration

//sensors
int16_t gyro_offsets[3];

static volatile int t;                     // Global vars for cogs to share

//motors
volatile int  cog1;
unsigned int stack1[300];                 // Stack vars for cog1
  
int main()                                    // main function
{
  t = 50; 
                                      // Set values of t & n 
   // Initialize IMU
    mpu6050_init(); 
    
     
  // Launch rps_motor1 function in another cog (processor).   
  cog1 = cog_run(rps_motor1, 256); 
  if (cog1 == -1) {
    print("Failed to start cog!\n");
                  }  

    servo_set(RPS_LEG1_PIN, 1600);
    pause(2500);
  // Main loop
    while(1) {
          current_pos();
          pause(t);
          
          
             }            
// all the cogs

}

// Function that can continue on its 
// own if launched into another cog.
void rps_motor1(void *par1)                         // current_pos keeps running
{
    while(1){
    servo_set(RPS_LEG1_PIN, 1600);
    pause(2500);
    print("Cog running...\n");  // Debugging output
    pause(500);
  }                       
}
