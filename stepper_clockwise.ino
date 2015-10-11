
/* 
 Stepper Motor Control - one revolution
 
 Original code from the Aduino package:
 Created 11 Mar. 2007
 Modified 30 Nov. 2009
 by Tom Igoe
 
 This program drives a unipolar or bipolar stepper motor. 
 The motor is attached to digital pins 8 - 11 of the Arduino.
 
 The motor should revolve one revolution in one direction, then
 one revolution in the other direction.  
 
 _____________________________________
 
 Serial Events from 
 https://www.arduino.cc/en/Tutorial/SerialEvent
 
 _____________________________________
 
 Modified by Sophia Thach For this project
 10/10/2015
 
 This program drives a unipolar stepper motor. 
 (Step Motor 28BYJ-48 5V)
 and using the Arduino Uno.
 
 Acknowlements: Brandon helped alot
 */
#include <Stepper.h>

int stepsPerRevolution = 205;  // change this to fit the number of steps per revolution
// for your motor

//counts the number of steps that have been processed. 
int steps;

//verifies for the string that is inputted is complete
boolean stringComplete=false;

//the string that is inputted
String inputString="";


// initialize the stepper library on pins 8 through 11:
Stepper myStepper(stepsPerRevolution, 8,9,10,11);            

void setup() {
  //initialize steps to 0
  steps=0;

  // set the speed at 50 rpm:
  myStepper.setSpeed(50);

  // initialize the serial port:
  Serial.begin(9600);
  
  // reserve 200 bytes for the inputString:
  inputString.reserve(200);
}

void loop() {
  serialEvent(); //call the function

  if(stringComplete){
    // step one revolution  in one direction:
    //while loop ensures that cog takes only 10 steps
    //which is one revolution = 205 (steps per revolution) (divided) 50 (speed)
    // the extra 5 steps per revolution accounts for error

    while(steps<10){
      Serial.println("clockwise");
      myStepper.step(stepsPerRevolution);
      steps++;
    }
    
    //reset all values so you're able to accept a new command (a new string)
    steps=0;
    stringComplete=false;
    inputString="";
  }
}


/*
  SerialEvent occurs whenever a new data comes in the
 hardware serial RX.  This routine is run between each
 time loop() runs, so using delay inside loop can delay
 response.  Multiple bytes of data may be available.
 */
void serialEvent() {
  while (Serial.available()) {
    // get the new byte:
    char inChar = (char)Serial.read();
    // add it to the inputString:
    inputString += inChar;
    // if the incoming character is a newline, set a flag
    // so the main loop can do something about it:
    if (inChar == '\n') {
      Serial.println("hi");
      stringComplete = true;
    }
  }
}









