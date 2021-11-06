#ifndef _ROS_status_msgs_goal_monitor_msg_h
#define _ROS_status_msgs_goal_monitor_msg_h

#include <stdint.h>
#include <string.h>
#include <stdlib.h>
#include "ros/msg.h"
#include "status_msgs/vector.h"
#include "status_msgs/quaternion.h"

namespace status_msgs
{

  class goal_monitor_msg : public ros::Msg
  {
    public:
      typedef status_msgs::vector _pose_type;
      _pose_type pose;
      typedef status_msgs::quaternion _orientation_type;
      _orientation_type orientation;
      typedef bool _is_angled_type;
      _is_angled_type is_angled;
      typedef const char* _state_type;
      _state_type state;

    goal_monitor_msg():
      pose(),
      orientation(),
      is_angled(0),
      state("")
    {
    }

    virtual int serialize(unsigned char *outbuffer) const
    {
      int offset = 0;
      offset += this->pose.serialize(outbuffer + offset);
      offset += this->orientation.serialize(outbuffer + offset);
      union {
        bool real;
        uint8_t base;
      } u_is_angled;
      u_is_angled.real = this->is_angled;
      *(outbuffer + offset + 0) = (u_is_angled.base >> (8 * 0)) & 0xFF;
      offset += sizeof(this->is_angled);
      uint32_t length_state = strlen(this->state);
      varToArr(outbuffer + offset, length_state);
      offset += 4;
      memcpy(outbuffer + offset, this->state, length_state);
      offset += length_state;
      return offset;
    }

    virtual int deserialize(unsigned char *inbuffer)
    {
      int offset = 0;
      offset += this->pose.deserialize(inbuffer + offset);
      offset += this->orientation.deserialize(inbuffer + offset);
      union {
        bool real;
        uint8_t base;
      } u_is_angled;
      u_is_angled.base = 0;
      u_is_angled.base |= ((uint8_t) (*(inbuffer + offset + 0))) << (8 * 0);
      this->is_angled = u_is_angled.real;
      offset += sizeof(this->is_angled);
      uint32_t length_state;
      arrToVar(length_state, (inbuffer + offset));
      offset += 4;
      for(unsigned int k= offset; k< offset+length_state; ++k){
          inbuffer[k-1]=inbuffer[k];
      }
      inbuffer[offset+length_state-1]=0;
      this->state = (char *)(inbuffer + offset-1);
      offset += length_state;
     return offset;
    }

    const char * getType(){ return "status_msgs/goal_monitor_msg"; };
    const char * getMD5(){ return "6756cfffb2c94232ccffb6f76402296d"; };

  };

}
#endif
