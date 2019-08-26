void setup() {
  // put your setup code here, to run once:
  pinMode(8,OUTPUT);
  pinMode(7,OUTPUT);
  pinMode(12,OUTPUT);
  pinMode(13,OUTPUT);
}

int timeout = 1000;
//8   = x0
//13  = x1
//7   = x2
//12  = x3

void loop() {
  // put your main code here, to run repeatedly:
  digitalWrite(8,LOW);
  digitalWrite(7,LOW);
  digitalWrite(12,LOW);
  digitalWrite(13,LOW);
  delay(timeout);
  digitalWrite(8,HIGH);
  digitalWrite(7,LOW);
  digitalWrite(12,LOW);
  digitalWrite(13,LOW);
  delay(timeout);
}
