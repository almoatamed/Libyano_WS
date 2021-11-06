#ifndef _ROS_status_msgs_sensors_msg_h
#define _ROS_status_msgs_sensors_msg_h

#include <stdint.h>
#include <string.h>
#include <stdlib.h>
#include "ros/msg.h"
#include "status_msgs/imu_msg.h"

namespace status_msgs
{

  class sensors_msg : public ros::Msg
  {
    public:
      uint32_t ultrasonic_length;
      typedef uint16_t _ultrasonic_type;
      _ultrasonic_type st_ultrasonic;
      _ultrasonic_type * ultrasonic;
      uint32_t temp_length;
      typedef float _temp_type;
      _temp_type st_temp;
      _temp_type * temp;
      uint32_t humidity_length;
      typedef float _humidity_type;
      _humidity_type st_humidity;
      _humidity_type * humidity;
      uint32_t imu_length;
      typedef status_msgs::imu_msg _imu_type;
      _imu_type st_imu;
      _imu_type * imu;
      uint32_t touch_length;
      typedef uint8_t _touch_type;
      _touch_type st_touch;
      _touch_type * touch;

    sensors_msg():
      ultrasonic_length(0), ultrasonic(NULL),
      temp_length(0), temp(NULL),
      humidity_length(0), humidity(NULL),
      imu_length(0), imu(NULL),
      touch_length(0), touch(NULL)
    {
    }

    virtual int serialize(unsigned char *outbuffer) const
    {
      int offset = 0;
      *(outbuffer + offset + 0) = (this->ultrasonic_length >> (8 * 0)) & 0xFF;
      *(outbuffer + offset + 1) = (this->ultrasonic_length >> (8 * 1)) & 0xFF;
      *(outbuffer + offset + 2) = (this->ultrasonic_length >> (8 * 2)) & 0xFF;
      *(outbuffer + offset + 3) = (this->ultrasonic_length >> (8 * 3)) & 0xFF;
      offset += sizeof(this->ultrasonic_length);
      for( uint32_t i = 0; i < ultrasonic_length; i++){
      *(outbuffer + offset + 0) = (this->ultrasonic[i] >> (8 * 0)) & 0xFF;
      *(outbuffer + offset + 1) = (this->ultrasonic[i] >> (8 * 1)) & 0xFF;
      offset += sizeof(this->ultrasonic[i]);
      }
      *(outbuffer + offset + 0) = (this->temp_length >> (8 * 0)) & 0xFF;
      *(outbuffer + offset + 1) = (this->temp_length >> (8 * 1)) & 0xFF;
      *(outbuffer + offset + 2) = (this->temp_length >> (8 * 2)) & 0xFF;
      *(outbuffer + offset + 3) = (this->temp_length >> (8 * 3)) & 0xFF;
      offset += sizeof(this->temp_length);
      for( uint32_t i = 0; i < temp_length; i++){
      union {
        float real;
        uint32_t base;
      } u_tempi;
      u_tempi.real = this->temp[i];
      *(outbuffer + offset + 0) = (u_tempi.base >> (8 * 0)) & 0xFF;
      *(outbuffer + offset + 1) = (u_tempi.base >> (8 * 1)) & 0xFF;
      *(outbuffer + offset + 2) = (u_tempi.base >> (8 * 2)) & 0xFF;
      *(outbuffer + offset + 3) = (u_tempi.base >> (8 * 3)) & 0xFF;
      offset += sizeof(this->temp[i]);
      }
      *(outbuffer + offset + 0) = (this->humidity_length >> (8 * 0)) & 0xFF;
      *(outbuffer + offset + 1) = (this->humidity_length >> (8 * 1)) & 0xFF;
      *(outbuffer + offset + 2) = (this->humidity_length >> (8 * 2)) & 0xFF;
      *(outbuffer + offset + 3) = (this->humidity_length >> (8 * 3)) & 0xFF;
      offset += sizeof(this->humidity_length);
      for( uint32_t i = 0; i < humidity_length; i++){
      union {
        float real;
        uint32_t base;
      } u_humidityi;
      u_humidityi.real = this->humidity[i];
      *(outbuffer + offset + 0) = (u_humidityi.base >> (8 * 0)) & 0xFF;
      *(outbuffer + offset + 1) = (u_humidityi.base >> (8 * 1)) & 0xFF;
      *(outbuffer + offset + 2) = (u_humidityi.base >> (8 * 2)) & 0xFF;
      *(outbuffer + offset + 3) = (u_humidityi.base >> (8 * 3)) & 0xFF;
      offset += sizeof(this->humidity[i]);
      }
      *(outbuffer + offset + 0) = (this->imu_length >> (8 * 0)) & 0xFF;
      *(outbuffer + offset + 1) = (this->imu_length >> (8 * 1)) & 0xFF;
      *(outbuffer + offset + 2) = (this->imu_length >> (8 * 2)) & 0xFF;
      *(outbuffer + offset + 3) = (this->imu_length >> (8 * 3)) & 0xFF;
      offset += sizeof(this->imu_length);
      for( uint32_t i = 0; i < imu_length; i++){
      offset += this->imu[i].serialize(outbuffer + offset);
      }
      *(outbuffer + offset + 0) = (this->touch_length >> (8 * 0)) & 0xFF;
      *(outbuffer + offset + 1) = (this->touch_length >> (8 * 1)) & 0xFF;
      *(outbuffer + offset + 2) = (this->touch_length >> (8 * 2)) & 0xFF;
      *(outbuffer + offset + 3) = (this->touch_length >> (8 * 3)) & 0xFF;
      offset += sizeof(this->touch_length);
      for( uint32_t i = 0; i < touch_length; i++){
      *(outbuffer + offset + 0) = (this->touch[i] >> (8 * 0)) & 0xFF;
      offset += sizeof(this->touch[i]);
      }
      return offset;
    }

