#ifndef _ROS_status_msgs_status_h
#define _ROS_status_msgs_status_h

#include <stdint.h>
#include <string.h>
#include <stdlib.h>
#include "ros/msg.h"
#include "status_msgs/sensors_msg.h"
#include "status_msgs/controllers_msg.h"
#include "status_msgs/power_msg.h"
#include "status_msgs/cash_reader_msg.h"

namespace status_msgs
{

  class status : public ros::Msg
  {
    public:
      typedef status_msgs::sensors_msg _sensors_type;
      _sensors_type sensors;
      typedef status_msgs::controllers_msg _controllers_type;
      _controllers_type controllers;
      typedef status_msgs::power_msg _power_type;
      _power_type power;
      uint32_t mcu_length;
      typedef uint8_t _mcu_type;
      _mcu_type st_mcu;
      _mcu_type * mcu;
      typedef status_msgs::cash_reader_msg _cash_reader_type;
      _cash_reader_type cash_reader;
      uint32_t nodes_list_length;
      typedef char* _nodes_list_type;
      _nodes_list_type st_nodes_list;
      _nodes_list_type * nodes_list;
      typedef const char* _mode_type;
      _mode_type mode;

    status():
      sensors(),
      controllers(),
      power(),
      mcu_length(0), mcu(NULL),
      cash_reader(),
      nodes_list_length(0), nodes_list(NULL),
      mode("")
    {
    }

    virtual int serialize(unsigned char *outbuffer) const
    {
      int offset = 0;
      offset += this->sensors.serialize(outbuffer + offset);
      offset += this->controllers.serialize(outbuffer + offset);
      offset += this->power.serialize(outbuffer + offset);
      *(outbuffer + offset + 0) = (this->mcu_length >> (8 * 0)) & 0xFF;
      *(outbuffer + offset + 1) = (this->mcu_length >> (8 * 1)) & 0xFF;
      *(outbuffer + offset + 2) = (this->mcu_length >> (8 * 2)) & 0xFF;
      *(outbuffer + offset + 3) = (this->mcu_length >> (8 * 3)) & 0xFF;
      offset += sizeof(this->mcu_length);
      for( uint32_t i = 0; i < mcu_length; i++){
      *(outbuffer + offset + 0) = (this->mcu[i] >> (8 * 0)) & 0xFF;
      offset += sizeof(this->mcu[i]);
      }
      offset += this->cash_reader.serialize(outbuffer + offset);
      *(outbuffer + offset + 0) = (this->nodes_list_length >> (8 * 0)) & 0xFF;
      *(outbuffer + offset + 1) = (this->nodes_list_length >> (8 * 1)) & 0xFF;
      *(outbuffer + offset + 2) = (this->nodes_list_length >> (8 * 2)) & 0xFF;
      *(outbuffer + offset + 3) = (this->nodes_list_length >> (8 * 3)) & 0xFF;
      offset += sizeof(this->nodes_list_length);
      for( uint32_t i = 0; i < nodes_list_length; i++){
      uint32_t length_nodes_listi = strlen(this->nodes_list[i]);
      varToArr(outbuffer + offset, length_nodes_listi);
      offset += 4;
      memcpy(outbuffer + offset, this->nodes_list[i], length_nodes_listi);
      offset += length_nodes_listi;
      }
      uint32_t length_mode = strlen(this->mode);
      varToArr(outbuffer + offset, length_mode);
      offset += 4;
      memcpy(outbuffer + offset, this->mode, length_mode);
      offset += length_mode;
      return offset;
    }

    virtual int deserialize(unsigned char *inbuffer)
    {
      int offset = 0;
      offset += this->sensors.deserialize(inbuffer + offset);
      offset += this->controllers.deserialize(inbuffer + offset);
      offset += this->power.deserialize(inbuffer + offset);
      uint32_t mcu_lengthT = ((uint32_t) (*(inbuffer + offset))); 
      mcu_lengthT |= ((uint32_t) (*(inbuffer + offset + 1))) << (8 * 1); 
      mcu_lengthT |= ((uint32_t) (*(inbuffer + offset + 2))) << (8 * 2); 
      mcu_lengthT |= ((uint32_t) (*(inbuffer + offset + 3))) << (8 * 3); 
      offset += sizeof(this->mcu_length);
      if(mcu_lengthT > mcu_length)
        this->mcu = (uint8_t*)realloc(this->mcu, mcu_lengthT * sizeof(uint8_t));
      mcu_length = mcu_lengthT;
      for( uint32_t i = 0; i < mcu_length; i++){
      this->st_mcu =  ((uint8_t) (*(inbuffer + offset)));
      offset += sizeof(this->st_mcu);
        memcpy( &(this->mcu[i]), &(this->st_mcu), sizeof(uint8_t));
      }
      offset += this->cash_reader.deserialize(inbuffer + offset);
      uint32_t nodes_list_lengthT = ((uint32_t) (*(inbuffer + offset))); 
      nodes_list_lengthT |= ((uint32_t) (*(inbuffer + offset + 1))) << (8 * 1); 
      nodes_list_lengthT |= ((uint32_t) (*(inbuffer + offset + 2))) << (8 * 2); 
      nodes_list_lengthT |= ((uint32_t) (*(inbuffer + offset + 3))) << (8 * 3); 
      offset += sizeof(this->nodes_list_length);
      if(nodes_list_lengthT > nodes_list_length)
        this->nodes_list = (char**)realloc(this->nodes_list, nodes_list_lengthT * sizeof(char*));
      nodes_list_length = nodes_list_lengthT;
      for( uint32_t i = 0; i < nodes_list_length; i++){
      uint32_t length_st_nodes_list;
      arrToVar(length_st_nodes_list, (inbuffer + offset));
      offset += 4;
      for(unsigned int k= offset; k< offset+length_st_nodes_list; ++k){
          inbuffer[k-1]=inbuffer[k];
      }
      inbuffer[offset+length_st_nodes_list-1]=0;
      this->st_nodes_list = (char *)(inbuffer + offset-1);
      offset += length_st_nodes_list;
        memcpy( &(this->nodes_list[i]), &(this->st_nodes_list), sizeof(char*));
      }
      uint32_t length_mode;
      arrToVar(length_mode, (inbuffer + offset));
      offset += 4;
      for(unsigned int k= offset; k< offset+length_mode; ++k){
          inbuffer[k-1]=inbuffer[k];
      }
      inbuffer[offset+length_mode-1]=0;
      this->mode = (char *)(inbuffer + offset-1);
      offset += length_mode;
     return offset;
    }

    const char * getType(){ return "status_msgs/status"; };
    const char * getMD5(){ return "bbe5ce96ec870bfc9a11c53bfc7fd8a8"; };

  };

}
#endif
