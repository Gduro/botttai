
void setup() {
  Serial.begin(115200);
  pinMode(13, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  if (Serial.available() > 0){
    Serial.print("weszlo");
    String msg  = Serial.readString();
    if(msg == "OPEN")
    {
      Serial.print("kest");
      digitalWrite(13,HIGH);
    }
    else if (msg == "OFF"){
      digitalWrite(13,LOW);

    }
  }

}
