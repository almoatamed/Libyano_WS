// #include "ultrasonic.h"

// typedef uint8_t u8;

// void Ultrasonic::init(){
//     for(u8 i=ULTRASONIC_BASE_PIN; i<=ULTRASONIC_END_PIN; i++){
//         pinMode(i,i%2 == 0? INPUT: OUTPUT);
//     }
//     for(u8 i=0; i<ULTRASONICS_NUMBER;i++){
//         this->readings[i] = 0;
//     }
// }

// long Ultrasonic::read_(u8 ultrasonicNumber){
//     long duration;
//     u8 ultrasonic_trigger_pin  = ULTRASONIC_BASE_PIN + 2*(ultrasonicNumber-1);    
//     u8 ultrasonic_echo_pin  = ULTRASONIC_BASE_PIN + 2*(ultrasonicNumber-1) + 1;
//     digitalWrite(ultrasonic_trigger_pin, LOW);  
//     delayMicroseconds(2); 
//     digitalWrite(ultrasonic_trigger_pin, HIGH);
//     delayMicroseconds(10); 
//     digitalWrite(ultrasonic_trigger_pin, LOW);
//     duration = pulseIn(ultrasonic_echo_pin, HIGH);
//     return (duration/2) / 29.1;
// }

// void Ultrasonic::readall(){
//     for(int i = 1; i<=ULTRASONICS_NUMBER;i++){
//         this->readings[i-1] = this->read_(i);
//     }
// }