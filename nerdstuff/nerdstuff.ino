int led = 13;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(A1, INPUT_PULLUP);
  double lightSensorPin = A1;
}

void loop() {
  // put your main code here, to run repeatedly:
  double lightSensorPin =  analogRead(A1);
  Serial.println(String(lightSensorPin));
  delay(300);
}

