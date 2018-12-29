#include <fusion.h>

#define pinDHT    2
#define pinBuzzer 3
#define pinButton 4
#define pinLED    13

boolean AT_enable = true;
boolean AT_REPLY_enable = true;
//boolean MURATA_REPLY_enable = true;
boolean SERIAL_REPLY_enable = true;
boolean PING_enabled = false;
boolean MQTT_enabled = true;

int led_state = LOW;
int button_state = LOW;
int prev_button_state = LOW;

String str_quec = "";


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
  pinMode(pinBuzzer, OUTPUT);
  pinMode(pinButton, INPUT_PULLUP);
  digitalWrite(pinBuzzer, HIGH);
//  delay(10);
  digitalWrite(pinBuzzer, LOW);

  Serial.begin(115200);
  Serial1.begin(115200);
  //  Serial2.begin(115200);
//  while (!SerialUSB);
  SerialUSB.begin(115200);
//  // Assign pins RX & TX SERCOM functionality
//  pinPeripheral(PIN_SERIAL2_RX, PIO_SERCOM);
//  pinPeripheral(PIN_SERIAL2_TX, PIO_SERCOM);

  dht.begin();

  Serial.println(F("READY"));

  setup_mqtt();

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
//	String str_quec = Serial1.readStringUntil('\n');
//	int c_mura = Serial2.read();
	int c_ser = Serial.read();
	if (c_ser > 0) {
		Serial.write(c_ser);
		SerialUSB.write(c_ser);
		if (c_ser == '!') AT_enable = !AT_enable;
		if (c_ser == '@') AT_REPLY_enable = !AT_REPLY_enable;
//		if (c_ser == ')') MURATA_REPLY_enable = !MURATA_REPLY_enable;
		if (c_ser == '#') SERIAL_REPLY_enable = !SERIAL_REPLY_enable;
		if (c_ser == '$') PING_enabled = !PING_enabled;
		if (c_ser == '%') MQTT_enabled = !MQTT_enabled;

		if (AT_enable) {
			//SerialUSB.write(c_usb);
//			Serial.write(c_usb);
			Serial1.write(c_ser);
//			Serial2.write(c_usb);
		}
	}
	if (c_quec > 0) {
		str_quec.concat((char)c_quec);
		if (c_quec == '\n') {
			if (AT_REPLY_enable) Serial.print(str_quec);
			if (str_quec.indexOf(F("+QMTRECV")) >= 0){
				if (str_quec.indexOf(F("setLED")) > 0) {
					int p = str_quec.indexOf(F("params"));
					if (p > 0) {
						String str_bool = str_quec.substring(p + 8, str_quec.indexOf('}'));
						if (str_bool.equals("true")) led_state = HIGH;
						else if (str_bool.equals("false")) led_state = LOW;
						digitalWrite(LED_BUILTIN, led_state);
					}
				}
				if (str_quec.indexOf(F("setBuzzer")) > 0) {
					int p = str_quec.indexOf(F("params"));
					if (p > 0) {
						String str_bool = str_quec.substring(p + 8, str_quec.indexOf('}'));
						if (str_bool.equals("true")) digitalWrite(pinBuzzer, HIGH);
						else if (str_bool.equals("false")) digitalWrite(pinBuzzer, LOW);
					}
				}
			}
			str_quec = "";
		}
	}

//	if (c_mura > 0) {
//		if (MURATA_REPLY_enable) SerialUSB.write(c_mura);
//	}
	if (c_usb > 0) {
		if (SERIAL_REPLY_enable) Serial.write(c_usb);
		SerialUSB.write(c_usb);
	}

	button_state = digitalRead(pinButton);
	if (button_state != prev_button_state) {
		prev_button_state = button_state;
		send_mqtt_button(button_state);
	}

	static unsigned long ms = millis();
	if (millis() - ms > 5000) {
		ms = millis();
		if (PING_enabled) Serial1.print(F("AT+QPING=1,\"1.1.1.1\",1,1\r\n"));
		if (MQTT_enabled) {
			send_mqtt();
		}
	}
}

/*
 *
at+qmtsub=0,4,"v1/devices/me/rpc/request/+",2

OK

+QMTSUB: 0,4,0,1
AT+QMTPUB=0,0,0,0,"v1/devices/me/telemetry"

> {"temperature":36.00,"humidity":78.00}

OK

+QMTPUB: 0,0,0

+QMTRECV: 0,1,"v1/devices/me/rpc/request/11","{"method":"setValue","params":true}"

+QMTRECV: 0,2,"v1/devices/me/rpc/request/12","{"method":"setValue","params":false}"

+QMTRECV: 0,3,"v1/devices/me/rpc/request/13","{"method":"setValue","params":true}"

+QMTRECV: 0,4,"v1/devices/me/rpc/request/14","{"method":"setValue","params":false}"







+QMTPUB: 0,0,0

AT+QMTPUB=0,0,0,0,"v1/devices/me/telemetry"


> {"temperature":22.03,"humidity":68.00,"analogRead":39}

OK




+QMTPUB: 0,0,0




+QMTRECV: 0,18,"v1/devices/me/rpc/request/47","{"method":"checkButton"}"

AT+QMTPUB=0,0,0,0,"v1/devices/me/telemetry"


> {"temperature":22.03,"humidity":68.00,"analogRead":39}

OK




+QMTPUB: 0,0,0

AT+QMTPUB=0,0,0,0,"v1/devices/me/telemetry"


> {"temperature":22.03,"humidity":68.00,"analogRead":39}

OK

 *
 */
