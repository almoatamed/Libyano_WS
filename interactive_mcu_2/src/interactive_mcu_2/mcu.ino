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