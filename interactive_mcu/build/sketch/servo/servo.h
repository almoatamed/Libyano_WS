#line 1 "/home/salem/catkin_ws/src/interactive_mcu/src/interactive_mcu/servo/servo.h"
#include <Herkulex.h>
#include <status_msgs/servo_msg.h>

#pragma once

typedef uint8_t u8;

#define SERVO_BAUD_RATE 115200

#define SERVO_VERTICAL_CENTER 0
#define SERVO_HORIZENTAL_CENTER 0


#define SERVO_HORIZENTAL 1
#define SERVO_VERTICAL_L 4
#define SERVO_VERTICAL_R 2

#define NUMBER_OF_SERVOS 3

const int VERTICAL_BOUNDRIES[3] = {-15,0,15} ;
const int HORIZENTAL_BOUNDRIES[3] = {-45,0,45} ;


class ServoMotors
{
    public:
        
        status_msgs::servo_msg servos[NUMBER_OF_SERVOS];

        void init(){
            Herkulex.beginSerial1(115200); //open serial port 1
            Herkulex.reboot(SERVO_HORIZENTAL);
            delay(1000);
            Herkulex.reboot(SERVO_VERTICAL_L);
            delay(1000);
            Herkulex.reboot(SERVO_VERTICAL_R);
            delay(1000);
            Herkulex.initialize();
            this->face_center();
            delay(100);
        }

        int get_angl(u8 servo_id){
            return (int)Herkulex.getAngle(servo_id);
        }

        void reinit(){
            // Herkulex.end();
            // delay(1);
            this->init();
        }

        void readall(){
            // Herkulex.initialize();
            servos[0].angle = Herkulex.getAngle(SERVO_HORIZENTAL);
            delay(1);
            servos[0].stat = Herkulex.stat(SERVO_HORIZENTAL);
            delay(1);
            servos[1].angle = Herkulex.getAngle(SERVO_VERTICAL_R);
            delay(1);
            servos[1].stat = Herkulex.stat(SERVO_VERTICAL_R);
            delay(1);
            servos[2].angle = Herkulex.getAngle(SERVO_VERTICAL_L);
            delay(1);
            servos[2].stat = Herkulex.stat(SERVO_VERTICAL_L);
        }

        void prepare(){
            Herkulex.initialize();
            delay(1);
        }

        void face_center(int time=700){
            this->prepare();
            Herkulex.moveAllAngle(SERVO_HORIZENTAL,(int)HORIZENTAL_BOUNDRIES[1],0x01);
            delay(1);
            Herkulex.moveAllAngle(SERVO_VERTICAL_R,(int)VERTICAL_BOUNDRIES[1],0x03);
            delay(1);
            Herkulex.moveAllAngle(SERVO_VERTICAL_L,-(int)VERTICAL_BOUNDRIES[1],0x02);
            delay(1);
            Herkulex.actionAll(time);
        }
        
        int timeout = 700;
        void move(float *angles){
            this->timeout = int(angles[2]);
            Herkulex.initialize();
            if((angles[0]<HORIZENTAL_BOUNDRIES[0] || angles[0]>HORIZENTAL_BOUNDRIES[2]) || (angles[1]<VERTICAL_BOUNDRIES[0] || angles[1]>VERTICAL_BOUNDRIES[2])){
                return;
            }
            Herkulex.moveAllAngle(SERVO_HORIZENTAL,(int)angles[0],0x01);
            delay(1);
            Herkulex.moveAllAngle(SERVO_VERTICAL_R,-(int)angles[1],0x03);
            delay(1);
            Herkulex.moveAllAngle(SERVO_VERTICAL_L,(int)angles[1],0x02);
            delay(1);
            Herkulex.actionAll(this->timeout);
            
        }



};
