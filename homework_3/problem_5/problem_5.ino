int ledPin = 8;
const byte btnPin = 2;

int dlyDebounce = 10; //number of repetiitons in aloop for debouncing
int ctr = 0;

boolean debounce(int btnPin)
{
  boolean currState, prevState;
  prevState = digitalRead(btnPin);
  for (int ctr = 0; ctr < dlyDebounce; ctr++)
 {
    delay(1);  
    currState= digitalRead(btnPin); 
    
    if(currState!= prevState)
      {
        ctr = 0; // if state changes, reset the counter 
        prevState= currState; 
      }
 }
}

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(ledPin, OUTPUT);
  pinMode(btnPin, INPUT_PULLUP);

}

void loop() {
  // put your main code here, to run repeatedly:
  Serial.print("Button state is: ");
  Serial.println(debounce(btnPin)); 

  if (!debounce(btnPin)) // check if debounced input is LOW
    digitalWrite(ledPin, HIGH);   // turns the LED on
  else 
    digitalWrite(ledPin, LOW);   // turns the LED off
}
