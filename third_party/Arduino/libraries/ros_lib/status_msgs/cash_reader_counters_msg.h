#ifndef _ROS_status_msgs_cash_reader_counters_msg_h
#define _ROS_status_msgs_cash_reader_counters_msg_h

#include <stdint.h>
#include <string.h>
#include <stdlib.h>
#include "ros/msg.h"

namespace status_msgs
{

  class cash_reader_counters_msg : public ros::Msg
  {
    public:
      typedef int16_t _stacked_type;
      _stacked_type stacked;
      typedef int16_t _stored_type;
      _stored_type stored;
      typedef int16_t _dispensed_type;
      _dispensed_type dispensed;
      typedef int16_t _transferred_type;
      _transferred_type transferred;
      typedef int16_t _rejected_type;
      _rejected_type rejected;

    cash_reader_counters_msg():
      stacked(0),
      stored(0),
      dispensed(0),
      transferred(0),
      rejected(0)
    {
    }

    virtual int serialize(unsigned char *outbuffer) const
    {
      int offset = 0;
      union {
        int16_t real;
        uint16_t base;
      } u_stacked;
      u_stacked.real = this->stacked;
      *(outbuffer + offset + 0) = (u_stacked.base >> (8 * 0)) & 0xFF;
      *(outbuffer + offset + 1) = (u_stacked.base >> (8 * 1)) & 0xFF;
      offset += sizeof(this->stacked);
      union {
        int16_t real;
        uint16_t base;
      } u_stored;
      u_stored.real = this->stored;
      *(outbuffer + offset + 0) = (u_stored.base >> (8 * 0)) & 0xFF;
      *(outbuffer + offset + 1) = (u_stored.base >> (8 * 1)) & 0xFF;
      offset += sizeof(this->stored);
      union {
        int16_t real;
        uint16_t base;
      } u_dispensed;
      u_dispensed.real = this->dispensed;
      *(outbuffer + offset + 0) = (u_dispensed.base >> (8 * 0)) & 0xFF;
      *(outbuffer + offset + 1) = (u_dispensed.base >> (8 * 1)) & 0xFF;
      offset += sizeof(this->dispensed);
      union {
        int16_t real;
        uint16_t base;
      } u_transferred;
      u_transferred.real = this->transferred;
      *(outbuffer + offset + 0) = (u_transferred.base >> (8 * 0)) & 0xFF;
      *(outbuffer + offset + 1) = (u_transferred.base >> (8 * 1)) & 0xFF;
      offset += sizeof(this->transferred);
      union {
        int16_t real;
        uint16_t base;
      } u_rejected;
      u_rejected.real = this->rejected;
      *(outbuffer + offset + 0) = (u_rejected.base >> (8 * 0)) & 0xFF;
      *(outbuffer + offset + 1) = (u_rejected.base >> (8 * 1)) & 0xFF;
      offset += sizeof(this->rejected);
      return offset;
    }

    virtual int deserialize(unsigned char *inbuffer)
    {
      int offset = 0;
      union {
        int16_t real;
        uint16_t base;
      } u_stacked;
      u_stacked.base = 0;
      u_stacked.base |= ((uint16_t) (*(inbuffer + offset + 0))) << (8 * 0);
      u_stacked.base |= ((uint16_t) (*(inbuffer + offset + 1))) << (8 * 1);
      this->stacked = u_stacked.real;
      offset += sizeof(this->stacked);
      union {
        int16_t real;
        uint16_t base;
      } u_stored;
      u_stored.base = 0;
      u_stored.base |= ((uint16_t) (*(inbuffer + offset + 0))) << (8 * 0);
      u_stored.base |= ((uint16_t) (*(inbuffer + offset + 1))) << (8 * 1);
      this->stored = u_stored.real;
      offset += sizeof(this->stored);
      union {
        int16_t real;
        uint16_t base;
      } u_dispensed;
      u_dispensed.base = 0;
      u_dispensed.base |= ((uint16_t) (*(inbuffer + offset + 0))) << (8 * 0);
      u_dispensed.base |= ((uint16_t) (*(inbuffer + offset + 1))) << (8 * 1);
      this->dispensed = u_dispensed.real;
      offset += sizeof(this->dispensed);
      union {
        int16_t real;
        uint16_t base;
      } u_transferred;
      u_transferred.base = 0;
      u_transferred.base |= ((uint16_t) (*(inbuffer + offset + 0))) << (8 * 0);
      u_transferred.base |= ((uint16_t) (*(inbuffer + offset + 1))) << (8 * 1);
      this->transferred = u_transferred.real;
      offset += sizeof(this->transferred);
      union {
        int16_t real;
        uint16_t base;
      } u_rejected;
      u_rejected.base = 0;
      u_rejected.base |= ((uint16_t) (*(inbuffer + offset + 0))) << (8 * 0);
      u_rejected.base |= ((uint16_t) (*(inbuffer + offset + 1))) << (8 * 1);
      this->rejected = u_rejected.real;
      offset += sizeof(this->rejected);
     return offset;
    }

    const char * getType(){ return "status_msgs/cash_reader_counters_msg"; };
    const char * getMD5(){ return "82d0c6b30e171e2dd9dc2803efb91c4b"; };

  };

}
#endif
