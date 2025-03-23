/*InterrExampDly Use this to generate a 1 second interrupt and blink
LED on 13. */
#include <avr/interrupt.h>
volatile unsigned int input_delay;
//counts number of Timer/Counter2 Overflow interrupts

void setup()
{
  pinMode(13,OUTPUT);
  init_timer2_ovf_interrupt(); //initialize Timer/Counter2 Overfl.
}
void loop()
{
  digitalWrite(13,LOW);
  pause(122); //1 second delay 244*4.096ms=1second
  digitalWrite(13,HIGH);
  pause(122); //1 second delay
}
/* ISR(TIMER2_OVF_vect) -increments counter on every interrupt. */
ISR(TIMER2_OVF_vect)
{
  input_delay++; //increment overflow counter
}

void init_timer2_ovf_interrupt(void)
{
  TCCR2A = 0x00; //Waveform generation mode normal
  TCCR2B = 0x06; //divide timer2 timebase by 256, overflow occurs every 4.1 ms
  TIMSK2 = 0x01; //enable timer2 overflow interrupt
  asm("SEI"); //enable global interrupt
}
/* pause(unsigned int num_of_4_1ms_interrupts): this delay function provides
the specified amount of delay as the number of 4.1 ms "clock ticks" using the
Timer/Counter2 Overflow interrupt. This function is only valid when using a
16 MHz crystal or ceramic resonator. If a different source frequency is used,
the clock tick delay value must be recalculated. */
void pause(unsigned int number_of_4_1ms_interrupts)
{
  TCNT2 = 0x00; //reset timer2
  input_delay = 0; //reset timer2 overflow counter
  while(input_delay <= number_of_4_1ms_interrupts); //wait for spec. number of intrpts.}
} 