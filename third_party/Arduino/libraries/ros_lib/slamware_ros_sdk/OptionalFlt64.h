#ifndef _ROS_slamware_ros_sdk_OptionalFlt64_h
#define _ROS_slamware_ros_sdk_OptionalFlt64_h

#include <stdint.h>
#include <string.h>
#include <stdlib.h>
#include "ros/msg.h"

namespace slamware_ros_sdk
{

  class OptionalFlt64 : public ros::Msg
  {
    public:
      typedef bool _is_valid_type;
      _is_valid_type is_valid;
      typedef float _value_type;
      _value_type value;

    OptionalFlt64():
      is_valid(0),
      value(0)
    {
    }

    virtual int serialize(unsigned char *outbuffer) const
    {
      int offset = 0;
      union {
        bool real;
        uint8_t base;
      } u_is_valid;
      u_is_valid.real = this->is_valid;
      *(outbuffer + offset + 0) = (u_is_valid.base >> (8 * 0)) & 0xFF;
      offset += sizeof(this->is_valid);
      offset += serializeAvrFloat64(outbuffer + offset, this->value);
      return offset;
    }

    virtual int deserialize(unsigned char *inbuffer)
    {
      int offset = 0;
      union {
        bool real;
        uint8_t base;
      } u_is_valid;
      u_is_valid.base = 0;
      u_is_valid.base |= ((uint8_t) (*(inbuffer + offset + 0))) << (8 * 0);
      this->is_valid = u_is_valid.real;
      offset += sizeof(this->is_valid);
      offset += deserializeAvrFloat64(inbuffer + offset, &(this->value));
     return offset;
    }

    const char * getType(){ return "slamware_ros_sdk/OptionalFlt64"; };
    const char * getMD5(){ return "0c9bf9d3f509c3e4cb7cb33373e1b9d5"; };

  };

}
#endif
