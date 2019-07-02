#include "header.h"
#include <math.h>

void setup() {
    Serial.begin(115200);
    // pinMode(7, OUTPUT);
    energySetup();
}

void loop() {
    // // digitalWrite(7, true);
    // // delay(random(1000));
    // // digitalWrite(7, false);
    // // delay(random(1000));
    // if (Serial.available()) {
    //     char c = Serial.read();
    //     if (c == 'r') energySetup();
    // }
    energyLoop();
}

// void loop() {
//     uint8_t reading = analogRead(A0);
//     if (reading > 0) {
//         zeroCounter = 0;
//         tEnd = millis();
//         analogBuf[aCounter++] = reading;
//         energy += reading *
//         if (!readCount++) tStart = millis();
//         if (readCount == 500) {
//             for (int i = 0; i < 500; i++) {
//                 Serial.print(analogBuf[i]); Serial.print(",");
//             }
//             aCounter = 0;
//         }
//         if (aCounter >= bufLen) {
//             for (int i = 0; i < bufLen; i++) {
//                 Serial.print(analogBuf[i]); Serial.print(",");
//             }
//             aCounter = 0;
//         }
//     }
//     else if (zeroCounter < 1000) {
//         zeroCounter++;
//     }
//     else if (aCounter) {
//         for (int i = 0; i < aCounter; i++) {
//             Serial.print(analogBuf[i]); Serial.print(",");
//         }
//         Serial.print(reading); Serial.print(",");
//         Serial.println();
//         aCounter = 0;
//     }
//     else if (readCount) {
//         Serial.print(F("readCount: "));
//         Serial.println(readCount);
//         Serial.print(F("time: "));
//         Serial.println(tEnd - tStart);
//         readCount = 0;
//     }
// }

// #define minIdleTime 1000
// #define bufLen 1000

// volatile uint32_t lastEdgeTime, firstEdgeTime, idleTime, txTime, counter;
// volatile boolean triggered, printOutput;

// String logMessage = "";

// uint16_t aCounter = 0;
// uint8_t analogBuf[bufLen];

// void servicePulses();

// void setup()
// {
//     Serial.begin(115200);
//     ACSR =
//         (0 << ACD) |
//         (0 << ACBG) |
//         (0 << ACO) |
//         (1 << ACI) |
//         (1 << ACIE) |
//         (0 << ACIC) |
//         (1 << ACIS1) |
//         (1 << ACIS0);

//     pinMode(13, OUTPUT);
// }

// void loop()
// {
//     servicePulses();

//     if (triggered) {
//         analogBuf[aCounter++] = analogRead(A0);
//         if (aCounter == bufLen) {
//             for (int i = 0; i < bufLen; i++) {
//                 Serial.print(analogBuf[i]);
//                 Serial.print(",");
//             }
//             Serial.println();
//         }
//         aCounter %= bufLen;
//     }
//     else if (aCounter) {
//         for (uint16_t i = 0; i < bufLen; i++) {
//             if (i < aCounter) {
//                 Serial.print(analogBuf[i]);
//                 Serial.print(",");
//             }
//             analogBuf[i] = 0;
//         }
//         Serial.println();
//         aCounter = 0;
//     }

//     // if (Serial.available()) {
//     //     char c = Serial.read();
//     //     if (c == 'r') {
//     //         counter = 0;
//     //     }
//     // }
// }

// void servicePulses() {
//     uint32_t ms = millis();   
//     boolean afterIdle = (ms - lastEdgeTime) > minIdleTime;
//     if (triggered) {
//         if (afterIdle) {
//             firstEdgeTime = ms;
//             idleTime = ms - lastEdgeTime;
//             printOutput = true;
//         }
//         triggered = false;
//         lastEdgeTime = ms;
//     } else if (afterIdle && printOutput) {
//         txTime = lastEdgeTime - firstEdgeTime ? lastEdgeTime - firstEdgeTime : txTime;
//         logMessage = String(idleTime + txTime) + ", " + String(idleTime) + ", " + String(txTime) + ", " + ++counter;
//         Serial.println(logMessage);
//         printOutput = false;
//         triggered = false;
//     }
// }

// ISR(ANALOG_COMP_vect)
// {
//     digitalWrite(13, !digitalRead(13));
//     triggered = true;
// }