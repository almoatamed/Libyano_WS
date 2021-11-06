#pragma once

#include "ODriveArduino.h"
#include "ros.h"
#include "geometry_msgs/Twist.h"
#include <ros/time.h>
#include <tf/tf.h>
#include <tf/transform_broadcaster.h>
#include <nav_msgs/Odometry.h>
#include <mcu_msgs/mcu_input.h>
#include <status_msgs/driver_msg.h>

// #define Serial1 Serial1

#define LOOPTIME 100.0f
#define WHEEL_CIRCUMFERENSE_M 0.5186f 
#define WHEEL_AXIS_LENGTH_M 0.30f
 
// frame names 
#define BASE_LINK_FRAME "/base_link";
#define ODOM_FRAME "/odom";

// topic names 
#define CMD_VEL_TOPIC "/cmd_vel"
#define ODOM_TOPIC "/odom"
#define STATUS_TOPIC "/mcu/movement/driver/status"
#define OPERATION_STATE_CONTROL_TOPIC "/mcu/movement/operation_state_control"

// operation states 
#define RUN 0
#define REBOOT 1
#define REINIT 2

class Mcu
{
    public:
        // ROS NH
        ros::NodeHandle nh;
        // ROS terminals
        ros::Subscriber<geometry_msgs::Twist, Mcu> cmd_vel_sub_;
        ros::Subscriber<mcu_msgs::mcu_input, Mcu> operation_state_control_sub_;
        ros::Publisher odom_pub_;        
        // odometry message
        nav_msgs::Odometry odom_msg_;

        ros::Publisher status_pub_;
        status_msgs::driver_msg driver_state_;

        tf::TransformBroadcaster tf_broadcaster_;
        // transformation message uused as translation between dometry frame and base_link frame
        geometry_msgs::TransformStamped t_;

        // brushless wheell driver 
        ODriveArduino odrive_;

        // ###################### driver status string holders ######################################
        String system_error;
        String axis0_error;
        String axis1_error;
        String encoder0_error;
        String encoder1_error;
        String motor0_error;
        String motor1_error;
        
        // ###################### movment calculation variables ######################################


        // cmd_vel variables to be received to drive with
        double demandx;
        double demandz;

        // output variables to drive the ODrive
        double forward0_;
        double forward1_;
        double turn0_;
        double turn1_;

        // timers for the sub-main loop
        unsigned long currentMillis_;
        long previousMillis_; // set up timers

        // axis controller for odrive
        int requested_state_ = 0;
        mcu_msgs::mcu_input control_msg_;
        // position and velocity variables read from the ODrive
        double vel0_;
        double vel1_;
        double pos0_;
        double pos1_;

        // variables to work out the different on each cycle
        float pos0_old_;
        float pos1_old_;
        float pos0_diff_;
        float pos1_diff_;
        float pos0_m_diff_;
        float pos1_m_diff_;
        float pos_average_m_diff_;
        float pos_total_m_;

        // tf variables to be broadcast
        double x_;
        double y_;
        double theta_;


        Mcu(): 
        odrive_(Serial1),
        odom_pub_(ODOM_TOPIC, &odom_msg_),
        status_pub_(STATUS_TOPIC, &driver_state_),
        theta_(0),
        y_(0),
        x_(0),
        previousMillis_(0),
        cmd_vel_sub_(CMD_VEL_TOPIC,&Mcu::cmd_vel_cb_,this),
        operation_state_control_sub_(OPERATION_STATE_CONTROL_TOPIC,&Mcu::operation_state_control_cb_,this)
        {}

        void operation_state_control_cb_(const mcu_msgs::mcu_input& msg);
        void cmd_vel_cb_(const geometry_msgs::Twist& msg);
        
        void init(ros::NodeHandle& nh);
        
        void set_vel_();
        void estimate_pos_();
        void prepare_driver_();

        void read_();
        void pub_();
        void run();

};
