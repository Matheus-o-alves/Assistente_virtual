String inputString = "";         // a String to hold incoming data
bool stringComplete = false;  // whether the string is complete
int led = 2;
void setup() {
  // initialize serial:
  Serial.begin(9600);
  // reserve 200 bytes for the inputString:
  inputString.reserve(200);
  
  pinMode(led, OUTPUT);
}
   void loop() {
  // print the string when a newline arrives:
  if (stringComplete) {
    Serial.print(" ");
    Serial.print(inputString);
    // clear the string:
    if(inputString.startsWith("ligar")){ //19
     digitalWrite(led, digitalRead(LOW));// toggle
   
    }
      
     else if (inputString.startsWith("desligar")){
      digitalWrite(led, digitalRead(HIGH));
    }
      
    
  //  else
  // Serial.print(F("Comando Invalido[ Fale(ligar) para ligar  led ou (desligar) para desligar led)]"));
   
    inputString = "";
    stringComplete = false;
  }
}

/*
  SerialEvent occurs whenever a new data comes in the hardware serial RX. This
  routine is run between each time loop() runs, so using delay inside loop can
  delay response. Multiple bytes of data may be available.
*/
void serialEvent() {
  while (Serial.available()) {
    // get the new byte:
    char inChar = (char)Serial.read();
    // add it to the inputString:
    inputString += inChar;
    // if the incoming character is a newline, set a flag so the main loop can
    // do something about it:
    if (inChar == '\n') {
      stringComplete = true;
    }
  }
}
