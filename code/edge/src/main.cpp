

#include <Arduino.h>

uint32_t seconds = 0, i = 0;

void setup () {
    Serial.begin(115200);
    pinMode(A0, INPUT);
}

void loop() {
    uint32_t s = millis()/1000;

    int r = analogRead(A0);
    
    if (s != seconds) {
        Serial.print(i, DEC);
        Serial.print(": ");
        Serial.println(r, DEC);
        seconds = s;
        i = 0;
    }

    i++;
}