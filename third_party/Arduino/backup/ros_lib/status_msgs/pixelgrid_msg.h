#ifndef _ROS_status_msgs_pixelgrid_msg_h
#define _ROS_status_msgs_pixelgrid_msg_h

#include <stdint.h>
#include <string.h>
#include <stdlib.h>
#include "ros/msg.h"
#include "status_msgs/color_msg.h"

namespace status_msgs
{

  class pixelgrid_msg : public ros::Msg
  {
    public:
      typedef uint8_t _face_type;
      _face_type face;
      typedef status_msgs::color_msg _grid_color_type;
      _grid_color_type grid_color;
      typedef uint8_t _brightness_type;
      _brightness_type brightness;

    pixelgrid_msg():
      face(0),
      grid_color(),
      brightness(0)
    {
    }

    virtual int serialize(unsigned char *outbuffer) const
    {
      int offset = 0;
      *(outbuffer + offset + 0) = (this->face >> (8 * 0)) & 0xFF;
      offset += sizeof(this->face);
      offset += this->grid_color.serialize(outbuffer + offset);
      *(outbuffer + offset + 0) = (this->brightness >> (8 * 0)) & 0xFF;
      offset += sizeof(this->brightness);
      return offset;
    }

    virtual int deserialize(unsigned char *inbuffer)
    {
      int offset = 0;
      this->face =  ((uint8_t) (*(inbuffer + offset)));
      offset += sizeof(this->face);
      offset += this->grid_color.deserialize(inbuffer + offset);
      this->brightness =  ((uint8_t) (*(inbuffer + offset)));
      offset += sizeof(this->brightness);
     return offset;
    }

    const char * getType(){ return "status_msgs/pixelgrid_msg"; };
    const char * getMD5(){ return "b0fb7bc13171ca620842f0b2f559205e"; };

  };

}
#endif
