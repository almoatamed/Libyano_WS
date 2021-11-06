#ifndef _ROS_mcu_msgs_mcu_output_h
#define _ROS_mcu_msgs_mcu_output_h

#include <stdint.h>
#include <string.h>
#include <stdlib.h>
#include "ros/msg.h"
#include "mcu_msgs/mcu_input.h"

namespace mcu_msgs
{

  class mcu_output : public ros::Msg
  {
    public:
      uint32_t output_length;
      typedef mcu_msgs::mcu_input _output_type;
      _output_type st_output;
      _output_type * output;

    mcu_output():
      output_length(0), output(NULL)
    {
    }

    virtual int serialize(unsigned char *outbuffer) const
    {
      int offset = 0;
      *(outbuffer + offset + 0) = (this->output_length >> (8 * 0)) & 0xFF;
      *(outbuffer + offset + 1) = (this->output_length >> (8 * 1)) & 0xFF;
      *(outbuffer + offset + 2) = (this->output_length >> (8 * 2)) & 0xFF;
      *(outbuffer + offset + 3) = (this->output_length >> (8 * 3)) & 0xFF;
      offset += sizeof(this->output_length);
      for( uint32_t i = 0; i < output_length; i++){
      offset += this->output[i].serialize(outbuffer + offset);
      }
      return offset;
    }

    virtual int deserialize(unsigned char *inbuffer)
    {
      int offset = 0;
      uint32_t output_lengthT = ((uint32_t) (*(inbuffer + offset))); 
      output_lengthT |= ((uint32_t) (*(inbuffer + offset + 1))) << (8 * 1); 
      output_lengthT |= ((uint32_t) (*(inbuffer + offset + 2))) << (8 * 2); 
      output_lengthT |= ((uint32_t) (*(inbuffer + offset + 3))) << (8 * 3); 
      offset += sizeof(this->output_length);
      if(output_lengthT > output_length)
        this->output = (mcu_msgs::mcu_input*)realloc(this->output, output_lengthT * sizeof(mcu_msgs::mcu_input));
      output_length = output_lengthT;
      for( uint32_t i = 0; i < output_length; i++){
      offset += this->st_output.deserialize(inbuffer + offset);
        memcpy( &(this->output[i]), &(this->st_output), sizeof(mcu_msgs::mcu_input));
      }
     return offset;
    }

    const char * getType(){ return "mcu_msgs/mcu_output"; };
    const char * getMD5(){ return "1183a28e47cf8079d556695ea67a0ecb"; };

  };

}
#endif
