const int ledv1=2;
const int ledr1=3;
const int ledv2=4;
const int ledr2=5;

void setup() {
  Serial.begin(9600);
  pinMode(ledr1, OUTPUT);
  pinMode(ledv1, OUTPUT); 
  pinMode(ledr2, OUTPUT);
  pinMode(ledv2, OUTPUT);

}

void loop() {
 char comando = Serial.read();
 if(comando == 'a'){
  digitalWrite(ledv1, HIGH);
  digitalWrite(ledr1, LOW);
  digitalWrite(ledr2, HIGH);
  digitalWrite(ledv2, LOW);
 }

 if(comando == 'b'){
  digitalWrite(ledv1, LOW);
  digitalWrite(ledr1, HIGH);
  digitalWrite(ledr2, LOW);
  digitalWrite(ledv2, HIGH);  
 }
 

}
