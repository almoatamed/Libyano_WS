#ifndef _ROS_SERVICE_action_srv_h
#define _ROS_SERVICE_action_srv_h
#include <stdint.h>
#include <string.h>
#include <stdlib.h>
#include "ros/msg.h"

namespace action_handler_msgs
{

static const char ACTION_SRV[] = "action_handler_msgs/action_srv";

  class action_srvRequest : public ros::Msg
  {
    public:
      typedef const char* _action_type;
      _action_type action;

    action_srvRequest():
      action("")
    {
    }

    virtual int serialize(unsigned char *outbuffer) const
    {
      int offset = 0;
      uint32_t length_action = strlen(this->action);
      varToArr(outbuffer + offset, length_action);
      offset += 4;
      memcpy(outbuffer + offset, this->action, length_action);
      offset += length_action;
      return offset;
    }

    virtual int deserialize(unsigned char *inbuffer)
    {
      int offset = 0;
      uint32_t length_action;
      arrToVar(length_action, (inbuffer + offset));
      offset += 4;
      for(unsigned int k= offset; k< offset+length_action; ++k){
          inbuffer[k-1]=inbuffer[k];
      }
      inbuffer[offset+length_action-1]=0;
      this->action = (char *)(inbuffer + offset-1);
      offset += length_action;
     return offset;
    }

    const char * getType(){ return ACTION_SRV; };
    const char * getMD5(){ return "7757aad79fa343e61bc69ed7f1b7666d"; };

  };

  class action_srvResponse : public ros::Msg
  {
    public:
      typedef const char* _result_type;
      _result_type result;

    action_srvResponse():
      result("")
    {
    }

    virtual int serialize(unsigned char *outbuffer) const
    {
      int offset = 0;
      uint32_t length_result = strlen(this->result);
      varToArr(outbuffer + offset, length_result);
      offset += 4;
      memcpy(outbuffer + offset, this->result, length_result);
      offset += length_result;
      return offset;
    }

    virtual int deserialize(unsigned char *inbuffer)
    {
      int offset = 0;
      uint32_t length_result;
      arrToVar(length_result, (inbuffer + offset));
      offset += 4;
      for(unsigned int k= offset; k< offset+length_result; ++k){
          inbuffer[k-1]=inbuffer[k];
      }
      inbuffer[offset+length_result-1]=0;
      this->result = (char *)(inbuffer + offset-1);
      offset += length_result;
     return offset;
    }

    const char * getType(){ return ACTION_SRV; };
    const char * getMD5(){ return "c22f2a1ed8654a0b365f1bb3f7ff2c0f"; };

  };

  class action_srv {
    public:
    typedef action_srvRequest Request;
    typedef action_srvResponse Response;
  };

}
#endif
