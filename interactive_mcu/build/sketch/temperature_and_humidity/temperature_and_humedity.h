#line 1 "/home/salem/catkin_ws/src/interactive_mcu/src/interactive_mcu/temperature_and_humidity/temperature_and_humedity.h"

#pragma once

#define VREF 5.0
#define ADC_RESOLUTION 1024

typedef uint8_t u8;
typedef const uint8_t cu8;

cu8 TEMPERATURE_AND_HUMIDITY_BASE_PIN = A9;
cu8 TEMPERATURE_AND_HUMIDITY_END_PIN = A10;

cu8 TEMPERATURE_AND_HUMIDITY_NUMBER = (TEMPERATURE_AND_HUMIDITY_END_PIN - TEMPERATURE_AND_HUMIDITY_BASE_PIN + 1)/2;

class TemperatureAndHumidity{
    public:        
        float temperature_readings[TEMPERATURE_AND_HUMIDITY_NUMBER];
        float humidity_readings[TEMPERATURE_AND_HUMIDITY_NUMBER];
        

        float read_temp_(u8 temperature_sensor_number){
            u8 temp_pin = TEMPERATURE_AND_HUMIDITY_BASE_PIN + 2*(temperature_sensor_number - 1);
            float voltage_reading = ((float)analogRead(temp_pin) / ADC_RESOLUTION * VREF);
            // float temp = -66.875 + 72.917 * voltage_reading;
            float temp = -25.875 + 27.917 * voltage_reading;
            return temp;
        }

        float read_humidity_(u8 humidity_sensor_number){
            u8 humidity_pin = TEMPERATURE_AND_HUMIDITY_BASE_PIN + 2*(humidity_sensor_number - 1) + 1;
            float voltage_reading = ((float)analogRead(humidity_pin) / ADC_RESOLUTION * VREF);
            float humedity = -4.5 + 15.667 * voltage_reading;
            return humedity;
        }

        void readall(){
            for(int i = 1; i<=TEMPERATURE_AND_HUMIDITY_NUMBER;i++){
                this->temperature_readings[i-1] = this->read_temp_(i);
                this->humidity_readings[i-1] = this->read_humidity_(i);
            }
        }
};
