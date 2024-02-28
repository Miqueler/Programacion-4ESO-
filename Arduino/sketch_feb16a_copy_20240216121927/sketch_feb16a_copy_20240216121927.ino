const int ledPin = 9;

void setup() {
  Serial.begin(9600);
  pinmode(ledPin, OUTPUT);
}

void loop() {
  digitalWrite(ledPin, HIGH);
  delay(1000);
  digitalWrite(ledPin, HIGH);
  delay(1000);
}

