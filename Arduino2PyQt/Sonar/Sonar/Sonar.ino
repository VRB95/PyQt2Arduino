#include<NewPing.h>
#define trig A0
#define echo A1
#define maximum 200
int usec;
int cm;
NewPing sonar(trig, echo, maximum);
void setup()
{

Serial.begin(9600);

}
void loop(){ 
usec=sonar.ping();
cm=usec/58;
Serial.print("Distance: ");
Serial.print(cm);
Serial.print("\n");

delay(200);
}
