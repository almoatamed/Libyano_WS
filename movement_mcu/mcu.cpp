#include "mcu.h"

void Mcu::cmd_vel_cb_(const geometry_msgs::Twist& msg){
    this->demandx = msg.linear.x;
    this->demandz = msg.angular.z;
}

void Mcu::operation_state_control_cb_(const mcu_msgs::mcu_input& msg){
    this->control_msg_.Element = msg.Element;
    // this->control_msg_.Part_and_function = msg.Part_and_function;
    // this->control_msg_.values = msg.values;
    // this->control_msg_.values_length = msg.values_length;
}

void Mcu::read_(){
    this->driver_state_.system.voltage = this->odrive_.get_voltage();
    delay(3);
    // this->system_error = this->odrive_.get_system_errors();
    // this->driver_state_.system.error = &this->system_error[0];
    // delay(3);
    this->axis0_error = this->odrive_.get_axis_error(0);
    delay(3);
    this->driver_state_.axis0.error = &this->axis0_error[0];
    this->axis1_error = this->odrive_.get_axis_error(1);
    delay(3);
    this->driver_state_.axis1.error = &this->axis1_error[0];
    this->encoder0_error = this->odrive_.get_encoder_error(0);
    delay(3);
    this->driver_state_.axis0.encoder.error = &this->encoder0_error[0];
    this->encoder1_error = this->odrive_.get_encoder_error(1);
    delay(3);
    this->driver_state_.axis1.encoder.error = &this->encoder1_error[0];
    this->driver_state_.axis0.encoder.pos = this->odrive_.get_pos(0);
    delay(3);
    this->driver_state_.axis1.encoder.pos = this->odrive_.get_pos(1);
    delay(3);
    this->driver_state_.axis0.encoder.vel = this->odrive_.get_vel(0);
    delay(3);
    this->driver_state_.axis1.encoder.vel = this->odrive_.get_vel(1);
    delay(3);
    this->motor0_error = this->odrive_.get_motor_error(0);
    this->driver_state_.axis0.motor.error = &motor0_error[0];
    delay(3);
    this->motor1_error = this->odrive_.get_motor_error(1);
    this->driver_state_.axis1.motor.error = &motor1_error[0];
    delay(3);
    this->driver_state_.axis0.motor.phase_inductance = this->odrive_.get_motor_phase_inductance(0);
    delay(3);
    this->driver_state_.axis1.motor.phase_inductance = this->odrive_.get_motor_phase_inductance(1);
    delay(3);
    this->driver_state_.axis0.motor.phase_resistance = this->odrive_.get_motor_phase_resistance(0);
    delay(3);
    this->driver_state_.axis1.motor.phase_resistance = this->odrive_.get_motor_phase_resistance(1);
    delay(3);
}

void Mcu::set_vel_(){
    this->forward0_ = this->demandx /WHEEL_CIRCUMFERENSE_M; // convert m/s into turn/s
    this->forward1_ = this->demandx /WHEEL_CIRCUMFERENSE_M; // convert m/s into turn/s

    this->turn0_ = this->demandz /(TWO_PI); // convert rads/s into turn/s
    this->turn1_ = this->demandz /(TWO_PI); // convert rads/s into turn/s
    this->forward1_ = this->forward1_ * -1; // one motor and encoder is mounted facing the other way

    this->odrive_.set_vel(0, this->forward0_ - this->turn0_);  
    this->odrive_.set_vel(1, this->forward1_ - this->turn1_);
}