    virtual int deserialize(unsigned char *inbuffer)
    {
      int offset = 0;
      uint32_t ultrasonic_lengthT = ((uint32_t) (*(inbuffer + offset))); 
      ultrasonic_lengthT |= ((uint32_t) (*(inbuffer + offset + 1))) << (8 * 1); 
      ultrasonic_lengthT |= ((uint32_t) (*(inbuffer + offset + 2))) << (8 * 2); 
      ultrasonic_lengthT |= ((uint32_t) (*(inbuffer + offset + 3))) << (8 * 3); 
      offset += sizeof(this->ultrasonic_length);
      if(ultrasonic_lengthT > ultrasonic_length)
        this->ultrasonic = (uint16_t*)realloc(this->ultrasonic, ultrasonic_lengthT * sizeof(uint16_t));
      ultrasonic_length = ultrasonic_lengthT;
      for( uint32_t i = 0; i < ultrasonic_length; i++){
      this->st_ultrasonic =  ((uint16_t) (*(inbuffer + offset)));
      this->st_ultrasonic |= ((uint16_t) (*(inbuffer + offset + 1))) << (8 * 1);
      offset += sizeof(this->st_ultrasonic);
        memcpy( &(this->ultrasonic[i]), &(this->st_ultrasonic), sizeof(uint16_t));
      }
      uint32_t temp_lengthT = ((uint32_t) (*(inbuffer + offset))); 
      temp_lengthT |= ((uint32_t) (*(inbuffer + offset + 1))) << (8 * 1); 
      temp_lengthT |= ((uint32_t) (*(inbuffer + offset + 2))) << (8 * 2); 
      temp_lengthT |= ((uint32_t) (*(inbuffer + offset + 3))) << (8 * 3); 
      offset += sizeof(this->temp_length);
      if(temp_lengthT > temp_length)
        this->temp = (float*)realloc(this->temp, temp_lengthT * sizeof(float));
      temp_length = temp_lengthT;
      for( uint32_t i = 0; i < temp_length; i++){
      union {
        float real;
        uint32_t base;
      } u_st_temp;
      u_st_temp.base = 0;
      u_st_temp.base |= ((uint32_t) (*(inbuffer + offset + 0))) << (8 * 0);
      u_st_temp.base |= ((uint32_t) (*(inbuffer + offset + 1))) << (8 * 1);
      u_st_temp.base |= ((uint32_t) (*(inbuffer + offset + 2))) << (8 * 2);
      u_st_temp.base |= ((uint32_t) (*(inbuffer + offset + 3))) << (8 * 3);
      this->st_temp = u_st_temp.real;
      offset += sizeof(this->st_temp);
        memcpy( &(this->temp[i]), &(this->st_temp), sizeof(float));
      }
      uint32_t humidity_lengthT = ((uint32_t) (*(inbuffer + offset))); 
      humidity_lengthT |= ((uint32_t) (*(inbuffer + offset + 1))) << (8 * 1); 
      humidity_lengthT |= ((uint32_t) (*(inbuffer + offset + 2))) << (8 * 2); 
      humidity_lengthT |= ((uint32_t) (*(inbuffer + offset + 3))) << (8 * 3); 
      offset += sizeof(this->humidity_length);
      if(humidity_lengthT > humidity_length)
        this->humidity = (float*)realloc(this->humidity, humidity_lengthT * sizeof(float));
      humidity_length = humidity_lengthT;
      for( uint32_t i = 0; i < humidity_length; i++){
      union {
        float real;
        uint32_t base;
      } u_st_humidity;
      u_st_humidity.base = 0;
      u_st_humidity.base |= ((uint32_t) (*(inbuffer + offset + 0))) << (8 * 0);
      u_st_humidity.base |= ((uint32_t) (*(inbuffer + offset + 1))) << (8 * 1);
      u_st_humidity.base |= ((uint32_t) (*(inbuffer + offset + 2))) << (8 * 2);
      u_st_humidity.base |= ((uint32_t) (*(inbuffer + offset + 3))) << (8 * 3);
      this->st_humidity = u_st_humidity.real;
      offset += sizeof(this->st_humidity);
        memcpy( &(this->humidity[i]), &(this->st_humidity), sizeof(float));
      }
      uint32_t imu_lengthT = ((uint32_t) (*(inbuffer + offset))); 
      imu_lengthT |= ((uint32_t) (*(inbuffer + offset + 1))) << (8 * 1); 
      imu_lengthT |= ((uint32_t) (*(inbuffer + offset + 2))) << (8 * 2); 
      imu_lengthT |= ((uint32_t) (*(inbuffer + offset + 3))) << (8 * 3); 
      offset += sizeof(this->imu_length);
      if(imu_lengthT > imu_length)
        this->imu = (status_msgs::imu_msg*)realloc(this->imu, imu_lengthT * sizeof(status_msgs::imu_msg));
      imu_length = imu_lengthT;
      for( uint32_t i = 0; i < imu_length; i++){
      offset += this->st_imu.deserialize(inbuffer + offset);
        memcpy( &(this->imu[i]), &(this->st_imu), sizeof(status_msgs::imu_msg));
      }
      uint32_t touch_lengthT = ((uint32_t) (*(inbuffer + offset))); 
      touch_lengthT |= ((uint32_t) (*(inbuffer + offset + 1))) << (8 * 1); 
      touch_lengthT |= ((uint32_t) (*(inbuffer + offset + 2))) << (8 * 2); 
      touch_lengthT |= ((uint32_t) (*(inbuffer + offset + 3))) << (8 * 3); 
      offset += sizeof(this->touch_length);
      if(touch_lengthT > touch_length)
        this->touch = (uint8_t*)realloc(this->touch, touch_lengthT * sizeof(uint8_t));
      touch_length = touch_lengthT;
      for( uint32_t i = 0; i < touch_length; i++){
      this->st_touch =  ((uint8_t) (*(inbuffer + offset)));
      offset += sizeof(this->st_touch);
        memcpy( &(this->touch[i]), &(this->st_touch), sizeof(uint8_t));
      }
     return offset;
    }

    const char * getType(){ return "status_msgs/sensors_msg"; };
    const char * getMD5(){ return "bc23fd84a55f1300861a82f4b4583dc3"; };

  };

}
#endif
