#include <LiquidCrystal_I2C.h>

LiquidCrystal_I2C LCD(0x27,16,2);

int Trig=7;
int Echo=8;
int SWpin=13;
float echotime;
float distance;
float T=22.0;
float Predis;
float v=(331+0.6*T)*100/1000000; 

void setup() 
{
  // put your setup code here, to run once:
  pinMode(13,INPUT);
  Serial.begin(9600);
  pinMode(Trig,OUTPUT);
  pinMode(Echo,INPUT);
  LCD.init();
  LCD.backlight();
}

void loop() 
{
  float Predis=distance;

  if( digitalRead(13)==0 )
  {
    return;
  }
  
  // put your main code here, to run repeatedly:
  digitalWrite(Trig,1);
  delay(5);
  digitalWrite(Trig,0);

  echotime=pulseIn(Echo,1);
  distance=v*(echotime/2);

  if( distance<4 || distance>400 )
  {
    return;
  }

  Serial.print("D=");
  Serial.print(distance);
  Serial.println("cm");
  LCD.clear();
  LCD.setCursor(0,0);
  LCD.print("Distance is"); 
  LCD.setCursor(0,1);
  LCD.print(distance);
}
