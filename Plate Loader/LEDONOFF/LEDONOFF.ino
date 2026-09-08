String inputString = "";        // a String to hold incoming data
bool isStringComplete = false;  // whether the string is complete

void setup() {
  Serial.begin(19200);
  // reserve 200 bytes for the inputString:
  inputString.reserve(200);

  pinMode(LED_BUILTIN, OUTPUT);
}

void loop() {
  // print the string when a newline arrives:
  if (isStringComplete) {
    inputString.toUpperCase();

    if (inputString.equals("LED ON")) {
      digitalWrite(LED_BUILTIN, HIGH);
      Serial.println("The LED is now on");
    } else if (inputString.equals("LED OFF")) {
      digitalWrite(LED_BUILTIN, LOW);
      Serial.println("The LED is now off");
    } else {
      Serial.print("Unrecognized Command --> ");
      Serial.println(inputString);
    }


    // clear the string:
    inputString = "";
    isStringComplete = false;
  }
}

/*
  SerialEvent occurs whenever a new data comes in the hardware serial RX. This
  routine is run between each time loop() runs, so using delay inside loop can
  delay response. Multiple bytes of data may be available.
*/
void serialEvent() {
  while (Serial.available()) {
    char inChar = (char)Serial.read();
    if (inChar == '\n') {
      isStringComplete = true;
    } else {
      inputString += inChar;
    }
  }
}
