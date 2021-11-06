#pragma once

typedef uint8_t u8;

#define RELAY_PIN_BASE 24
#define RELAY_PIN_END 27

class RelayController
{
    public:
        //void init();
        void init(){
            for(int i=RELAY_PIN_BASE; i<=RELAY_PIN_END; i++){
                pinMode(i,OUTPUT);
            }
        }

        void set(u8 relayNumber, u8 value){
            if (relayNumber >= RELAY_PIN_BASE && relayNumber <= RELAY_PIN_END)
            {
                this->set_(relayNumber, value);
            }
            
        }

        u8 get(u8 relayNumber){
            if (relayNumber >= RELAY_PIN_BASE && relayNumber <= RELAY_PIN_END)
            {
                return digitalRead(relayNumber);
            }
            return 0;
        }   

        void set_(u8 relayNumber, u8 value){
            digitalWrite(relayNumber, value);
        }
};