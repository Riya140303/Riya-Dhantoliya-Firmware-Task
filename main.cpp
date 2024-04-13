#include <EEPROM.h>
#include <Arduino.h>

const int EEPROM_SIZE = 1024;
int addr = 0;
int count = 0;


void readEEPROM(){
  int temp = addr;
  for (addr = 0; addr<=temp; addr++){
    char c = EEPROM.read(addr);
    Serial.print(c);
  }
}


int writeEEPROM(){
    if(Serial.available() > 0 && addr < EEPROM_SIZE) {
      while(true){
        char receivedChar = Serial.read();
        EEPROM.write(addr, receivedChar);
        addr++;
        count++;
        if(count==100){
          digitalWrite(LED_BUILTIN, HIGH);
          delay(2000);
          digitalWrite(LED_BUILTIN, LOW);
          readEEPROM();
        }
          break;
    }

  }
  return 0;
}

void setup(){
  pinMode(LED_BUILTIN, OUTPUT);
  Serial.begin(2400);
  while(!Serial){

  }
  // Serial.println("ARDUINO IS WORKING!!!");
  writeEEPROM();
}

void loop(){

}