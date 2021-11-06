#ifndef _ROS_status_msgs_servo_msg_h
#define _ROS_status_msgs_servo_msg_h

#include <stdint.h>
#include <string.h>
#include <stdlib.h>
#include "ros/msg.h"

namespace status_msgs
{

  class servo_msg : public ros::Msg
  {
    public:
      typedef uint8_t _stat_type;
      _stat_type stat;
      typedef int16_t _angle_type;
      _angle_type angle;

    servo_msg():
      stat(0),
      angle(0)
    {
    }

    virtual int serialize(unsigned char *outbuffer) const
    {
      int offset = 0;
      *(outbuffer + offset + 0) = (this->stat >> (8 * 0)) & 0xFF;
      offset += sizeof(this->stat);
      union {
        int16_t real;
        uint16_t base;
      } u_angle;
      u_angle.real = this->angle;
      *(outbuffer + offset + 0) = (u_angle.base >> (8 * 0)) & 0xFF;
      *(outbuffer + offset + 1) = (u_angle.base >> (8 * 1)) & 0xFF;
      offset += sizeof(this->angle);
      return offset;
    }

    virtual int deserialize(unsigned char *inbuffer)
    {
      int offset = 0;
      this->stat =  ((uint8_t) (*(inbuffer + offset)));
      offset += sizeof(this->stat);
      union {
        int16_t real;
        uint16_t base;
      } u_angle;
      u_angle.base = 0;
      u_angle.base |= ((uint16_t) (*(inbuffer + offset + 0))) << (8 * 0);
      u_angle.base |= ((uint16_t) (*(inbuffer + offset + 1))) << (8 * 1);
      this->angle = u_angle.real;
      offset += sizeof(this->angle);
     return offset;
    }

    const char * getType(){ return "status_msgs/servo_msg"; };
    const char * getMD5(){ return "1bc889d94917d5f567fccfd49ffc0460"; };

  };

}
#endif
