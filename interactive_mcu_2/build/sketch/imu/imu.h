#line 1 "/home/salem/catkin_ws/src/interactive_mcu_2/src/interactive_mcu_2/imu/imu.h"
#include <DFRobot_BNO055.h>
#include "Wire.h"

typedef DFRobot_BNO055_IIC    BNO;  
typedef uint8_t u8;
typedef uint32_t u32;

#define SEA_LEVEL_PRESSURE    1015.0f   // sea level pressure


class Imu{
    public:
        u8 BNO055_STATUS = 0; // 0 did not begin, 1 every thing is ok, 2 unknown error, 3 device not detected, 4 device ready timeout, 5 device internal error, any thing else is unkown status
        BNO::sAxisAnalog_t   sAccAnalog, sMagAnalog, sGyrAnalog, sLiaAnalog, sGrvAnalog;
        BNO::sEulAnalog_t    sEulAnalog;
        BNO::sQuaAnalog_t    sQuaAnalog;

        float temp; float altitude; u32 pressure;

        BNO   bno;

        Imu():bno(&Wire, 0x28){}
        
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
            this->init_bno();
        }

        void run(){
            this->run_bno();
        }
};

