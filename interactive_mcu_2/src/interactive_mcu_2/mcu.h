#pragma once
#include <ros.h>
#include <geometry_msgs/Vector3.h>
#include "./led_strip/led_strip.h"

///////////////////////////// CONTROLS /////////////////////////////////////////////

#define CONTROL_BASE_ELEMENT 20

#define PIXEL_STRIP_ELEMENT CONTROL_BASE_ELEMENT +5
#define PIXEL_STRIP_SET_COLOR 65
#define PIXEL_STRIP_SET_DEFAULT 67

///////////////////////////////////////////////////////////////////////////



class Mcu{
    public:
        ros::Subscriber<geometry_msgs::Vector3, Mcu> input_;

        Led_strip led_strip_controller_;

        Mcu(): input_("mcu/interactive/input2", &Mcu::cb_,this), 
               led_strip_controller_()
        {}

        void init(ros::NodeHandle& nh);
        void read_();
        void cb_(const geometry_msgs::Vector3& msg);
        void run();

};