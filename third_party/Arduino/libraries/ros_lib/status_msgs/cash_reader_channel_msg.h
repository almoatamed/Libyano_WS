#ifndef _ROS_status_msgs_cash_reader_channel_msg_h
#define _ROS_status_msgs_cash_reader_channel_msg_h

#include <stdint.h>
#include <string.h>
#include <stdlib.h>
#include "ros/msg.h"

namespace status_msgs
{

  class cash_reader_channel_msg : public ros::Msg
  {
    public:
      typedef uint8_t _channel_type;
      _channel_type channel;
      typedef const char* _currency_type;
      _currency_type currency;
      typedef float _value_type;
      _value_type value;

    cash_reader_channel_msg():
      channel(0),
      currency(""),
      value(0)
    {
    }

    virtual int serialize(unsigned char *outbuffer) const
    {
      int offset = 0;
      *(outbuffer + offset + 0) = (this->channel >> (8 * 0)) & 0xFF;
      offset += sizeof(this->channel);
      uint32_t length_currency = strlen(this->currency);
      varToArr(outbuffer + offset, length_currency);
      offset += 4;
      memcpy(outbuffer + offset, this->currency, length_currency);
      offset += length_currency;
      union {
        float real;
        uint32_t base;
      } u_value;
      u_value.real = this->value;
      *(outbuffer + offset + 0) = (u_value.base >> (8 * 0)) & 0xFF;
      *(outbuffer + offset + 1) = (u_value.base >> (8 * 1)) & 0xFF;
      *(outbuffer + offset + 2) = (u_value.base >> (8 * 2)) & 0xFF;
      *(outbuffer + offset + 3) = (u_value.base >> (8 * 3)) & 0xFF;
      offset += sizeof(this->value);
      return offset;
    }

    virtual int deserialize(unsigned char *inbuffer)
    {
      int offset = 0;
      this->channel =  ((uint8_t) (*(inbuffer + offset)));
      offset += sizeof(this->channel);
      uint32_t length_currency;
      arrToVar(length_currency, (inbuffer + offset));
      offset += 4;
      for(unsigned int k= offset; k< offset+length_currency; ++k){
          inbuffer[k-1]=inbuffer[k];
      }
      inbuffer[offset+length_currency-1]=0;
      this->currency = (char *)(inbuffer + offset-1);
      offset += length_currency;
      union {
        float real;
        uint32_t base;
      } u_value;
      u_value.base = 0;
      u_value.base |= ((uint32_t) (*(inbuffer + offset + 0))) << (8 * 0);
      u_value.base |= ((uint32_t) (*(inbuffer + offset + 1))) << (8 * 1);
      u_value.base |= ((uint32_t) (*(inbuffer + offset + 2))) << (8 * 2);
      u_value.base |= ((uint32_t) (*(inbuffer + offset + 3))) << (8 * 3);
      this->value = u_value.real;
      offset += sizeof(this->value);
     return offset;
    }

    const char * getType(){ return "status_msgs/cash_reader_channel_msg"; };
    const char * getMD5(){ return "d1f8f2a8854c6e2436c62e2db5e4dbb5"; };

  };

}
#endif
