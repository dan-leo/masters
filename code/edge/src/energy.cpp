#include "header.h"

// #define bufLen 2000
// uint16_t aCounter = 0;
// uint32_t prevMillis = 0;
// uint8_t analogBuf[bufLen];
volatile uint32_t tStart, tEnd, sum = 0, idleTime = 0, txTime = 0, tOffset = 0;
volatile uint32_t zeroCounter = 0, readCount = 0;
volatile double energy = 0;
uint8_t maxReading = 0;
// boolean prime = false;

void energySetup() {
    sum = idleTime = txTime = readCount = maxReading = energy = 0;
}

void energyLoop() {
    uint8_t reading = analogRead(A0);
    if (reading > 20) {
        // Serial.println(reading);
        if (reading > maxReading) maxReading = reading;
        if (!readCount++) {
            tStart = millis();
            idleTime = tStart - tEnd;
        }
        tEnd = millis();
        zeroCounter = 0;
        sum += reading;
    }
    else if (zeroCounter < 10000) {
        // if (!zeroCounter) tEnd = millis();
        zeroCounter++;
    }
    else if (readCount) {
        txTime = tEnd - tStart;
        energy = sum * 500 / 1023.0 * txTime / 1000 / 1000;
        Serial.print(idleTime); Serial.print(",");
        Serial.print(txTime); Serial.print(",");
        Serial.print(idleTime + txTime); Serial.print(",");
        Serial.print(energy); Serial.print(",");
        Serial.println(maxReading/2);
        energySetup();
    }
}