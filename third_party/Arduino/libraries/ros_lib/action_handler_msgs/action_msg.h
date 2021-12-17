#ifndef _ROS_action_handler_msgs_action_msg_h
#define _ROS_action_handler_msgs_action_msg_h

#include <stdint.h>
#include <string.h>
#include <stdlib.h>
#include "ros/msg.h"

namespace action_handler_msgs
{

  class action_msg : public ros::Msg
  {
    public:
      typedef const char* _category_type;
      _category_type category;
      typedef const char* _action_name_type;
      _action_name_type action_name;

    action_msg():
      category(""),
      action_name("")
    {
    }

    virtual int serialize(unsigned char *outbuffer) const
    {
      int offset = 0;
      uint32_t length_category = strlen(this->category);
      varToArr(outbuffer + offset, length_category);
      offset += 4;
      memcpy(outbuffer + offset, this->category, length_category);
      offset += length_category;
      uint32_t length_action_name = strlen(this->action_name);
      varToArr(outbuffer + offset, length_action_name);
      offset += 4;
      memcpy(outbuffer + offset, this->action_name, length_action_name);
      offset += length_action_name;
      return offset;
    }

    virtual int deserialize(unsigned char *inbuffer)
    {
      int offset = 0;
      uint32_t length_category;
      arrToVar(length_category, (inbuffer + offset));
      offset += 4;
      for(unsigned int k= offset; k< offset+length_category; ++k){
          inbuffer[k-1]=inbuffer[k];
      }
      inbuffer[offset+length_category-1]=0;
      this->category = (char *)(inbuffer + offset-1);
      offset += length_category;
      uint32_t length_action_name;
      arrToVar(length_action_name, (inbuffer + offset));
      offset += 4;
      for(unsigned int k= offset; k< offset+length_action_name; ++k){
          inbuffer[k-1]=inbuffer[k];
      }
      inbuffer[offset+length_action_name-1]=0;
      this->action_name = (char *)(inbuffer + offset-1);
      offset += length_action_name;
     return offset;
    }

    const char * getType(){ return "action_handler_msgs/action_msg"; };
    const char * getMD5(){ return "a35bd6d6c2b6b871823d53d3bd7c036c"; };

  };

}
#endif
