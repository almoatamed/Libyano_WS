/* 
 * rosserial Subscriber Example
 * Blinks an LED on callback
 */

#include <ros.h>
#include <geometry_msgs/Vector3.h>

ros::NodeHandle  nh;

const uint8_t redDefault = 149;
const uint8_t greenDefault = 27;
const uint8_t blueDefault = 129;

const uint8_t redPin = 10;
const uint8_t greenPin = 9;
const uint8_t bluePin = 11;

void setColor_(uint8_t red, uint8_t green, uint8_t blue)
{
    analogWrite(redPin, red);
    analogWrite(greenPin, green);
    analogWrite(bluePin, blue);
}
void messageCb( const geometry_msgs::Vector3& toggle_msg){
  setColor_(uint8_t(toggle_msg.x),uint8_t(toggle_msg.y),uint8_t(toggle_msg.z));   // blink the led
}

ros::Subscriber<geometry_msgs::Vector3> sub("led_strip", &messageCb );

void setup()
{ 
  pinMode(redPin, OUTPUT);   
  pinMode(greenPin, OUTPUT);
  pinMode(bluePin, OUTPUT);
  setColor_(redDefault,greenDefault,blueDefault);
  nh.initNode();
  nh.subscribe(sub);
}

void loop()
{  
  nh.spinOnce();
  delay(1);
}

