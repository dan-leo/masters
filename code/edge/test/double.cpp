// Demo of avr-libc dtostrf() and dtostre()
//
// davekw7x

#include <Arduino.h>

void setup()
{
   Serial.begin(115200);

   float x = -1.23456;
   byte precision = 4;  // Number of digits after the decimal point

   // Make room for your floating point number, however you
   // plan to format it.
   char floatBuffer[20];

   // Make room for entire print line, however long you plan
   // to make it.
   char printBuffer[80];

   // Width of floating point field includes places for
   //
   // The sign
   // One digit before the decimal point
   // The decimal point
   // Digits after decimal point (== precision)
   // (Don't forget that the buffer has to hold the
   //  terminating zero byte.)

   // Bottom line: The size of floatBuffer must be at least
   // precision+4.  The "width" field in the call do
   // dtostrf should be at least precision plus 3 and at most
   // the size of floatBuffer minus 1
   //
   dtostrf(x, precision+3, precision, floatBuffer);

   // You could just print the raw value.  (You might
   // have other Serial.print() statements to give it some
   // user-friendly context.)
   Serial.println(floatBuffer);


   // Or you could use sprintf to create an entire line in a
   // different buffer.  Then you could use Serial.print
   // or LiquidCrystal::print, or whatever, to emit
   // the whole enchilada in one statement.
   sprintf(printBuffer, "With %%.%df precision, x = %s", precision, floatBuffer);
   Serial.println(printBuffer);


   // Width of scientific field includes places for
   //
   // The sign.
   // One decimal digit before the decimal point.
   // The decimal point.
   // Some digits ofter the decimal point (== precision).
   // The 'e' character for exponent.
   // The sign of the exponent.
   // Two places for the exponent value.
   // (Don't forget that the buffer has to hold the
   //  terminating zero byte.)

   // Bottom line: The size of floatBuffer must be at least
   // precision + 8
   //

   // Print out just the value
   dtostre(x, floatBuffer, precision, NULL);
   Serial.println(floatBuffer);

   // Print out the value with some other stuff from sprintf
   sprintf(printBuffer,"With %%.%de precision, x = %s", precision, floatBuffer);
   Serial.println(printBuffer);

}

void loop()
{
}