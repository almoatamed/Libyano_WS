#ifndef _ROS_status_msgs_cash_reader_msg_h
#define _ROS_status_msgs_cash_reader_msg_h

#include <stdint.h>
#include <string.h>
#include <stdlib.h>
#include "ros/msg.h"
#include "status_msgs/cash_reader_counters_msg.h"
#include "status_msgs/cash_reader_channel_msg.h"

namespace status_msgs
{

  class cash_reader_msg : public ros::Msg
  {
    public:
      uint32_t events_length;
      typedef char* _events_type;
      _events_type st_events;
      _events_type * events;
      typedef status_msgs::cash_reader_counters_msg _cash_reader_counters_type;
      _cash_reader_counters_type cash_reader_counters;
      uint32_t cash_reader_channel_length;
      typedef status_msgs::cash_reader_channel_msg _cash_reader_channel_type;
      _cash_reader_channel_type st_cash_reader_channel;
      _cash_reader_channel_type * cash_reader_channel;
      uint32_t serial_length;
      typedef uint64_t _serial_type;
      _serial_type st_serial;
      _serial_type * serial;

    cash_reader_msg():
      events_length(0), events(NULL),
      cash_reader_counters(),
      cash_reader_channel_length(0), cash_reader_channel(NULL),
      serial_length(0), serial(NULL)
    {
    }

    virtual int serialize(unsigned char *outbuffer) const
    {
      int offset = 0;
      *(outbuffer + offset + 0) = (this->events_length >> (8 * 0)) & 0xFF;
      *(outbuffer + offset + 1) = (this->events_length >> (8 * 1)) & 0xFF;
      *(outbuffer + offset + 2) = (this->events_length >> (8 * 2)) & 0xFF;
      *(outbuffer + offset + 3) = (this->events_length >> (8 * 3)) & 0xFF;
      offset += sizeof(this->events_length);
      for( uint32_t i = 0; i < events_length; i++){
      uint32_t length_eventsi = strlen(this->events[i]);
      varToArr(outbuffer + offset, length_eventsi);
      offset += 4;
      memcpy(outbuffer + offset, this->events[i], length_eventsi);
      offset += length_eventsi;
      }
      offset += this->cash_reader_counters.serialize(outbuffer + offset);
      *(outbuffer + offset + 0) = (this->cash_reader_channel_length >> (8 * 0)) & 0xFF;
      *(outbuffer + offset + 1) = (this->cash_reader_channel_length >> (8 * 1)) & 0xFF;
      *(outbuffer + offset + 2) = (this->cash_reader_channel_length >> (8 * 2)) & 0xFF;
      *(outbuffer + offset + 3) = (this->cash_reader_channel_length >> (8 * 3)) & 0xFF;
      offset += sizeof(this->cash_reader_channel_length);
      for( uint32_t i = 0; i < cash_reader_channel_length; i++){
      offset += this->cash_reader_channel[i].serialize(outbuffer + offset);
      }
      *(outbuffer + offset + 0) = (this->serial_length >> (8 * 0)) & 0xFF;
      *(outbuffer + offset + 1) = (this->serial_length >> (8 * 1)) & 0xFF;
      *(outbuffer + offset + 2) = (this->serial_length >> (8 * 2)) & 0xFF;
      *(outbuffer + offset + 3) = (this->serial_length >> (8 * 3)) & 0xFF;
      offset += sizeof(this->serial_length);
      for( uint32_t i = 0; i < serial_length; i++){
      *(outbuffer + offset + 0) = (this->serial[i] >> (8 * 0)) & 0xFF;
      *(outbuffer + offset + 1) = (this->serial[i] >> (8 * 1)) & 0xFF;
      *(outbuffer + offset + 2) = (this->serial[i] >> (8 * 2)) & 0xFF;
      *(outbuffer + offset + 3) = (this->serial[i] >> (8 * 3)) & 0xFF;
      *(outbuffer + offset + 4) = (this->serial[i] >> (8 * 4)) & 0xFF;
      *(outbuffer + offset + 5) = (this->serial[i] >> (8 * 5)) & 0xFF;
      *(outbuffer + offset + 6) = (this->serial[i] >> (8 * 6)) & 0xFF;
      *(outbuffer + offset + 7) = (this->serial[i] >> (8 * 7)) & 0xFF;
      offset += sizeof(this->serial[i]);
      }
      return offset;
    }

