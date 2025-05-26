//#include <Servo.h>

//Servo myServo;  // Create a servo object
//int servoPin = 9;  // Pin connected to the servo
String command;  // Variable to store the incoming command
int ledPin = 13;
void setup() {
  Serial.begin(9600);  // Start the serial communication
  pinMode(ledPin, OUTPUT);
  //myServo.attach(servoPin);  // Attach the servo to the pin
}

void loop() {
  if (Serial.available() > 0) {
    command = Serial.readStringUntil('\n');  // Read the incoming command

    if (command.equals("TN33J1364") || command.equals("IN33J1364")) {
      digitalWrite(ledPin, HIGH);
      delay(3000);
      digitalWrite(ledPin, LOW);
      delay(1000);
    }
  }
}