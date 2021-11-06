
#pragma once

#define VREF 5.0
#define ADC_RESOLUTION 1024

typedef uint8_t u8;
typedef const uint8_t cu8;

class TemperatureAndHumidity{
    public:        
        float temperature_readings[1];
        float humidity_readings[1];
        float temp;
        float voltage_reading;
        float humedity;

        void readall(){
            voltage_reading = ((float)analogRead(A5) / ADC_RESOLUTION * VREF);
            temp = -66.875 + 72.917 * voltage_reading;
            this->temperature_readings[0] = temp;
            voltage_reading = ((float)analogRead(A1) / ADC_RESOLUTION * VREF);
            humedity = -12.5 + 41.667 * voltage_reading;
            this->humidity_readings[0] = humedity;
        }
};
