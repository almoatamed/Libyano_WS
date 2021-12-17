#ifndef _ROS_status_msgs_power_msg_h
#define _ROS_status_msgs_power_msg_h

#include <stdint.h>
#include <string.h>
#include <stdlib.h>
#include "ros/msg.h"

namespace status_msgs
{

  class power_msg : public ros::Msg
  {
    public:
      typedef int32_t _battery_type;
      _battery_type battery;
      typedef bool _charging_status_type;
      _charging_status_type charging_status;
      typedef bool _cord_type;
      _cord_type cord;

    power_msg():
      battery(0),
      charging_status(0),
      cord(0)
    {
    }

    virtual int serialize(unsigned char *outbuffer) const
    {
      int offset = 0;
      union {
        int32_t real;
        uint32_t base;
      } u_battery;
      u_battery.real = this->battery;
      *(outbuffer + offset + 0) = (u_battery.base >> (8 * 0)) & 0xFF;
      *(outbuffer + offset + 1) = (u_battery.base >> (8 * 1)) & 0xFF;
      *(outbuffer + offset + 2) = (u_battery.base >> (8 * 2)) & 0xFF;
      *(outbuffer + offset + 3) = (u_battery.base >> (8 * 3)) & 0xFF;
      offset += sizeof(this->battery);
      union {
        bool real;
        uint8_t base;
      } u_charging_status;
      u_charging_status.real = this->charging_status;
      *(outbuffer + offset + 0) = (u_charging_status.base >> (8 * 0)) & 0xFF;
      offset += sizeof(this->charging_status);
      union {
        bool real;
        uint8_t base;
      } u_cord;
      u_cord.real = this->cord;
      *(outbuffer + offset + 0) = (u_cord.base >> (8 * 0)) & 0xFF;
      offset += sizeof(this->cord);
      return offset;
    }

    virtual int deserialize(unsigned char *inbuffer)
    {
      int offset = 0;
      union {
        int32_t real;
        uint32_t base;
      } u_battery;
      u_battery.base = 0;
      u_battery.base |= ((uint32_t) (*(inbuffer + offset + 0))) << (8 * 0);
      u_battery.base |= ((uint32_t) (*(inbuffer + offset + 1))) << (8 * 1);
      u_battery.base |= ((uint32_t) (*(inbuffer + offset + 2))) << (8 * 2);
      u_battery.base |= ((uint32_t) (*(inbuffer + offset + 3))) << (8 * 3);
      this->battery = u_battery.real;
      offset += sizeof(this->battery);
      union {
        bool real;
        uint8_t base;
      } u_charging_status;
      u_charging_status.base = 0;
      u_charging_status.base |= ((uint8_t) (*(inbuffer + offset + 0))) << (8 * 0);
      this->charging_status = u_charging_status.real;
      offset += sizeof(this->charging_status);
      union {
        bool real;
        uint8_t base;
      } u_cord;
      u_cord.base = 0;
      u_cord.base |= ((uint8_t) (*(inbuffer + offset + 0))) << (8 * 0);
      this->cord = u_cord.real;
      offset += sizeof(this->cord);
     return offset;
    }

    const char * getType(){ return "status_msgs/power_msg"; };
    const char * getMD5(){ return "9842d50af5c61cd052a3818a589a22b6"; };

  };

}
#endif
