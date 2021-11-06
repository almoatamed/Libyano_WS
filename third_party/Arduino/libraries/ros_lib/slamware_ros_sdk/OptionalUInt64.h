#ifndef _ROS_slamware_ros_sdk_OptionalUInt64_h
#define _ROS_slamware_ros_sdk_OptionalUInt64_h

#include <stdint.h>
#include <string.h>
#include <stdlib.h>
#include "ros/msg.h"

namespace slamware_ros_sdk
{

  class OptionalUInt64 : public ros::Msg
  {
    public:
      typedef bool _is_valid_type;
      _is_valid_type is_valid;
      typedef uint64_t _value_type;
      _value_type value;

    OptionalUInt64():
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
      *(outbuffer + offset + 0) = (this->value >> (8 * 0)) & 0xFF;
      *(outbuffer + offset + 1) = (this->value >> (8 * 1)) & 0xFF;
      *(outbuffer + offset + 2) = (this->value >> (8 * 2)) & 0xFF;
      *(outbuffer + offset + 3) = (this->value >> (8 * 3)) & 0xFF;
      *(outbuffer + offset + 4) = (this->value >> (8 * 4)) & 0xFF;
      *(outbuffer + offset + 5) = (this->value >> (8 * 5)) & 0xFF;
      *(outbuffer + offset + 6) = (this->value >> (8 * 6)) & 0xFF;
      *(outbuffer + offset + 7) = (this->value >> (8 * 7)) & 0xFF;
      offset += sizeof(this->value);
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
      this->value =  ((uint64_t) (*(inbuffer + offset)));
      this->value |= ((uint64_t) (*(inbuffer + offset + 1))) << (8 * 1);
      this->value |= ((uint64_t) (*(inbuffer + offset + 2))) << (8 * 2);
      this->value |= ((uint64_t) (*(inbuffer + offset + 3))) << (8 * 3);
      this->value |= ((uint64_t) (*(inbuffer + offset + 4))) << (8 * 4);
      this->value |= ((uint64_t) (*(inbuffer + offset + 5))) << (8 * 5);
      this->value |= ((uint64_t) (*(inbuffer + offset + 6))) << (8 * 6);
      this->value |= ((uint64_t) (*(inbuffer + offset + 7))) << (8 * 7);
      offset += sizeof(this->value);
     return offset;
    }

    const char * getType(){ return "slamware_ros_sdk/OptionalUInt64"; };
    const char * getMD5(){ return "bbc8206789ded580217090457c51cb66"; };

  };

}
#endif
