#ifndef _ROS_status_msgs_bno055_chip_h
#define _ROS_status_msgs_bno055_chip_h

#include <stdint.h>
#include <string.h>
#include <stdlib.h>
#include "ros/msg.h"
#include "status_msgs/vector.h"
#include "status_msgs/quaternion.h"

namespace status_msgs
{

  class bno055_chip : public ros::Msg
  {
    public:
      typedef uint8_t _statsu_type;
      _statsu_type statsu;
      typedef status_msgs::vector _eular_type;
      _eular_type eular;
      typedef status_msgs::vector _gyroscope_type;
      _gyroscope_type gyroscope;
      typedef status_msgs::vector _geomagnatic_type;
      _geomagnatic_type geomagnatic;
      typedef status_msgs::vector _gravity_type;
      _gravity_type gravity;
      typedef status_msgs::quaternion _quaternion_type;
      _quaternion_type quaternion;
      typedef status_msgs::vector _acceleration_type;
      _acceleration_type acceleration;
      typedef status_msgs::vector _linear_acceleration_type;
      _linear_acceleration_type linear_acceleration;

    bno055_chip():
      statsu(0),
      eular(),
      gyroscope(),
      geomagnatic(),
      gravity(),
      quaternion(),
      acceleration(),
      linear_acceleration()
    {
    }

    virtual int serialize(unsigned char *outbuffer) const
    {
      int offset = 0;
      *(outbuffer + offset + 0) = (this->statsu >> (8 * 0)) & 0xFF;
      offset += sizeof(this->statsu);
      offset += this->eular.serialize(outbuffer + offset);
      offset += this->gyroscope.serialize(outbuffer + offset);
      offset += this->geomagnatic.serialize(outbuffer + offset);
      offset += this->gravity.serialize(outbuffer + offset);
      offset += this->quaternion.serialize(outbuffer + offset);
      offset += this->acceleration.serialize(outbuffer + offset);
      offset += this->linear_acceleration.serialize(outbuffer + offset);
      return offset;
    }

    virtual int deserialize(unsigned char *inbuffer)
    {
      int offset = 0;
      this->statsu =  ((uint8_t) (*(inbuffer + offset)));
      offset += sizeof(this->statsu);
      offset += this->eular.deserialize(inbuffer + offset);
      offset += this->gyroscope.deserialize(inbuffer + offset);
      offset += this->geomagnatic.deserialize(inbuffer + offset);
      offset += this->gravity.deserialize(inbuffer + offset);
      offset += this->quaternion.deserialize(inbuffer + offset);
      offset += this->acceleration.deserialize(inbuffer + offset);
      offset += this->linear_acceleration.deserialize(inbuffer + offset);
     return offset;
    }

    const char * getType(){ return "status_msgs/bno055_chip"; };
    const char * getMD5(){ return "b9970b6cb091dbb6f6be2719497109a0"; };

  };

}
#endif
