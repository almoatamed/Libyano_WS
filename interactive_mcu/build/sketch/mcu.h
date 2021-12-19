#line 1 "/home/salem/catkin_ws/src/interactive_mcu/src/interactive_mcu/mcu.h"
#pragma once
#include <ros.h>
#include <mcu_msgs/mcu_input.h>
// #include <mcu_msgs/mcu_output.h>
#include <status_msgs/imu_msg.h>
#include <status_msgs/status.h>

#include "./pixelgrid/pixelgrid.h"
#include "./led_ring/led_ring.h"
#include "imu/imu.h"
#include "relay/relay.h"
#include "temperature_and_humidity/temperature_and_humedity.h"
#include "touch/touch.h"
// #include "ultrasonic/ultrasonic.h"
#include "servo/servo.h"
#include "./led_strip/led_strip.h"

///////////////////////////// CONTROLS /////////////////////////////////////////////

#define CONTROL_BASE_ELEMENT 20

#define PIXEL_ELEMENT CONTROL_BASE_ELEMENT +2
#define PIXEL_SET_FACE 64
#define PIXEL_SET_COLOR 65
#define PIXEL_SET_BRIGHTNESS 66

#define RING_ELEMENT CONTROL_BASE_ELEMENT +4
#define RING_SET_FLOW 64
#define RING_SET_COLOR 65
#define RING_SET_BRIGHTNESS 66

#define PIXEL_STRIP_ELEMENT CONTROL_BASE_ELEMENT +5
#define PIXEL_STRIP_SET_COLOR 65
#define PIXEL_STRIP_SET_DEFAULT 67

#define RELAY_ELEMENT CONTROL_BASE_ELEMENT +1
#define RELAY_SET_PART_BASE 10
#define NUMBER_OF_FANS 3
#define NUMBER_OF_CASH_READERS 1
#define NUMBER_OF_RELAYS NUMBER_OF_FANS + NUMBER_OF_CASH_READERS

#define SERVO_ELEMENT CONTROL_BASE_ELEMENT + 3
#define SERVO_SET_ANGLES 11
#define SERVO_FACE_FRONT 12
#define SERVO_INIT 13

/////////////////////////////// SENSORS ////////////////////////////////////////////

#define SENSORS_ELEMENT_BASE 10

#define TOUCH_ELEMENT SENSORS_ELEMENT_BASE+1

// #define ULTRASONIC_ELEMENT SENSORS_ELEMENT_BASE+2

#define TEMP_ELEMENT SENSORS_ELEMENT_BASE+3

#define HUMIDITY_ELEMENT SENSORS_ELEMENT_BASE+4

#define IMU_ELEMENT SENSORS_ELEMENT_BASE+5
#define BNO055_PART_BASE 10
#define BNO055_PART_STATUS BNO055_PART_BASE+0
#define BNO055_PART_ACCELERATION BNO055_PART_BASE+1
#define BNO055_PART_LINEAR_ACCELERATION BNO055_PART_BASE+2
#define BNO055_PART_GYROSCOPE BNO055_PART_BASE+3
#define BNO055_PART_GRAVITY BNO055_PART_BASE+4
#define BNO055_PART_GEOMAGNATIC BNO055_PART_BASE+5
#define BNO055_PART_EULAR BNO055_PART_BASE+6
#define BNO055_PART_QUATERNION BNO055_PART_BASE+7
#define BMP280_PART_BASE 20
#define BMP280_PART_STATUS BMP280_PART_BASE + 0
#define BMP280_PART_TEMP BMP280_PART_BASE + 1
#define BMP280_PART_PRESSURE BMP280_PART_BASE + 2
#define BMP280_PART_ALTITUDE BMP280_PART_BASE + 3

///////////////////////////////////////////////////////////////////////////



class Mcu{
    public:
        ros::Subscriber<mcu_msgs::mcu_input, Mcu> input_;
        ros::Publisher output_;
        status_msgs::status output_msg_;

        Led_strip led_strip_controller_;
        PixelController pixel_controller_;
        RingController ring_controller_;
        Imu imu_controller_;
        RelayController relay_controller_;
        TemperatureAndHumidity t_and_h_controller_;
        Touch touch_controller_;
        // Ultrasonic ultrasonic_controller_;
        ServoMotors servos_;

        Mcu(): input_("mcu/interactive/input", &Mcu::cb_,this), 
               output_("mcu/interactive/output", &output_msg_),
               pixel_controller_(),
               ring_controller_(),
               imu_controller_(),
               relay_controller_(),
               servos_(),
               led_strip_controller_()
        {}

        void init(ros::NodeHandle& nh);
        void read_();
        void cb_(const mcu_msgs::mcu_input& msg);
        void publish_();
        void run();

};