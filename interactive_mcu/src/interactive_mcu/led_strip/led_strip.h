#pragma once


class Led_strip
{
public:
    const uint8_t redPin = 5;
    const uint8_t greenPin = 6;
    const uint8_t bluePin = 4;

    const uint8_t redDefault = 149;
    const uint8_t greenDefault = 27;
    const uint8_t blueDefault = 129;
    
    uint8_t red = 149;
    uint8_t green = 27;
    uint8_t blue = 129;

    void init(){
        pinMode(this->redPin, OUTPUT);    //Init Arduino driving pins
        pinMode(this->greenPin, OUTPUT);
        pinMode(this->bluePin, OUTPUT);
        this->setColor(this->redDefault,this->greenDefault,this->blueDefault);
    }   

    void setColor_(uint8_t red, uint8_t green, uint8_t blue)
    {
        analogWrite(this->redPin, red);
        analogWrite(this->greenPin, green);
        analogWrite(this->bluePin, blue);
    }

    void setColor(uint8_t red, uint8_t green, uint8_t blue)
    {
        this->red = red;
        this->green = green;
        this->blue = blue;
        this->setColor_(this->red,this->green,this->blue);
    }

    void setDefaultColor(){
        this->setColor(this->redDefault,this->greenDefault,this->blueDefault);
    }

};
