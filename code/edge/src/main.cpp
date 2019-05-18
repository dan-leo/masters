#include <Arduino.h>

#define minIdleTime 1000

volatile uint32_t lastEdgeTime, firstEdgeTime, idleTime, txTime, counter;
volatile boolean triggered, printOutput;

String logMessage = "";

void servicePulses();

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
    servicePulses();

    if (Serial.available()) {
        char c = Serial.read();
        if (c == 'r') {
            counter = 0;
        }
    }
}

void servicePulses() {
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
        logMessage = String(idleTime + txTime) + ", " + String(idleTime) + ", " + String(txTime) + ", " + ++counter;
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