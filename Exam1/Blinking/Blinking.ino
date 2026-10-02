String inputString = "";
bool isStringComplete = false;

#define LED_BUILTIN 13

void setup() {
  Serial.begin(9600);

  pinMode(LED_BUILTIN, OUTPUT);
  digitalWrite(LED_BUILTIN, LOW);

  inputString.reserve(200);
}

void loop() {
  if (isStringComplete) {
    if (inputString.startsWith("LED")) {
      if (inputString.endsWith("ON")) {
        digitalWrite(LED_BUILTIN, HIGH);

        Serial.println("LED On");
      } else if (inputString.endsWith("OFF")) {
        digitalWrite(LED_BUILTIN, LOW);

        Serial.println("LED Off");
      } else {
        Serial.print("Unrecognized Command --> ");
        Serial.println(inputString);
      }
    } else if (inputString.startsWith("FLASH")) {
      int firstSpace = inputString.indexOf(' ');
      int secondSpace = inputString.indexOf(' ', firstSpace + 1);

      int flashes = inputString.substring(firstSpace + 1, secondSpace).toInt();
      int cycleTime = inputString.substring(secondSpace + 1).toInt();

      for (int i = 0; i < flashes; i++) {
        digitalWrite(LED_BUILTIN, HIGH);
        delay(cycleTime/2);
        digitalWrite(LED_BUILTIN, LOW);
        delay(cycleTime/2);
      }

      Serial.print("Flashes = ");
      Serial.print(flashes);
      Serial.print("   ");
      Serial.print("PeriodMS = ");
      Serial.println(cycleTime);
    } else {
        Serial.print("Unrecognized Command --> ");
        Serial.println(inputString);
    }

    inputString = "";
    isStringComplete = false;
  }
}

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