    virtual int deserialize(unsigned char *inbuffer)
    {
      int offset = 0;
      uint32_t events_lengthT = ((uint32_t) (*(inbuffer + offset))); 
      events_lengthT |= ((uint32_t) (*(inbuffer + offset + 1))) << (8 * 1); 
      events_lengthT |= ((uint32_t) (*(inbuffer + offset + 2))) << (8 * 2); 
      events_lengthT |= ((uint32_t) (*(inbuffer + offset + 3))) << (8 * 3); 
      offset += sizeof(this->events_length);
      if(events_lengthT > events_length)
        this->events = (char**)realloc(this->events, events_lengthT * sizeof(char*));
      events_length = events_lengthT;
      for( uint32_t i = 0; i < events_length; i++){
      uint32_t length_st_events;
      arrToVar(length_st_events, (inbuffer + offset));
      offset += 4;
      for(unsigned int k= offset; k< offset+length_st_events; ++k){
          inbuffer[k-1]=inbuffer[k];
      }
      inbuffer[offset+length_st_events-1]=0;
      this->st_events = (char *)(inbuffer + offset-1);
      offset += length_st_events;
        memcpy( &(this->events[i]), &(this->st_events), sizeof(char*));
      }
      offset += this->cash_reader_counters.deserialize(inbuffer + offset);
      uint32_t cash_reader_channel_lengthT = ((uint32_t) (*(inbuffer + offset))); 
      cash_reader_channel_lengthT |= ((uint32_t) (*(inbuffer + offset + 1))) << (8 * 1); 
      cash_reader_channel_lengthT |= ((uint32_t) (*(inbuffer + offset + 2))) << (8 * 2); 
      cash_reader_channel_lengthT |= ((uint32_t) (*(inbuffer + offset + 3))) << (8 * 3); 
      offset += sizeof(this->cash_reader_channel_length);
      if(cash_reader_channel_lengthT > cash_reader_channel_length)
        this->cash_reader_channel = (status_msgs::cash_reader_channel_msg*)realloc(this->cash_reader_channel, cash_reader_channel_lengthT * sizeof(status_msgs::cash_reader_channel_msg));
      cash_reader_channel_length = cash_reader_channel_lengthT;
      for( uint32_t i = 0; i < cash_reader_channel_length; i++){
      offset += this->st_cash_reader_channel.deserialize(inbuffer + offset);
        memcpy( &(this->cash_reader_channel[i]), &(this->st_cash_reader_channel), sizeof(status_msgs::cash_reader_channel_msg));
      }
      uint32_t serial_lengthT = ((uint32_t) (*(inbuffer + offset))); 
      serial_lengthT |= ((uint32_t) (*(inbuffer + offset + 1))) << (8 * 1); 
      serial_lengthT |= ((uint32_t) (*(inbuffer + offset + 2))) << (8 * 2); 
      serial_lengthT |= ((uint32_t) (*(inbuffer + offset + 3))) << (8 * 3); 
      offset += sizeof(this->serial_length);
      if(serial_lengthT > serial_length)
        this->serial = (uint64_t*)realloc(this->serial, serial_lengthT * sizeof(uint64_t));
      serial_length = serial_lengthT;
      for( uint32_t i = 0; i < serial_length; i++){
      this->st_serial =  ((uint64_t) (*(inbuffer + offset)));
      this->st_serial |= ((uint64_t) (*(inbuffer + offset + 1))) << (8 * 1);
      this->st_serial |= ((uint64_t) (*(inbuffer + offset + 2))) << (8 * 2);
      this->st_serial |= ((uint64_t) (*(inbuffer + offset + 3))) << (8 * 3);
      this->st_serial |= ((uint64_t) (*(inbuffer + offset + 4))) << (8 * 4);
      this->st_serial |= ((uint64_t) (*(inbuffer + offset + 5))) << (8 * 5);
      this->st_serial |= ((uint64_t) (*(inbuffer + offset + 6))) << (8 * 6);
      this->st_serial |= ((uint64_t) (*(inbuffer + offset + 7))) << (8 * 7);
      offset += sizeof(this->st_serial);
        memcpy( &(this->serial[i]), &(this->st_serial), sizeof(uint64_t));
      }
     return offset;
    }

    const char * getType(){ return "status_msgs/cash_reader_msg"; };
    const char * getMD5(){ return "8c5516511c3a60c09beb576bd566b4d8"; };

  };

}
#endif