void Mcu::estimate_pos_(){
    this->pos1_ = (this->odrive_.get_pos(0));
    this->pos0_ = (this->odrive_.get_pos(1)) * -1;
    this->pos0_diff_ = this->pos0_ - this->pos0_old_;
    this->pos1_diff_ = this->pos1_ - this->pos1_old_;
    this->pos0_old_ = this->pos0_;
    this->pos1_old_ = this->pos1_;
    // calc m from turn 
    this->pos0_m_diff_ = this->pos0_diff_ * WHEEL_CIRCUMFERENSE_M;
    this->pos1_m_diff_ = this->pos1_diff_ * WHEEL_CIRCUMFERENSE_M;

    // calc distance travelled based on average of both wheels
    this->pos_average_m_diff_ = (this->pos0_m_diff_ + this->pos1_m_diff_) / 2.0; // difference in each cycle
    this->pos_total_m_ += this->pos_average_m_diff_;                     // calc total running total distance

    // calc angle or rotation to broadcast with tf
    this->theta_ += (this->pos1_m_diff_ - this->pos0_m_diff_)/(WHEEL_AXIS_LENGTH_M/2.0); // rad
    if (this->theta_ > PI)
      this->theta_ -= TWO_PI;
    if (this->theta_ < (-PI))
      this->theta_ += TWO_PI;

      
    this->y_ += this->pos_average_m_diff_ * sin(this->theta_);
    this->x_ += this->pos_average_m_diff_ * cos(this->theta_);

    this->t_.transform.translation.x = this->x_;
    this->t_.transform.translation.y = this->y_;
    this->t_.transform.translation.z = 0;
    this->t_.transform.rotation = tf::createQuaternionFromYaw(this->theta_);
    this->t_.header.stamp = this->nh.now();

    this->odom_msg_.header.stamp = this->nh.now();
    this->odom_msg_.pose.pose.position.x = this->x_;
    this->odom_msg_.pose.pose.position.y = this->y_;
    this->odom_msg_.pose.pose.position.z = 0.0;
    this->odom_msg_.pose.pose.orientation = tf::createQuaternionFromYaw(this->theta_);
    this->odom_msg_.twist.twist.linear.x = ((this->pos0_m_diff_ + this->pos1_m_diff_) / 2.0) / (LOOPTIME*1.0e-3);
    this->odom_msg_.twist.twist.linear.y = 0.0;
    this->odom_msg_.twist.twist.angular.z = ((this->pos1_m_diff_ - this->pos0_m_diff_) / (WHEEL_AXIS_LENGTH_M/2.0))/(LOOPTIME*1.0e-3) ;
}

void Mcu::pub_(){
    // this->odom_pub_.publish(&this->odom_msg_);
    this->status_pub_.publish(&this->driver_state_);
    // this->tf_broadcaster_.sendTransform(this->t_);
}

void Mcu::init(ros::NodeHandle& nh){
    this->t_.header.frame_id = ODOM_FRAME;
    this->t_.child_frame_id = BASE_LINK_FRAME;
    this->odom_msg_.header.frame_id = ODOM_FRAME;
    this->odom_msg_.child_frame_id = BASE_LINK_FRAME;
    this->nh = nh;
    this->nh.advertise(this->odom_pub_);
    this->nh.advertise(this->status_pub_);
    this->nh.subscribe(this->cmd_vel_sub_);
    this->nh.subscribe(this->operation_state_control_sub_);
    Serial1.begin(115200); // ODrive
    this->tf_broadcaster_.init(this->nh);
    this->odrive_.reboot();
    this->prepare_driver_();
}

void Mcu::prepare_driver_(){
    this->odrive_.clear_errors();
    delay(3);
    this->requested_state_ = ODriveArduino::AXIS_STATE_CLOSED_LOOP_CONTROL;
    this->odrive_.run_state(0, this->requested_state_, false); // don't wait 
    delay(3);
    this->requested_state_ = ODriveArduino::AXIS_STATE_CLOSED_LOOP_CONTROL;
    this->odrive_.run_state(1, this->requested_state_, false); // don't wait 
    delay(3);
}

void Mcu::run(){
    this->nh.spinOnce();
    this->currentMillis_ = millis();
    if(this->currentMillis_ - this->previousMillis_ >= LOOPTIME){
        this->previousMillis_ = this->currentMillis_;
        switch (this->control_msg_.Element)
        {
        case REBOOT:
            this->odrive_.reboot();
            this->prepare_driver_();
            this->control_msg_.Element = 0;
            break;
        case REINIT:
            this->prepare_driver_();
            this->control_msg_.Element = 0;
            break;
        default:
            this->set_vel_();
            // this->estimate_pos_();
            this->read_();
            this->pub_();
            break;
        }
    }
}