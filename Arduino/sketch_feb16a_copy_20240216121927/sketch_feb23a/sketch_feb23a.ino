int led1 = 3;
int led2 = 10;
int button = 4;
int counter=0;
int previous=0;
void setup() {
  Serial.begin(9600);
  pinMode(led1, OUTPUT);
  pinMode(led2, OUTPUT);
  pinMode(button, INPUT);
}

void loop() {
  int clicked=digitalRead(button);
  if(clicked==1 and previous==0){
    counter+=1;
    delay(100);
  }
  previous=clicked;
  if(counter>2){
    digitalWrite(led1,HIGH);
    if(counter>4){
      digitalWrite(led2,HIGH);
    }
  }
  
}
