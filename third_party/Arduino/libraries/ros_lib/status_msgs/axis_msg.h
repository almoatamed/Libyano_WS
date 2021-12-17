#ifndef _ROS_status_msgs_axis_msg_h
#define _ROS_status_msgs_axis_msg_h

#include <stdint.h>
#include <string.h>
#include <stdlib.h>
#include "ros/msg.h"
#include "status_msgs/encoder_msg.h"
#include "status_msgs/motor_msg.h"

namespace status_msgs
{

  class axis_msg : public ros::Msg
  {
    public:
      typedef status_msgs::encoder_msg _encoder_type;
      _encoder_type encoder;
      typedef status_msgs::motor_msg _motor_type;
      _motor_type motor;
      typedef const char* _error_type;
      _error_type error;

    axis_msg():
      encoder(),
      motor(),
      error("")
    {
    }

    virtual int serialize(unsigned char *outbuffer) const
    {
      int offset = 0;
      offset += this->encoder.serialize(outbuffer + offset);
      offset += this->motor.serialize(outbuffer + offset);
      uint32_t length_error = strlen(this->error);
      varToArr(outbuffer + offset, length_error);
      offset += 4;
      memcpy(outbuffer + offset, this->error, length_error);
      offset += length_error;
      return offset;
    }

    virtual int deserialize(unsigned char *inbuffer)
    {
      int offset = 0;
      offset += this->encoder.deserialize(inbuffer + offset);
      offset += this->motor.deserialize(inbuffer + offset);
      uint32_t length_error;
      arrToVar(length_error, (inbuffer + offset));
      offset += 4;
      for(unsigned int k= offset; k< offset+length_error; ++k){
          inbuffer[k-1]=inbuffer[k];
      }
      inbuffer[offset+length_error-1]=0;
      this->error = (char *)(inbuffer + offset-1);
      offset += length_error;
     return offset;
    }

    const char * getType(){ return "status_msgs/axis_msg"; };
    const char * getMD5(){ return "16fae57e3091fe4b0fcfc0634a5b72b7"; };

  };

}
#endif
