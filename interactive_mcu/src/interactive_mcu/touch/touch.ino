// #include "touch.h"

// typedef uint8_t u8;

// void Touch::init(){
//     for(u8 i=TOUCH_BASE_PIN; i<=TOUCH_END_PIN; i++){
//         pinMode(i,INPUT);
//     }
//     for(u8 i=0; i<TOUCHS_NUMBER;i++){
//         this->readings[i] = 0;
//     }
// }

// u8 Touch::read_(u8 touchNumber){
//     return digitalRead(TOUCH_BASE_PIN + (touchNumber -1));
// }
// void Touch::readall(){
//     for(int i = 1; i<=TOUCHS_NUMBER;i++){
//         this->readings[i-1] = this->read_(i);
//     }
// }