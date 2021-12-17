#ifndef _ROS_status_msgs_motor_msg_h
#define _ROS_status_msgs_motor_msg_h

#include <stdint.h>
#include <string.h>
#include <stdlib.h>
#include "ros/msg.h"

namespace status_msgs
{

  class motor_msg : public ros::Msg
  {
    public:
      typedef float _phase_resistance_type;
      _phase_resistance_type phase_resistance;
      typedef float _phase_inductance_type;
      _phase_inductance_type phase_inductance;
      typedef const char* _error_type;
      _error_type error;

    motor_msg():
      phase_resistance(0),
      phase_inductance(0),
      error("")
    {
    }

    virtual int serialize(unsigned char *outbuffer) const
    {
      int offset = 0;
      union {
        float real;
        uint32_t base;
      } u_phase_resistance;
      u_phase_resistance.real = this->phase_resistance;
      *(outbuffer + offset + 0) = (u_phase_resistance.base >> (8 * 0)) & 0xFF;
      *(outbuffer + offset + 1) = (u_phase_resistance.base >> (8 * 1)) & 0xFF;
      *(outbuffer + offset + 2) = (u_phase_resistance.base >> (8 * 2)) & 0xFF;
      *(outbuffer + offset + 3) = (u_phase_resistance.base >> (8 * 3)) & 0xFF;
      offset += sizeof(this->phase_resistance);
      union {
        float real;
        uint32_t base;
      } u_phase_inductance;
      u_phase_inductance.real = this->phase_inductance;
      *(outbuffer + offset + 0) = (u_phase_inductance.base >> (8 * 0)) & 0xFF;
      *(outbuffer + offset + 1) = (u_phase_inductance.base >> (8 * 1)) & 0xFF;
      *(outbuffer + offset + 2) = (u_phase_inductance.base >> (8 * 2)) & 0xFF;
      *(outbuffer + offset + 3) = (u_phase_inductance.base >> (8 * 3)) & 0xFF;
      offset += sizeof(this->phase_inductance);
      uint32_t length_error = strlen(this->error);
      varToArr(outbuffer + offset, length_error);
      offset += 4;
      memcpy(outbuffer + offset, this->error, length_error);
      offset += length_error;
      return offset;
    }

    virtual int deserialize(unsigned char *inbuffer)
    {
      int offset = 0;
      union {
        float real;
        uint32_t base;
      } u_phase_resistance;
      u_phase_resistance.base = 0;
      u_phase_resistance.base |= ((uint32_t) (*(inbuffer + offset + 0))) << (8 * 0);
      u_phase_resistance.base |= ((uint32_t) (*(inbuffer + offset + 1))) << (8 * 1);
      u_phase_resistance.base |= ((uint32_t) (*(inbuffer + offset + 2))) << (8 * 2);
      u_phase_resistance.base |= ((uint32_t) (*(inbuffer + offset + 3))) << (8 * 3);
      this->phase_resistance = u_phase_resistance.real;
      offset += sizeof(this->phase_resistance);
      union {
        float real;
        uint32_t base;
      } u_phase_inductance;
      u_phase_inductance.base = 0;
      u_phase_inductance.base |= ((uint32_t) (*(inbuffer + offset + 0))) << (8 * 0);
      u_phase_inductance.base |= ((uint32_t) (*(inbuffer + offset + 1))) << (8 * 1);
      u_phase_inductance.base |= ((uint32_t) (*(inbuffer + offset + 2))) << (8 * 2);
      u_phase_inductance.base |= ((uint32_t) (*(inbuffer + offset + 3))) << (8 * 3);
      this->phase_inductance = u_phase_inductance.real;
      offset += sizeof(this->phase_inductance);
      uint32_t length_error;
      arrToVar(length_error, (inbuffer + offset));
      offset += 4;
      for(unsigned int k= offset; k< offset+length_error; ++k){
          inbuffer[k-1]=inbuffer[k];
      }
      inbuffer[offset+length_error-1]=0;
      this->error = (char *)(inbuffer + offset-1);
      offset += length_error;
     return offset;
    }

    const char * getType(){ return "status_msgs/motor_msg"; };
    const char * getMD5(){ return "980b016d63732693ad62ff5fa562b76b"; };

  };

}
#endif
