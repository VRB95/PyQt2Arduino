#include <dht.h>

dht DHT;

#define DHT11_PIN 8

void setup(){
  Serial.begin(9600);
}

void loop()
{
  int chk = DHT.read11(DHT11_PIN);
  Serial.print("T: ");
  Serial.print(DHT.temperature);
  Serial.print("\xC2"); 
  Serial.print("\xB0");
  Serial.print("C");
  Serial.print("\n");
  delay(2500);
}
