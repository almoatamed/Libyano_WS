#include <Arduino.h>
#line 1 "/home/salem/catkin_ws/src/interactive_mcu/src/interactive_mcu/interactive_mcu.ino"
#define USE_USBCON
#include "mcu.h"


ros::NodeHandle nh;

Mcu mcu;

#line 9 "/home/salem/catkin_ws/src/interactive_mcu/src/interactive_mcu/interactive_mcu.ino"
void setup();
#line 15 "/home/salem/catkin_ws/src/interactive_mcu/src/interactive_mcu/interactive_mcu.ino"
void loop();
#line 9 "/home/salem/catkin_ws/src/interactive_mcu/src/interactive_mcu/interactive_mcu.ino"
void setup(){
    nh.initNode();
    mcu.init(nh);
}


void loop()
{
  mcu.run();
  nh.spinOnce();
}
#line 1 "/home/salem/catkin_ws/src/interactive_mcu/src/interactive_mcu/mcu.ino"
#include "mcu.h"

void Mcu::init(ros::NodeHandle& nh){
    this->pixel_controller_.init();
    this->ring_controller_.init();
    this->led_strip_controller_.init();
    this->imu_controller_.init();
    this->relay_controller_.init();
    this->touch_controller_.init();
    // this->ultrasonic_controller_.init();
    this->servos_.init();

    nh.advertise(this->output_);
    nh.subscribe(this->input_);
}

void Mcu::read_(){
    this->pixel_controller_.run();
    this->ring_controller_.run();
    // this->imu_controller_.run();
    this->t_and_h_controller_.readall();
    this->touch_controller_.readall();
    // this->ultrasonic_controller_.readall();
    this->servos_.readall();
}

void Mcu::cb_(const mcu_msgs::mcu_input& msg){
    switch (msg.Element)
    {

        case PIXEL_ELEMENT:
        {
            switch (msg.Part_and_function)
            {
                case PIXEL_SET_FACE:
                {
                    if(msg.values_length > 4){
                        this->pixel_controller_.set_face(uint8_t(msg.values[0]),uint8_t(msg.values[1]), uint32_t(msg.values[2]), int(msg.values[3]),uint8_t(msg.values[4])); // 0 is face 1 is color
                    }else if(msg.values_length > 3){
                        this->pixel_controller_.set_face(uint8_t(msg.values[0]),uint8_t(msg.values[1]), uint32_t(msg.values[2]), int(msg.values[3])); // 0 is face 1 is color
                    }else if(msg.values_length > 2){
                        this->pixel_controller_.set_face(uint8_t(msg.values[0]),uint8_t(msg.values[1]), uint32_t(msg.values[2])); // 0 is face 1 is color
                    }else if(msg.values_length > 1){
                        this->pixel_controller_.set_face(uint8_t(msg.values[0]),uint8_t(msg.values[1])); // 0 is face 1 is color
                    }else{
                        this->pixel_controller_.set_face(uint8_t(msg.values[0])); // 0 is face 1 is color
                    }
                    break;
                }
                case PIXEL_SET_COLOR:
                { 
                    this->pixel_controller_.set_color(uint32_t(msg.values[0]));
                    break;
                }
                case PIXEL_SET_BRIGHTNESS:
                {
                    this->pixel_controller_.set_brightness(uint8_t(msg.values[0]));
                    break;
                }
                default:
                    break;
            }
            break;
        }
            
        case RING_ELEMENT:
        {
            switch (msg.Part_and_function)
            {
                case RING_SET_FLOW:
                {
                    if(msg.values_length > 4){
                        this->ring_controller_.set_flow(uint8_t(msg.values[0]),uint8_t(msg.values[1]), uint32_t(msg.values[2]), int(msg.values[3]),uint8_t(msg.values[4])); // 0 is face 1 is color
                    }else if(msg.values_length > 3){
                        this->ring_controller_.set_flow(uint8_t(msg.values[0]),uint8_t(msg.values[1]), uint32_t(msg.values[2]), int(msg.values[3])); // 0 is face 1 is color
                    }else if(msg.values_length > 2){
                        this->ring_controller_.set_flow(uint8_t(msg.values[0]),uint8_t(msg.values[1]), uint32_t(msg.values[2])); // 0 is face 1 is color
                    }else if(msg.values_length > 1){
                        this->ring_controller_.set_flow(uint8_t(msg.values[0]),uint8_t(msg.values[1])); // 0 is face 1 is color
                    }else{
                        this->ring_controller_.set_flow(uint8_t(msg.values[0])); // 0 is face 1 is color
                    }
                    break;
                }
                case RING_SET_COLOR:
                { 
                    this->ring_controller_.set_color(uint32_t(msg.values[0]));
                    break;
                }
                case RING_SET_BRIGHTNESS:
                {
                    this->ring_controller_.set_brightness(uint8_t(msg.values[0]));
                    break;
                }
                default:
                    break;
            }
            break;
        }
            
        case PIXEL_STRIP_ELEMENT:
        {
            switch (msg.Part_and_function)
            {
                case PIXEL_STRIP_SET_COLOR:
                {
                    if(msg.values_length > 2){
                        this->led_strip_controller_.setColor(uint8_t(msg.values[0]),uint8_t(msg.values[1]), uint8_t(msg.values[2])); // 0 is face 1 is color
                    }
                    break;
                }
                case PIXEL_STRIP_SET_DEFAULT:
                { 
                    this->led_strip_controller_.setDefaultColor();
                    break;
                }
                default:
                    break;
            }
            break;
        }
       
        case RELAY_ELEMENT:
        {
            switch (10*uint8_t(msg.Part_and_function/10))
            {
                case RELAY_SET_PART_BASE:
                {
                    this->relay_controller_.set(RELAY_PIN_BASE + msg.Part_and_function%RELAY_SET_PART_BASE -1,(uint8_t)msg.values[0]);
                    break;
                }
                default:
                    break;
            }
            break;
        }

        case SERVO_ELEMENT:
        {
            switch (msg.Part_and_function)
            {
                case SERVO_SET_ANGLES:
                {
                    this->servos_.move(msg.values);
                    break;
                }
                case SERVO_FACE_FRONT:
                {
                    this->servos_.face_center();
                    break;
                }
                case SERVO_INIT:
                {
                    this->servos_.reinit();
                    break;
                }
                default:
                    break;
            }
            break;
        }

        default:
            break;
    }
}

