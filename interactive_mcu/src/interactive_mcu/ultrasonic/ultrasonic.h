#pragma once

typedef const uint8_t cu8;
typedef uint8_t u8;

cu8 ULTRASONIC_BASE_PIN = 29;
cu8 ULTRASONIC_END_PIN = 40;

cu8 ULTRASONICS_NUMBER = (ULTRASONIC_END_PIN - ULTRASONIC_BASE_PIN + 1)/2;

class Ultrasonic{
    public:        
        uint16_t readings[ULTRASONICS_NUMBER];

        void init(){
            for(u8 i=ULTRASONIC_BASE_PIN; i<=ULTRASONIC_END_PIN; i++){
                pinMode(i,i%2 == 0? INPUT: OUTPUT);
            }
            for(u8 i=0; i<ULTRASONICS_NUMBER;i++){
                this->readings[i] = 0;
            }
        }

        long read_(u8 ultrasonicNumber){
            long duration;
            u8 ultrasonic_trigger_pin  = ULTRASONIC_BASE_PIN + 2*(ultrasonicNumber-1);    
            u8 ultrasonic_echo_pin  = ULTRASONIC_BASE_PIN + 2*(ultrasonicNumber-1) + 1;
            digitalWrite(ultrasonic_trigger_pin, LOW);  
            delayMicroseconds(2); 
            digitalWrite(ultrasonic_trigger_pin, HIGH);
            delayMicroseconds(10); 
            digitalWrite(ultrasonic_trigger_pin, LOW);
            duration = pulseIn(ultrasonic_echo_pin, HIGH,100);
            return (duration/2) / 29.1;
        }

        void readall(){
            for(int i = 1; i<=ULTRASONICS_NUMBER;i++){
                this->readings[i-1] = uint16_t(this->read_(i));
                // this->readings[i-1] = 1;
            }
        }
};
