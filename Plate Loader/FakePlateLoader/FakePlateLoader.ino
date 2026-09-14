String inputString = "";        // a String to hold incoming data
bool isStringComplete = false;  // whether the string is complete

void setup() {
  Serial.begin(19200);
  // reserve 200 bytes for the inputString:
  inputString.reserve(200);
}

void loop() {
  // print the string when a newline arrives:
  if (isStringComplete) {
    if (inputString.equals("RESET")) {
      Serial.println("READY, SAGIAN PE LOADER, ROM VER. 1.1.6, 12APR2001");
    } else if (inputString.startsWith("X-AXIS")) {
      Serial.println("READY, SAGIAN PE LOADER, ROM VER. 1.1.6, 12APR2001");
    } else if (inputString.startsWith("Z-AXIS EXTEND")) {
      Serial.println("READY, EXTENDED");
    } else if (inputString.startsWith("Z-AXIS RETRACT")) {
      Serial.println("READY, RETRACTED");
    } else if (inputString.equals("GRIPPER OPEN")) {
      Serial.println("READY, OPEN");
    } else if (inputString.equals("GRIPPER CLOSE")) {
      Serial.println("READY, CLOSED, NOPLATE");
    } else if (inputString.startsWith("MOVE")) {
      Serial.println("READY");
    } else if (inputString.equals("LOADER_STATUS")) {
      Serial.println("READY");
    } else if (inputString.startsWith("SET_DELAY")) {
      Serial.println("READY");
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
