#include "Arduino.h"
#include "ODriveArduino.h"


// Print with stream operator
template<class T> inline Print& operator <<(Print &obj,     T arg) { obj.print(arg);    return obj; }
template<>        inline Print& operator <<(Print &obj, float arg) { obj.print(arg, 4); return obj; }

// ################################ system control ########################################################333

void ODriveArduino::clear_errors(){
    serial_ << "sc"<<'\n';
}

float ODriveArduino::reboot(){
    serial_ << "sr"<<'\n';
    delay(3000);
    return get_voltage();
}
void ODriveArduino::save_config(){
    serial_ << "ss"<<'\n';
}

// ################################ system status ########################################################333

float ODriveArduino::get_voltage(){
    serial_ << "r vbus_voltage"<<'\n';
    return readFloat();
}

String ODriveArduino::get_system_errors(){
    serial_ << "r error"<<'\n';
    return readString();
}

// ################################ axis control ########################################################333

bool ODriveArduino::run_state(int axis, int requested_state, bool wait_for_idle) {
    int timeout_ctr = 100;
    serial_ << "w axis" << axis << ".requested_state " << requested_state << '\n';
    if (wait_for_idle) {
        do {
            delay(100);
            serial_ << "r axis" << axis << ".current_state\n";
        } while (readInt() != AXIS_STATE_IDLE && --timeout_ctr > 0);
    }

    return timeout_ctr > 0;
}

// ################################ axis status ########################################################333


int ODriveArduino::get_current_state(int axis){
    serial_ << "r axis" << axis << ".current_state\n";
}

String ODriveArduino::get_axis_error(int axis){
    serial_ << "r axis" << axis << ".error\n";
    return ODriveArduino::readString();
}


// ################################ motor control ########################################################333

void ODriveArduino::set_pos(int motor_number, float pos) {
    set_pos(motor_number, pos, 0.0f, 0.0f);
}

void ODriveArduino::set_pos(int motor_number, float pos, float vel_feedforward) {
    set_pos(motor_number, pos, vel_feedforward, 0.0f);
}

void ODriveArduino::set_pos(int motor_number, float pos, float vel_feedforward, float current_feedforward) {
    serial_ << "p " << motor_number  << " " << pos << " " << vel_feedforward << " " << current_feedforward << "\n";
}

void ODriveArduino::set_vel(int motor_number, float vel) {
    set_vel(motor_number, vel, 0.0f);
}

void ODriveArduino::set_vel(int motor_number, float vel, float current_feedforward) {
    serial_ << "v " << motor_number  << " " << vel << " " << current_feedforward << "\n";
}

void ODriveArduino::set_current(int motor_number, float current) {
    serial_ << "c " << motor_number << " " << current << "\n";
}

void ODriveArduino::trapezoidal_move(int motor_number, float pos){
    serial_ << "t " << motor_number << " " << pos << "\n";
}

// ################################ motor status ########################################################333

String ODriveArduino::get_motor_error(int axis){
    serial_ << "r axis" << axis << ".motor.error\n";
    return ODriveArduino::readString();
}

float ODriveArduino::get_motor_phase_resistance(int axis){
    serial_ << "r axis" << axis << ".motor.phase_resistance\n";
    return ODriveArduino::readFloat();
}

float ODriveArduino::get_motor_phase_inductance(int axis){
    serial_ << "r axis" << axis << ".motor.phase_inductance\n";
    return ODriveArduino::readFloat();
}

// ################################ encoder status ########################################################333

float ODriveArduino::get_vel(int motor_number){
	serial_<< "r axis" << motor_number << ".encoder.vel_estimate\n";
	return ODriveArduino::readFloat();
}

float ODriveArduino::get_pos(int motor_number){
	serial_<< "r axis" << motor_number << ".encoder.pos_estimate\n";
	return ODriveArduino::readFloat();
}

String ODriveArduino::get_encoder_error(int axis){
    serial_ << "r axis" << axis << ".encoder.error\n";
    return ODriveArduino::readString();
}


// ################################ functionalities ########################################################333

int32_t ODriveArduino::readInt() {
    return readString().toInt();
}

float ODriveArduino::readFloat() {
    return readString().toFloat();
}


String ODriveArduino::readString() {
    String str = "";
    static const unsigned long timeout = 1000;
    unsigned long timeout_start = millis();
    for (;;) {
        while (!serial_.available()) {
            if (millis() - timeout_start >= timeout) {
                return str;
            }
        }
        char c = serial_.read();
        if (c == '\n')
            break;
        str += c;
    }
    return str;
}

