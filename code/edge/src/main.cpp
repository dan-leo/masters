#include <Arduino.h>

#define minIdleTime 1000

volatile uint32_t lastEdgeTime, firstEdgeTime, idleTime, txTime;
volatile boolean triggered, printOutput;

String logMessage = "";

void setup()
{
    Serial.begin(115200);
    ACSR =
        (0 << ACD) |
        (0 << ACBG) |
        (0 << ACO) |
        (1 << ACI) |
        (1 << ACIE) |
        (0 << ACIC) |
        (1 << ACIS1) |
        (1 << ACIS0);

    pinMode(13, OUTPUT);
}

void loop()
{
    uint32_t ms = millis();   
    boolean afterIdle = (ms - lastEdgeTime) > minIdleTime;
    if (triggered) {
        if (afterIdle) {
            firstEdgeTime = ms;
            idleTime = ms - lastEdgeTime;
            printOutput = true;
        }
        triggered = false;
        lastEdgeTime = ms;
    } else if (afterIdle && printOutput) {
        txTime = lastEdgeTime - firstEdgeTime;
        logMessage = String(idleTime + txTime) + ", " + String(idleTime) + ", " + String(txTime);
        Serial.println(logMessage);
        printOutput = false;
        triggered = false;
    }
}

ISR(ANALOG_COMP_vect)
{
    digitalWrite(13, !digitalRead(13));
    triggered = true;
}

// uint32_t seconds = 0;
// uint8_t threshVolt = 0.3 * 255 / 5;
// uint32_t tRise = 0, tFall = 0;

// int currentEdge = 0, lastEdge = 0;

// boolean pulsed = false;
// volatile boolean triggered = false;

// ISR (ANALOG_COMP_vect)
// {
// 	triggered = true;
// }

// boolean onSecond() {
//     uint32_t s = millis()/1000;

//     if (s != seconds) {
//         seconds = s;
//         return true;
//     }
//     return false;
// }

// void setup () {
//     Serial.begin(115200);
//     pinMode(A0, INPUT);

//     ADCSRB = 0;        // (Disable) ACME: Analog Comparator Multiplexer Enable
//     ACSR = bit(ACI)    // (Clear) Analog Comparator Interrupt Flag
//            | bit(ACIE) // Analog Comparator Interrupt Enable
//            | bit(ACBG)
//            | bit(ACIS0); // ACIS1, ACIS0: Analog Comparator Interrupt Mode Select (trigger on falling edge)
// }

// void loop() {

//     int edge = analogRead(A0) > threshVolt;

//     if (triggered) {
//         Serial.println("triggered");
//         triggered = false;
//     }

//     if (edge != lastEdge) {
//         if (!edge) {
//             tFall = millis();
//         }

//         if ((millis() - tFall) > 50) {
//             // if (!pulsed) {
//             //     Serial.print(tFall - tRise); Serial.print(", ");
//             //     pulsed = true;
//             // }
//             if (edge && (millis() - tRise > 1000)) {
//                 // pulsed = false;
//                 tRise = millis();
//                 int diff = tRise - tFall;
//                 Serial.print(2540 - diff % 2540);
//                 Serial.print(", ");
//                 Serial.println(diff);
//             }
//         }
//     }

//     lastEdge = edge;
// }