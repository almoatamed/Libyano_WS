#ifndef _ROS_mcu_msgs_mcu_input_h
#define _ROS_mcu_msgs_mcu_input_h

#include <stdint.h>
#include <string.h>
#include <stdlib.h>
#include "ros/msg.h"

namespace mcu_msgs
{

  class mcu_input : public ros::Msg
  {
    public:
      typedef uint8_t _Element_type;
      _Element_type Element;
      typedef uint8_t _Part_and_function_type;
      _Part_and_function_type Part_and_function;
      uint32_t values_length;
      typedef float _values_type;
      _values_type st_values;
      _values_type * values;

    mcu_input():
      Element(0),
      Part_and_function(0),
      values_length(0), values(NULL)
    {
    }

    virtual int serialize(unsigned char *outbuffer) const
    {
      int offset = 0;
      *(outbuffer + offset + 0) = (this->Element >> (8 * 0)) & 0xFF;
      offset += sizeof(this->Element);
      *(outbuffer + offset + 0) = (this->Part_and_function >> (8 * 0)) & 0xFF;
      offset += sizeof(this->Part_and_function);
      *(outbuffer + offset + 0) = (this->values_length >> (8 * 0)) & 0xFF;
      *(outbuffer + offset + 1) = (this->values_length >> (8 * 1)) & 0xFF;
      *(outbuffer + offset + 2) = (this->values_length >> (8 * 2)) & 0xFF;
      *(outbuffer + offset + 3) = (this->values_length >> (8 * 3)) & 0xFF;
      offset += sizeof(this->values_length);
      for( uint32_t i = 0; i < values_length; i++){
      union {
        float real;
        uint32_t base;
      } u_valuesi;
      u_valuesi.real = this->values[i];
      *(outbuffer + offset + 0) = (u_valuesi.base >> (8 * 0)) & 0xFF;
      *(outbuffer + offset + 1) = (u_valuesi.base >> (8 * 1)) & 0xFF;
      *(outbuffer + offset + 2) = (u_valuesi.base >> (8 * 2)) & 0xFF;
      *(outbuffer + offset + 3) = (u_valuesi.base >> (8 * 3)) & 0xFF;
      offset += sizeof(this->values[i]);
      }
      return offset;
    }

    virtual int deserialize(unsigned char *inbuffer)
    {
      int offset = 0;
      this->Element =  ((uint8_t) (*(inbuffer + offset)));
      offset += sizeof(this->Element);
      this->Part_and_function =  ((uint8_t) (*(inbuffer + offset)));
      offset += sizeof(this->Part_and_function);
      uint32_t values_lengthT = ((uint32_t) (*(inbuffer + offset))); 
      values_lengthT |= ((uint32_t) (*(inbuffer + offset + 1))) << (8 * 1); 
      values_lengthT |= ((uint32_t) (*(inbuffer + offset + 2))) << (8 * 2); 
      values_lengthT |= ((uint32_t) (*(inbuffer + offset + 3))) << (8 * 3); 
      offset += sizeof(this->values_length);
      if(values_lengthT > values_length)
        this->values = (float*)realloc(this->values, values_lengthT * sizeof(float));
      values_length = values_lengthT;
      for( uint32_t i = 0; i < values_length; i++){
      union {
        float real;
        uint32_t base;
      } u_st_values;
      u_st_values.base = 0;
      u_st_values.base |= ((uint32_t) (*(inbuffer + offset + 0))) << (8 * 0);
      u_st_values.base |= ((uint32_t) (*(inbuffer + offset + 1))) << (8 * 1);
      u_st_values.base |= ((uint32_t) (*(inbuffer + offset + 2))) << (8 * 2);
      u_st_values.base |= ((uint32_t) (*(inbuffer + offset + 3))) << (8 * 3);
      this->st_values = u_st_values.real;
      offset += sizeof(this->st_values);
        memcpy( &(this->values[i]), &(this->st_values), sizeof(float));
      }
     return offset;
    }

    const char * getType(){ return "mcu_msgs/mcu_input"; };
    const char * getMD5(){ return "9e32c3d40e25c632be3e4637fb6ca2ad"; };

  };

}
#endif
