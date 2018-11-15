/*
 * mqtt.cpp
 *
 *  Created on: 14 Nov 2018
 *      Author: d7rob
 */

#include <fusion.h>

void setup_mqtt() {
	Serial1.print(F("\x1A\x1A"));
	SerialUSB.println(Serial1.readString()); Serial1.print(F("AT\r\n"));
	SerialUSB.println(Serial1.readString()); Serial1.print(F("at+cops?\r\n"));
	SerialUSB.println(Serial1.readString()); Serial1.print(F("at+qnwinfo\r\n"));
	SerialUSB.println(Serial1.readString()); Serial1.print(F("AT+qmtdisc=0\r\n"));
	SerialUSB.println(Serial1.readString()); Serial1.print(F("AT+QIDNSCFG=1,\"8.8.8.8\",\"8.8.4.4\"\r\n"));
	SerialUSB.println(Serial1.readString()); Serial1.print(F("at+qmtopen=0,\"demo.thingsboard.io\",1883\r\n"));
	SerialUSB.println(Serial1.readString()); Serial1.print(F("at+qmtconn=0,\"demo.thingsboard.io\",\"KD0wEWeMIMrNHFcQngaI\",\"\"\r\n"));
	SerialUSB.println(Serial1.readString()); Serial1.print(F("at+qmtsub=0,1,\"v1/devices/me/rpc/request/+\",2\r\n"));
//	pinMode(A0, INPUT);
//	pinMode(A1, INPUT);
}

void send_mqtt() {
	Serial1.print(F("AT+QMTPUB=0,0,0,0,\"v1/devices/me/telemetry\"\r\n"));
	// Reading temperature or humidity takes about 250 milliseconds!
	// Sensor readings may also be up to 2 seconds 'old' (its a very slow sensor)
	float h = dht.readHumidity();
	// Read temperature as Celsius (the default)
	float t = dht.readTemperature();

	// Check if any reads failed and exit early (to try again).
	if (isnan(h) || isnan(t)) {
		SerialUSB.println("Failed to read from DHT sensor!");
		Serial1.print(F("\x1A"));
		return;
	}

	Serial1.print(F("{\"temperature\":")); //37.00
	//	Serial1.print(analogRead(A0)/10);
	Serial1.print(t);
	Serial1.print(F(",\"humidity\":")); //77.00
	//	Serial1.print(analogRead(A1)/10);
	Serial1.print(h);
	Serial1.print(F("}\x1A"));
}