void Mcu::publish_(){
    this->output_msg_.controllers.pixelgrid.face = this->pixel_controller_.face;
    this->output_msg_.controllers.pixelgrid.grid_color = this->pixel_controller_.color;
    this->output_msg_.controllers.pixelgrid.is_running = this->pixel_controller_.is_running;
    this->output_msg_.controllers.pixelgrid.brightness = this->pixel_controller_.brighness;

    this->output_msg_.controllers.led_ring.flow = this->ring_controller_.flow;
    this->output_msg_.controllers.led_ring.grid_color = this->ring_controller_.color;
    this->output_msg_.controllers.led_ring.is_running = this->ring_controller_.is_running;
    this->output_msg_.controllers.led_ring.brightness = this->ring_controller_.brighness;

    this->output_msg_.controllers.relays_length = NUMBER_OF_RELAYS;
    uint8_t relays[NUMBER_OF_RELAYS];
    for(uint8_t i; i < NUMBER_OF_RELAYS; i++){
        relays[i] = (uint8_t)this->relay_controller_.get(uint8_t(RELAY_PIN_BASE+i));
    }
    this->output_msg_.controllers.relays = relays;

    this->output_msg_.sensors.humidity = this->t_and_h_controller_.humidity_readings;
    this->output_msg_.sensors.humidity_length = TEMPERATURE_AND_HUMIDITY_NUMBER;

    this->output_msg_.sensors.temp = this->t_and_h_controller_.temperature_readings;
    this->output_msg_.sensors.temp_length = TEMPERATURE_AND_HUMIDITY_NUMBER;
    status_msgs::imu_msg imu_msg[1];

    imu_msg[0].bmp280.status = this->imu_controller_.BMP280_STATUS;
    imu_msg[0].bmp280.pressure = this->imu_controller_.pressure;
    imu_msg[0].bmp280.temp = this->imu_controller_.temp;
    imu_msg[0].bmp280.altitude = float(this->imu_controller_.altitude);

    imu_msg[0].bno055.statsu = this->imu_controller_.BNO055_STATUS;
    imu_msg[0].bno055.acceleration.x = this->imu_controller_.sAccAnalog.x;
    imu_msg[0].bno055.acceleration.y = this->imu_controller_.sAccAnalog.y;
    imu_msg[0].bno055.acceleration.z = this->imu_controller_.sAccAnalog.z;
    imu_msg[0].bno055.linear_acceleration.x = this->imu_controller_.sLiaAnalog.x;
    imu_msg[0].bno055.linear_acceleration.y = this->imu_controller_.sLiaAnalog.y;
    imu_msg[0].bno055.linear_acceleration.z = this->imu_controller_.sLiaAnalog.z;
    imu_msg[0].bno055.gyroscope.x = this->imu_controller_.sGyrAnalog.x;
    imu_msg[0].bno055.gyroscope.y = this->imu_controller_.sGyrAnalog.y;
    imu_msg[0].bno055.gyroscope.z = this->imu_controller_.sGyrAnalog.z;
    imu_msg[0].bno055.geomagnatic.x = this->imu_controller_.sMagAnalog.x;
    imu_msg[0].bno055.geomagnatic.y = this->imu_controller_.sMagAnalog.y;
    imu_msg[0].bno055.geomagnatic.z = this->imu_controller_.sMagAnalog.z;
    imu_msg[0].bno055.gravity.x = this->imu_controller_.sMagAnalog.x;
    imu_msg[0].bno055.gravity.y = this->imu_controller_.sMagAnalog.y;
    imu_msg[0].bno055.gravity.z = this->imu_controller_.sMagAnalog.z;
    imu_msg[0].bno055.quaternion.x = this->imu_controller_.sQuaAnalog.x;
    imu_msg[0].bno055.quaternion.y = this->imu_controller_.sQuaAnalog.y;
    imu_msg[0].bno055.quaternion.z = this->imu_controller_.sQuaAnalog.z;
    imu_msg[0].bno055.quaternion.w = this->imu_controller_.sQuaAnalog.w;
    imu_msg[0].bno055.eular.x= this->imu_controller_.sEulAnalog.pitch;
    imu_msg[0].bno055.eular.y= this->imu_controller_.sEulAnalog.roll;
    imu_msg[0].bno055.eular.z= this->imu_controller_.sEulAnalog.head;
    this->output_msg_.sensors.imu_length = 1;
    this->output_msg_.sensors.imu = imu_msg;
    
    // this->output_msg_.sensors.ultrasonic_length = ULTRASONICS_NUMBER;
    // this->output_msg_.sensors.ultrasonic = this->ultrasonic_controller_.readings;    

    this->output_msg_.sensors.touch = this->touch_controller_.readings;
    this->output_msg_.sensors.touch_length = TOUCHS_NUMBER;    

    this->output_msg_.controllers.servos = this->servos_.servos;
    this->output_msg_.controllers.servos_length = NUMBER_OF_SERVOS;

    this->output_.publish(&this->output_msg_);
    
}

void Mcu::run(){
    this->read_();
    this->publish_();
}
