#ifndef _ROS_status_msgs_driver_msg_h
#define _ROS_status_msgs_driver_msg_h

#include <stdint.h>
#include <string.h>
#include <stdlib.h>
#include "ros/msg.h"
#include "status_msgs/driver_system_msg.h"
#include "status_msgs/axis_msg.h"

namespace status_msgs
{

  class driver_msg : public ros::Msg
  {
    public:
      typedef status_msgs::driver_system_msg _system_type;
      _system_type system;
      typedef status_msgs::axis_msg _axis0_type;
      _axis0_type axis0;
      typedef status_msgs::axis_msg _axis1_type;
      _axis1_type axis1;

    driver_msg():
      system(),
      axis0(),
      axis1()
    {
    }

    virtual int serialize(unsigned char *outbuffer) const
    {
      int offset = 0;
      offset += this->system.serialize(outbuffer + offset);
      offset += this->axis0.serialize(outbuffer + offset);
      offset += this->axis1.serialize(outbuffer + offset);
      return offset;
    }

    virtual int deserialize(unsigned char *inbuffer)
    {
      int offset = 0;
      offset += this->system.deserialize(inbuffer + offset);
      offset += this->axis0.deserialize(inbuffer + offset);
      offset += this->axis1.deserialize(inbuffer + offset);
     return offset;
    }

    const char * getType(){ return "status_msgs/driver_msg"; };
    const char * getMD5(){ return "fbfcdf5c9c38bd847537c10151a328db"; };

  };

}
#endif
