#ifndef _ROS_status_msgs_controllers_msg_h
#define _ROS_status_msgs_controllers_msg_h

#include <stdint.h>
#include <string.h>
#include <stdlib.h>
#include "ros/msg.h"
#include "status_msgs/pixelgrid_msg.h"
#include "status_msgs/led_ring_msg.h"
#include "status_msgs/servo_msg.h"

namespace status_msgs
{

  class controllers_msg : public ros::Msg
  {
    public:
      typedef status_msgs::pixelgrid_msg _pixelgrid_type;
      _pixelgrid_type pixelgrid;
      typedef status_msgs::led_ring_msg _led_ring_type;
      _led_ring_type led_ring;
      uint32_t relays_length;
      typedef uint8_t _relays_type;
      _relays_type st_relays;
      _relays_type * relays;
      uint32_t servos_length;
      typedef status_msgs::servo_msg _servos_type;
      _servos_type st_servos;
      _servos_type * servos;

    controllers_msg():
      pixelgrid(),
      led_ring(),
      relays_length(0), relays(NULL),
      servos_length(0), servos(NULL)
    {
    }

    virtual int serialize(unsigned char *outbuffer) const
    {
      int offset = 0;
      offset += this->pixelgrid.serialize(outbuffer + offset);
      offset += this->led_ring.serialize(outbuffer + offset);
      *(outbuffer + offset + 0) = (this->relays_length >> (8 * 0)) & 0xFF;
      *(outbuffer + offset + 1) = (this->relays_length >> (8 * 1)) & 0xFF;
      *(outbuffer + offset + 2) = (this->relays_length >> (8 * 2)) & 0xFF;
      *(outbuffer + offset + 3) = (this->relays_length >> (8 * 3)) & 0xFF;
      offset += sizeof(this->relays_length);
      for( uint32_t i = 0; i < relays_length; i++){
      *(outbuffer + offset + 0) = (this->relays[i] >> (8 * 0)) & 0xFF;
      offset += sizeof(this->relays[i]);
      }
      *(outbuffer + offset + 0) = (this->servos_length >> (8 * 0)) & 0xFF;
      *(outbuffer + offset + 1) = (this->servos_length >> (8 * 1)) & 0xFF;
      *(outbuffer + offset + 2) = (this->servos_length >> (8 * 2)) & 0xFF;
      *(outbuffer + offset + 3) = (this->servos_length >> (8 * 3)) & 0xFF;
      offset += sizeof(this->servos_length);
      for( uint32_t i = 0; i < servos_length; i++){
      offset += this->servos[i].serialize(outbuffer + offset);
      }
      return offset;
    }

    virtual int deserialize(unsigned char *inbuffer)
    {
      int offset = 0;
      offset += this->pixelgrid.deserialize(inbuffer + offset);
      offset += this->led_ring.deserialize(inbuffer + offset);
      uint32_t relays_lengthT = ((uint32_t) (*(inbuffer + offset))); 
      relays_lengthT |= ((uint32_t) (*(inbuffer + offset + 1))) << (8 * 1); 
      relays_lengthT |= ((uint32_t) (*(inbuffer + offset + 2))) << (8 * 2); 
      relays_lengthT |= ((uint32_t) (*(inbuffer + offset + 3))) << (8 * 3); 
      offset += sizeof(this->relays_length);
      if(relays_lengthT > relays_length)
        this->relays = (uint8_t*)realloc(this->relays, relays_lengthT * sizeof(uint8_t));
      relays_length = relays_lengthT;
      for( uint32_t i = 0; i < relays_length; i++){
      this->st_relays =  ((uint8_t) (*(inbuffer + offset)));
      offset += sizeof(this->st_relays);
        memcpy( &(this->relays[i]), &(this->st_relays), sizeof(uint8_t));
      }
      uint32_t servos_lengthT = ((uint32_t) (*(inbuffer + offset))); 
      servos_lengthT |= ((uint32_t) (*(inbuffer + offset + 1))) << (8 * 1); 
      servos_lengthT |= ((uint32_t) (*(inbuffer + offset + 2))) << (8 * 2); 
      servos_lengthT |= ((uint32_t) (*(inbuffer + offset + 3))) << (8 * 3); 
      offset += sizeof(this->servos_length);
      if(servos_lengthT > servos_length)
        this->servos = (status_msgs::servo_msg*)realloc(this->servos, servos_lengthT * sizeof(status_msgs::servo_msg));
      servos_length = servos_lengthT;
      for( uint32_t i = 0; i < servos_length; i++){
      offset += this->st_servos.deserialize(inbuffer + offset);
        memcpy( &(this->servos[i]), &(this->st_servos), sizeof(status_msgs::servo_msg));
      }
     return offset;
    }

    const char * getType(){ return "status_msgs/controllers_msg"; };
    const char * getMD5(){ return "d3d5811adfc7665578f5f138d6529073"; };

  };

}
#endif
