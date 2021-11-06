#ifndef ODriveArduino_h
#define ODriveArduino_h

#include "Arduino.h"

class ODriveArduino {
public:
    enum AxisState_t {
        AXIS_STATE_UNDEFINED = 0,           //<! will fall through to idle
        AXIS_STATE_IDLE = 1,                //<! disable PWM and do nothing
        AXIS_STATE_STARTUP_SEQUENCE = 2, //<! the actual sequence is defined by the config.startup_... flags
        AXIS_STATE_FULL_CALIBRATION_SEQUENCE = 3,   //<! run all calibration procedures, then idle
        AXIS_STATE_MOTOR_CALIBRATION = 4,   //<! run motor calibration
        AXIS_STATE_SENSORLESS_CONTROL = 5,  //<! run sensorless control
        AXIS_STATE_ENCODER_INDEX_SEARCH = 6, //<! run encoder index search
        AXIS_STATE_ENCODER_OFFSET_CALIBRATION = 7, //<! run encoder offset calibration
        AXIS_STATE_CLOSED_LOOP_CONTROL = 8  //<! run closed loop control
    };

    // system   
    ODriveArduino(Stream& serial): serial_(serial){}

    float reboot();
    void clear_errors();
    void save_config();

    float get_voltage();
    String get_system_errors();
    
    // axis
    bool run_state(int axis, int requested_state, bool wait_for_idle);
    
    int get_current_state(int axis);
    String get_axis_error(int axis);
    
    //motro 
    void set_pos(int motor_number, float pos);
    void set_pos(int motor_number, float pos, float vel_feedforward);
    void set_pos(int motor_number, float pos, float vel_feedforward, float cureent_feedforward);
    void set_vel(int motor_number, float vel);
    void set_vel(int motor_number, float vel, float current_feedforward);
    void set_current(int motor_number, float current);
    void trapezoidal_move(int motor_number, float pos);

    String get_motor_error( int motor_number);
    float get_motor_phase_resistance(int motor_number); 
    float get_motor_phase_inductance(int motor_number); 

    //encoder
    float get_vel(int axis);
    float get_pos(int axis);
    String get_encoder_error(int axis);


private:
    String readString();
    int32_t readInt();
    float readFloat();
    Stream& serial_;
};

#endif //ODriveArduino_h
