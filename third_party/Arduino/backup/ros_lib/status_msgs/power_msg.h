#ifndef _ROS_status_msgs_power_msg_h
#define _ROS_status_msgs_power_msg_h

#include <stdint.h>
#include <string.h>
#include <stdlib.h>
#include "ros/msg.h"

namespace status_msgs
{

  class power_msg : public ros::Msg
  {
    public:
      typedef uint8_t _battery_type;
      _battery_type battery;
      typedef uint8_t _charging_status_type;
      _charging_status_type charging_status;

    power_msg():
      battery(0),
      charging_status(0)
    {
    }

    virtual int serialize(unsigned char *outbuffer) const
    {
      int offset = 0;
      *(outbuffer + offset + 0) = (this->battery >> (8 * 0)) & 0xFF;
      offset += sizeof(this->battery);
      *(outbuffer + offset + 0) = (this->charging_status >> (8 * 0)) & 0xFF;
      offset += sizeof(this->charging_status);
      return offset;
    }

    virtual int deserialize(unsigned char *inbuffer)
    {
      int offset = 0;
      this->battery =  ((uint8_t) (*(inbuffer + offset)));
      offset += sizeof(this->battery);
      this->charging_status =  ((uint8_t) (*(inbuffer + offset)));
      offset += sizeof(this->charging_status);
     return offset;
    }

    const char * getType(){ return "status_msgs/power_msg"; };
    const char * getMD5(){ return "8ca5d28a319ff1f42c9092793089aac8"; };

  };

}
#endif
