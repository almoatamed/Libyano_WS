#include "mcu.h"

ros::NodeHandle nh;
Mcu mcu;

void setup(){
    nh.getHardware()->setBaud(115200); // set baud rate to 115200
    nh.initNode();              
    mcu.init(nh);
}

void loop(){
  mcu.run();
}