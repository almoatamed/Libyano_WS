int RedPin = 3;      //Arduino driving pin for Red
int GreenPin = 2;    //Arduino driving pin for Green
int BluePin = 5;      //Arduino driving pin for Blue

void setColor(int red, int green, int blue)
{
  analogWrite(RedPin, red);
  analogWrite(GreenPin, green);
  analogWrite(BluePin, blue);
}

void setup()
{
  pinMode(RedPin, OUTPUT);    //Init Arduino driving pins
  pinMode(GreenPin, OUTPUT);
  pinMode(BluePin, OUTPUT);
  Serial.begin(9600);
}

void loop()
{
  
    setColor(149,27,129);

  delay(2000);

}
