#include <Wire.h>
#include <LiquidCrystal_I2C.h>

String words;

LiquidCrystal_I2C lcd(0x27, 20, 4); // set the LCD address to 0x27 for a 16 chars and 2 line display

void setup()
{
  lcd.init();
  lcd.backlight();
  lcd.setCursor(0, 0);
  Serial.begin(9600);
}

void loop()
{
  while (Serial.available() > 0) {}
  words = Serial.readString();
  if (words.length() > 0)
  {
    lcd.clear();
    delay(20);
  }
  lcd.print(words);
  delay(100);


}
