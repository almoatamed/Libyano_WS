#include <DFRobot_BMP280.h>
#include <DFRobot_BNO055.h>
#include "Wire.h"

typedef DFRobot_BNO055_IIC    BNO;  
typedef DFRobot_BMP280_IIC    BMP;  
typedef uint8_t u8;
typedef uint32_t u32;

#define SEA_LEVEL_PRESSURE    1015.0f   // sea level pressure


class Imu{
    public:
        u8 BMP280_STATUS = 0; // 0 did not begin, 1 every thing is ok, 2 unknown error, 3 device not detected, 4 parameter error, else unkown status    
        u8 BNO055_STATUS = 0; // 0 did not begin, 1 every thing is ok, 2 unknown error, 3 device not detected, 4 device ready timeout, 5 device internal error, any thing else is unkown status
        BNO::sAxisAnalog_t   sAccAnalog, sMagAnalog, sGyrAnalog, sLiaAnalog, sGrvAnalog;
        BNO::sEulAnalog_t    sEulAnalog;
        BNO::sQuaAnalog_t    sQuaAnalog;

        float temp; float altitude; u32 pressure;

        BMP   bmp;
        BNO   bno;

        Imu():bno(&Wire, 0x28), bmp(&Wire, BMP::eSdo_low){}
        
        void init_bmp(){
            this->bmp.reset();
            this->bmp.begin();
            this->set_bmp_status(this->bmp.lastOperateStatus);
        }

        void set_bmp_status(BMP::eStatus_t status)
        {
            switch(status) {
                case BMP::eStatusOK:    this->BMP280_STATUS = 1; break;
                case BMP::eStatusErr:   this->BMP280_STATUS = 2; break;
                case BMP::eStatusErrDeviceNotDetected:    this->BMP280_STATUS = 3; break;
                case BMP::eStatusErrParameter:    this->BMP280_STATUS = 4 ; break;
                default: this->BMP280_STATUS = 5; break;
            }
        }

        void read_bmp(){
            this->temp = this->bmp.getTemperature();
            this->pressure = this->bmp.getPressure();
            this->altitude = this->bmp.calAltitude(SEA_LEVEL_PRESSURE, this->pressure);
        }

        void run_bmp(){
            if(this->BMP280_STATUS ==1){
                this->read_bmp();
            }else{
                this->init_bmp();
            }
        }

        void init_bno(){
            this->bno.reset();
            this->bno.begin();
            this->set_bno_status(this->bno.lastOperateStatus);
        }

        void set_bno_status(BNO::eStatus_t status)
        {
            switch(status) {
                case BNO::eStatusOK:   this->BNO055_STATUS = 1; break;
                case BNO::eStatusErr:  this->BNO055_STATUS = 2; break;
                case BNO::eStatusErrDeviceNotDetect:   this->BNO055_STATUS = 3; break;
                case BNO::eStatusErrDeviceReadyTimeOut:    this->BNO055_STATUS = 4; break;
                case BNO::eStatusErrDeviceStatus:    this->BNO055_STATUS = 5; break;
                default: this->BNO055_STATUS = 6; break;
            }
        }

        void read_bno(){
            this->sAccAnalog = this->bno.getAxis(BNO::eAxisAcc);    // read acceleration
            this->sMagAnalog = this->bno.getAxis(BNO::eAxisMag);    // read geomagnetic
            this->sGyrAnalog = this->bno.getAxis(BNO::eAxisGyr);    // read gyroscope
            this->sLiaAnalog = this->bno.getAxis(BNO::eAxisLia);    // read linear acceleration
            this->sGrvAnalog = this->bno.getAxis(BNO::eAxisGrv);    // read gravity vector
            this->sEulAnalog = this->bno.getEul();                  // read euler angle
            this->sQuaAnalog = this->bno.getQua();                  // read quaternion
        }

        void run_bno(){
            if(this->BNO055_STATUS ==1){
                this->read_bno();
            }else{
                this->init_bno();
            }
        }

        void init(){
            this->init_bmp();
            this->init_bno();
        }

        void run(){
            this->run_bmp();
            // this->run_bno();
        }
};

