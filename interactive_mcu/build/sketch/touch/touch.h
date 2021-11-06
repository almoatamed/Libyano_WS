#line 1 "/home/salem/catkin_ws/src/interactive_mcu/src/interactive_mcu/touch/touch.h"
#pragma once

typedef const uint8_t cu8;
typedef uint8_t u8;

cu8 TOUCH_BASE_PIN = 41;
cu8 TOUCH_END_PIN = 47;

cu8 TOUCHS_NUMBER = (TOUCH_END_PIN - TOUCH_BASE_PIN + 1);

class Touch{
    public:        
        u8 readings[TOUCHS_NUMBER];

        void init(){
            for(u8 i=TOUCH_BASE_PIN; i<=TOUCH_END_PIN; i++){
                pinMode(i,INPUT);
            }
            for(u8 i=0; i<TOUCHS_NUMBER;i++){
                this->readings[i] = 0;
            }
        }

        u8 read_(u8 touchNumber){
            return digitalRead(TOUCH_BASE_PIN + (touchNumber -1));
        }

        void readall(){
            for(int i = 1; i<=TOUCHS_NUMBER;i++){
                this->readings[i-1] = this->read_(i);
            }
        }
};
