#define USE_USBCON
#include "mcu.h"


ros::NodeHandle nh;

Mcu mcu;

void setup(){
    nh.initNode();
    mcu.init(nh);
}


void loop()
{
  mcu.run();
  nh.spinOnce();
}