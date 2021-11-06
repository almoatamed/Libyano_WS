#include <Arduino.h>
#line 1 "/home/salem/catkin_ws/src/interactive_mcu_2/src/interactive_mcu_2/interactive_mcu_2.ino"
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

const uint8_t redPin = 9;
const uint8_t greenPin = 10;
const uint8_t bluePin = 11;

#line 19 "/home/salem/catkin_ws/src/interactive_mcu_2/src/interactive_mcu_2/interactive_mcu_2.ino"
void setColor_(uint8_t red, uint8_t green, uint8_t blue);
#line 25 "/home/salem/catkin_ws/src/interactive_mcu_2/src/interactive_mcu_2/interactive_mcu_2.ino"
void messageCb( const geometry_msgs::Vector3& toggle_msg);
#line 31 "/home/salem/catkin_ws/src/interactive_mcu_2/src/interactive_mcu_2/interactive_mcu_2.ino"
void setup();
#line 41 "/home/salem/catkin_ws/src/interactive_mcu_2/src/interactive_mcu_2/interactive_mcu_2.ino"
void loop();
#line 19 "/home/salem/catkin_ws/src/interactive_mcu_2/src/interactive_mcu_2/interactive_mcu_2.ino"
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
  pinMode(redPin, OUTPUT);    //Init Arduino driving pins
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


#line 1 "/home/salem/catkin_ws/src/interactive_mcu_2/src/interactive_mcu_2/mcu.ino"
#include "mcu.h"

void Mcu::init(ros::NodeHandle& nh){
    this->led_strip_controller_.init();

    nh.subscribe(this->input_);
}


void Mcu::cb_(const geometry_msgs::Vector3& msg){
    this->led_strip_controller_.setColor(uint8_t(msg.x),uint8_t(msg.y), uint8_t(msg.z)); // 0 is face 1 is color

}

void Mcu::run(){
}
