/*
 * fusion.h
 *
 *  Created on: 14 Nov 2018
 *      Author: d7rob
 */

#ifndef LIBRARIES_FUSION_FUSION_H_
#define LIBRARIES_FUSION_FUSION_H_

#include <Arduino.h>

#include "DHT.h"
extern DHT dht;

void setup_mqtt();
void send_mqtt();

#endif /* LIBRARIES_FUSION_FUSION_H_ */
