#include <Wire.h>
#include "TSL2561.h"

// connect SCL to analog 5
// connect SDA to analog 4
// connect VDD to 3.3V DC
// connect GROUND to common ground

TSL2561 tsl(TSL2561_ADDR_FLOAT); 

void setup(void) {
  Serial.begin(9600);
  tsl.setGain(TSL2561_GAIN_16X);
  tsl.setTiming(TSL2561_INTEGRATIONTIME_13MS);
}

void loop(void) {

  uint32_t lum = tsl.getFullLuminosity();
  uint16_t ir, full;
  ir = lum >> 16;
  full = lum & 0xFFFF;
  //Serial.print("IR: "); Serial.print(ir);   Serial.print("\t\t");
  Serial.print("Lux: "); Serial.println(tsl.calculateLux(full, ir));
  
  delay(500); 
}
