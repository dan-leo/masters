
#include <Arduino.h>

boolean AT_enable = true;
boolean AT_REPLY_enable = true;
//boolean MURATA_REPLY_enable = true;
boolean SERIAL_REPLY_enable = true;
boolean PING_enabled = false;
boolean MQTT_enabled = true;


//#include "wiring_private.h"
//
//#define PIN_SERIAL2_RX 11
//#define PIN_SERIAL2_TX 10
//
//Uart Serial2 (&sercom1, PIN_SERIAL2_RX, PIN_SERIAL2_TX, SERCOM_RX_PAD_0, UART_TX_PAD_2);
//
///* IRQ handler hook called by the internal core */
//void SERCOM1_Handler()
//{
//  Serial2.IrqHandler();
//}

void setup() {
  // initialize digital pin LED_BUILTIN as an output.
  pinMode(LED_BUILTIN, OUTPUT);
  Serial1.begin(115200);
//  while (!SerialUSB);
  SerialUSB.begin(115200);
//  Serial2.begin(115200);
  Serial.begin(115200);
//  // Assign pins RX & TX SERCOM functionality
//  pinPeripheral(PIN_SERIAL2_RX, PIO_SERCOM);
//  pinPeripheral(PIN_SERIAL2_TX, PIO_SERCOM);
  SerialUSB.println(F("READY"));
  Serial1.print(F("\x1A"));
  Serial1.print(F("AT\r\n"));
  SerialUSB.println(Serial1.readString()); Serial1.print(F("AT+qmtdisc=0\r\n"));
  SerialUSB.println(Serial1.readString()); Serial1.print(F("AT+QIDNSCFG=1,\"8.8.8.8\",\"8.8.4.4\"\r\n"));
  SerialUSB.println(Serial1.readString()); Serial1.print(F("AT+QIDNSCFG=1,\"8.8.8.8\",\"8.8.4.4\"\r\n"));
  SerialUSB.println(Serial1.readString()); Serial1.print(F("at+qmtopen=0,\"demo.thingsboard.io\",1883\r\n"));
  SerialUSB.println(Serial1.readString()); Serial1.print(F("at+qmtconn=0,\"demo.thingsboard.io\",\"KD0wEWeMIMrNHFcQngaI\",\"\"\r\n"));
  pinMode(A0, INPUT);
  pinMode(A1, INPUT);
}

// the loop function runs over and over again forever
void loop() {
//  digitalWrite(LED_BUILTIN, HIGH);   // turn the LED on (HIGH is the voltage level)
//  delay(100);                       // wait for a second
//  digitalWrite(LED_BUILTIN, LOW);    // turn the LED off by making the voltage LOW
//  delay(100);                       // wait for a second

//	SerialUSB.print(Serial1.read(), 10);

	int c_usb = SerialUSB.read();
	int c_quec = Serial1.read();
//	int c_mura = Serial2.read();
	int c_ser = Serial.read();
	if (c_usb > 0) {
		if (c_usb == '!') AT_enable = !AT_enable;
		if (c_usb == '@') AT_REPLY_enable = !AT_REPLY_enable;
//		if (c_usb == ')') MURATA_REPLY_enable = !MURATA_REPLY_enable;
		if (c_usb == '#') SERIAL_REPLY_enable = !SERIAL_REPLY_enable;
		if (c_usb == '$') PING_enabled = !PING_enabled;
		if (c_usb == '%') MQTT_enabled = !MQTT_enabled;

		if (AT_enable) {
			//SerialUSB.write(c_usb);
//			Serial.write(c_usb);
			Serial1.write(c_usb);
//			Serial2.write(c_usb);
		}
	}
	if (c_quec > 0) {
		if (AT_REPLY_enable) SerialUSB.write(c_quec);
	}
//	if (c_mura > 0) {
//		if (MURATA_REPLY_enable) SerialUSB.write(c_mura);
//	}
	if (c_ser > 0) {
		if (SERIAL_REPLY_enable) SerialUSB.write(c_ser);
	}

	static unsigned long ms = millis();
	if (millis() - ms > 1000) {
		ms = millis();
		if (PING_enabled) Serial1.print(F("AT+QPING=1,\"1.1.1.1\",1,1\r\n"));
		if (MQTT_enabled) {
			Serial1.print(F("AT+QMTPUB=0,0,0,0,\"v1/devices/me/telemetry\"\r\n"));
			delay(50);
			Serial1.print(F("{\"temperature\":"));
			//37.00
			Serial1.print(analogRead(A0)/10);
			Serial1.print(F(",\"humidity\":"));
			//77.00
			Serial1.print(analogRead(A1)/10);
			Serial1.print(F("}\x1A"));
		}
	}
}
