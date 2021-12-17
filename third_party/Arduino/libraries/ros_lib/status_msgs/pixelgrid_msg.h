#ifndef _ROS_status_msgs_pixelgrid_msg_h
#define _ROS_status_msgs_pixelgrid_msg_h

#include <stdint.h>
#include <string.h>
#include <stdlib.h>
#include "ros/msg.h"

namespace status_msgs
{

  class pixelgrid_msg : public ros::Msg
  {
    public:
      typedef uint8_t _face_type;
      _face_type face;
      typedef uint32_t _grid_color_type;
      _grid_color_type grid_color;
      typedef uint8_t _brightness_type;
      _brightness_type brightness;
      typedef uint8_t _is_running_type;
      _is_running_type is_running;

    pixelgrid_msg():
      face(0),
      grid_color(0),
      brightness(0),
      is_running(0)
    {
    }

    virtual int serialize(unsigned char *outbuffer) const
    {
      int offset = 0;
      *(outbuffer + offset + 0) = (this->face >> (8 * 0)) & 0xFF;
      offset += sizeof(this->face);
      *(outbuffer + offset + 0) = (this->grid_color >> (8 * 0)) & 0xFF;
      *(outbuffer + offset + 1) = (this->grid_color >> (8 * 1)) & 0xFF;
      *(outbuffer + offset + 2) = (this->grid_color >> (8 * 2)) & 0xFF;
      *(outbuffer + offset + 3) = (this->grid_color >> (8 * 3)) & 0xFF;
      offset += sizeof(this->grid_color);
      *(outbuffer + offset + 0) = (this->brightness >> (8 * 0)) & 0xFF;
      offset += sizeof(this->brightness);
      *(outbuffer + offset + 0) = (this->is_running >> (8 * 0)) & 0xFF;
      offset += sizeof(this->is_running);
      return offset;
    }

    virtual int deserialize(unsigned char *inbuffer)
    {
      int offset = 0;
      this->face =  ((uint8_t) (*(inbuffer + offset)));
      offset += sizeof(this->face);
      this->grid_color =  ((uint32_t) (*(inbuffer + offset)));
      this->grid_color |= ((uint32_t) (*(inbuffer + offset + 1))) << (8 * 1);
      this->grid_color |= ((uint32_t) (*(inbuffer + offset + 2))) << (8 * 2);
      this->grid_color |= ((uint32_t) (*(inbuffer + offset + 3))) << (8 * 3);
      offset += sizeof(this->grid_color);
      this->brightness =  ((uint8_t) (*(inbuffer + offset)));
      offset += sizeof(this->brightness);
      this->is_running =  ((uint8_t) (*(inbuffer + offset)));
      offset += sizeof(this->is_running);
     return offset;
    }

    const char * getType(){ return "status_msgs/pixelgrid_msg"; };
    const char * getMD5(){ return "a56e5b01ee575c2bce6c35f4176c183f"; };

  };

}
#endif
