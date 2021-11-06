#ifndef _ROS_status_msgs_status_h
#define _ROS_status_msgs_status_h

#include <stdint.h>
#include <string.h>
#include <stdlib.h>
#include "ros/msg.h"
#include "status_msgs/sensors_msg.h"
#include "status_msgs/driver_msg.h"
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
      typedef status_msgs::driver_msg _driver_type;
      _driver_type driver;
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

    status():
      sensors(),
      driver(),
      controllers(),
      power(),
      mcu_length(0), mcu(NULL),
      cash_reader()
    {
    }

    virtual int serialize(unsigned char *outbuffer) const
    {
      int offset = 0;
      offset += this->sensors.serialize(outbuffer + offset);
      offset += this->driver.serialize(outbuffer + offset);
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
      return offset;
    }

    virtual int deserialize(unsigned char *inbuffer)
    {
      int offset = 0;
      offset += this->sensors.deserialize(inbuffer + offset);
      offset += this->driver.deserialize(inbuffer + offset);
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
     return offset;
    }

    const char * getType(){ return "status_msgs/status"; };
    const char * getMD5(){ return "a36d345eec717910a160ce0cb2f1fb34"; };

  };

}
#endif
