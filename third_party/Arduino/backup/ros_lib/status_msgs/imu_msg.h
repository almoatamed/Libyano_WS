#ifndef _ROS_status_msgs_imu_msg_h
#define _ROS_status_msgs_imu_msg_h

#include <stdint.h>
#include <string.h>
#include <stdlib.h>
#include "ros/msg.h"
#include "status_msgs/bmp280_chip.h"
#include "status_msgs/bno055_chip.h"

namespace status_msgs
{

  class imu_msg : public ros::Msg
  {
    public:
      typedef status_msgs::bmp280_chip _bmp280_type;
      _bmp280_type bmp280;
      typedef status_msgs::bno055_chip _bno055_type;
      _bno055_type bno055;

    imu_msg():
      bmp280(),
      bno055()
    {
    }

    virtual int serialize(unsigned char *outbuffer) const
    {
      int offset = 0;
      offset += this->bmp280.serialize(outbuffer + offset);
      offset += this->bno055.serialize(outbuffer + offset);
      return offset;
    }

    virtual int deserialize(unsigned char *inbuffer)
    {
      int offset = 0;
      offset += this->bmp280.deserialize(inbuffer + offset);
      offset += this->bno055.deserialize(inbuffer + offset);
     return offset;
    }

    const char * getType(){ return "status_msgs/imu_msg"; };
    const char * getMD5(){ return "63af3dbe6d7b11d96dd971c25984070f"; };

  };

}
#endif
