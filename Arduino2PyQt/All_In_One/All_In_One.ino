#include <LiquidCrystal_I2C.h>
#include <Wire.h>
#include <dht.h>
#include "TSL2561.h"
#define DHT11_PIN 8
#include<NewPing.h>
#define trig A0
#define echo A1
#define maximum 200
int usec;
int cm;
NewPing sonar(trig, echo, maximum);

// connect SCL to analog 5
// connect SDA to analog 4
// connect VDD to 3.3V DC
// connect GROUND to common ground
TSL2561 tsl(TSL2561_ADDR_FLOAT); 

bool isLcdActivated = false;
bool isLightActivated = false;
bool isTempActivated = false;
bool isSonarActivated = false;
String words;
dht DHT;
LiquidCrystal_I2C lcd(0x27,20,4);  // set the LCD address to 0x27 for a 16 chars and 2 line display

void setup()
{
    Serial.begin(9600);
    lcd.init(); 
    lcd.backlight();
    lcd.setCursor(0,0);
    tsl.setGain(TSL2561_GAIN_16X);
    tsl.setTiming(TSL2561_INTEGRATIONTIME_13MS);
}

void loop()
{
    /*
     * verify serial incomming
     */
     
    while (Serial.available()>1){}
    
    /*
     * loop that run forever
     */
    
    words = Serial.readString();
    //Serial.println("Read");

    /*  
     *  check words
     *  avtivate lcd output
     */
     
    if (words.startsWith("lcd")){
        isLcdActivated = true;
        isLightActivated = false;
        isTempActivated = false;
        isSonarActivated = false;
        lcd.clear();    
    }
    
    if (isLcdActivated == true){
        lcd.setCursor(0,0);
        if (words.length() > 0)
        {
          lcd.clear();
          delay(20);
        }
        lcd.print(words);
        delay(100);
    }

    if (words.startsWith("light")){
        isLcdActivated = false;
        isLightActivated = true;  
        isTempActivated = false;
        isSonarActivated = false;
    } 

    if (isLightActivated == true){
        uint32_t lum = tsl.getFullLuminosity();
        uint16_t ir, full;
        ir = lum >> 16;
        full = lum & 0xFFFF;
        Serial.print("Lux: "); Serial.println(tsl.calculateLux(full, ir));
        delay(100);
    }

    if (words.startsWith("temp")){
        isLcdActivated = false;
        isLightActivated = false;  
        isTempActivated = true;
        isSonarActivated = false;
    } 

    if (isTempActivated == true){
        int chk = DHT.read11(DHT11_PIN);
        Serial.print("T: ");
        Serial.print(DHT.temperature);
        Serial.print("\xC2"); 
        Serial.print("\xB0");
        Serial.print("C");
        Serial.print("\n");
        delay(2500);
    }

    if (words.startsWith("distance")){
        isLcdActivated = false;
        isLightActivated = false;  
        isTempActivated = false;
        isSonarActivated = true;
    } 

    if (isSonarActivated == true){
        usec=sonar.ping();
        cm=usec/58;
        Serial.print("Distance: ");
        Serial.print(cm);
        Serial.print("\n");
        
        delay(200);
    }

    
    if (words.startsWith("close")){
        isLcdActivated = false;
        isLightActivated = false;
        isTempActivated = false; 
        isSonarActivated = false;
        lcd.clear();  
    } 
    
}
