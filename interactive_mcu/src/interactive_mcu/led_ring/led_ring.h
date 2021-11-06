#pragma once

#include "Adafruit_NeoPixel.h"

typedef uint8_t u8;
typedef const uint8_t cu8;


const uint16_t RING_PIXELS_NUMBER = 95;

const u8 RING_PIXEL_PIN = 3;

#define FLOW_FADEOUTFADEIN 1
#define FLOW_FADEOUT 2
#define FLOW_FADEIN 3
#define FLOW_OFF 4
#define FLOW_LOOP 5

class RingController{
    public:
        Adafruit_NeoPixel pixels;
        u8 flow = 13;
        u8 brighness = 50;
        u8 frame_index = 0;
        uint32_t color = 0;
        u8 roll = 0;
        u8 rolling_index = 0;
        u8 go_back_default = 0;
        u8 default_flow = FLOW_FADEIN;
        u8 is_running = 0;
        unsigned long t_start = 0;
        int period = 10;


    // ########################### FLOWS #######################################################
        // ########################### fadeoutfadein #########################                   
        int fadeoutfadein_number_of_frames = 12;
        // int fadeoutfadein_number_of_frames = 2*(RING_PIXELS_NUMBER/fadeoutfadein_pixels_gap);
        int fadeoutfadein_frames[12][3]= {
            {0,0,1},
            {0,1,9},
            {0,9,21},
            {0,21,37},
            {0,37,61},
            {0,61,93},
            {1,61,93},
            {1,37,61},
            {1,21,37},
            {1,9,21},
            {1,1,9},
            {1,0,1},
        };
        uint32_t fadeoutfadein_default_color = 9771905;
        void fadeoutfadein(){
            if(this->fadeoutfadein_frames[frame_index][0] == 0){
                for(int i = this->fadeoutfadein_frames[frame_index][1]; i< this->fadeoutfadein_frames[frame_index][2]; i++){
                    this->pixels.setPixelColor(i, 0x0);
                }
            }else{
                for(int i = this->fadeoutfadein_frames[frame_index][1]; i< this->fadeoutfadein_frames[frame_index][2]; i++){
                    this->pixels.setPixelColor(i, this->color);
                }
            }
            this->pixels.show();
            this->frame_index+=1;
            if(this->frame_index >= this->fadeoutfadein_number_of_frames){
                if(this->roll != 0){
                    this->rolling_index +=1;
                    if(this->rolling_index >= this->roll){
                        if(this->go_back_default != 0){
                            this->set_flow(this->default_flow,1,0,100,0);
                        }else{
                            this->is_running =0;
                        }
                    }
                }
                this->frame_index = 0;
            }
        }
    // #########################################################################################

        RingController()
        : pixels(RING_PIXELS_NUMBER, RING_PIXEL_PIN, NEO_GRB + NEO_KHZ800) 
        {} 

        void init(){
            this->pixels.begin();
            this->pixels.clear();
            this->pixels.setBrightness(this->brighness);
            this->pixels.show();
        }

        void set_brightness(u8 b){
            this->brighness = b;
            this->pixels.setBrightness(this->brighness);
            this->pixels.show();
        }

        void clear(){
            this->pixels.clear();
            this->pixels.show();
        }

        void set_color(uint32_t color){
            this->color = color;
        }

        void set_flow(u8 flow, u8 roll=0, uint32_t color = 0, int period=200,u8 go_default=0){
            switch (flow)
            {
                case FLOW_FADEOUTFADEIN:
                {
                    this->flow = flow;
                    if(color == 0x00){
                        this->color = this->fadeoutfadein_default_color;
                    }else{
                        this->color = color;
                    }
                    this->is_running = 1;
                    this->frame_index = 0;
                    this->go_back_default = go_default;
                    this->roll = roll;
                    this->rolling_index = 0;
                    this->period = period;
                    break;
                }
                case FLOW_OFF:
                {
                    this->flow = flow;
                    if(color == 0x00){
                        this->color = this->fadeoutfadein_default_color;
                    }else{
                        this->color = color;
                    }
                    this->is_running = 0;
                    this->frame_index = 0;
                    this->go_back_default = go_default;
                    this->roll = roll;
                    this->rolling_index = 0;
                    this->period = period;
                    this->pixels.clear();
                    this->pixels.show();
                    break;
                }
                default:
                    break;
            }
        }

        void switch_frame(){
            switch (this->flow)
            {
                case FLOW_FADEOUTFADEIN:
                {
                    this->fadeoutfadein();
                    break;
                }
                case FLOW_OFF:
                {
                    break;
                }
                default:
                    break;
            }
        }

        void run_frame(){
            unsigned long  current_time = millis();
            if(current_time - this->t_start > this->period){  
                this->t_start = current_time;   
                this->switch_frame();
            }
        }

        void run(){
            if(this->roll == 0){
                this->run_frame();
            }else{
                if(this->rolling_index < this->roll){
                    this->run_frame();
                }
            }
        }
    
};