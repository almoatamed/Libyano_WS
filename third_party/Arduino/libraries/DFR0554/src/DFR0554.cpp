/*
 * Copyright (C) 2020 Hendrik van Essen
 *
 * This file is subject to the terms and conditions of the GNU Lesser
 * General Public License v2.1. See the file LICENSE in the top level
 * directory for more details.
 */

#include "Arduino.h"

#include "DFR0554.h"

DFR0554::DFR0554() { }

void DFR0554::begin(TwoWire *wire) {
    _lcd.begin(LCD_ADDRESS, wire);
    _rgb.begin(RGB_ADDRESS, wire);
}

void DFR0554::turnOn() {
    _lcd.turnOn();
    _rgb.turnOn();
}

void DFR0554::turnOff() {
    _lcd.turnOff();
    _rgb.turnOff();
}

void DFR0554::wakeUp() {
    _lcd.turnOn();
    _rgb.wakeUp();
}

void DFR0554::sleep() {
    _lcd.turnOff();
    _rgb.sleep();
}

void DFR0554::setPwm(uint8_t regPwm, uint8_t pwm) {
    _rgb.setPwm(regPwm, pwm);
}

void DFR0554::setGrpPwm(uint8_t pwm) {
    _rgb.setGrpPwm(pwm);
}

void DFR0554::setBlinking(uint8_t blinkPeriod, float onOffRatio) {
    _rgb.setBlinking(blinkPeriod, onOffRatio);
}

void DFR0554::setRGB(uint8_t r, uint8_t g, uint8_t b) {
    _rgb.setRGB(r, g, b);
}

void DFR0554::setRGBW(uint8_t r, uint8_t g, uint8_t b, uint8_t w) {
    _rgb.setRGBW(r, g, b, w);
}

void DFR0554::setLdrState(uint8_t state, uint8_t ldrBit) {
    _rgb.setLdrState(state, ldrBit);
}

void DFR0554::setLdrStateAll(uint8_t state) {
    _rgb.setLdrStateAll(state);
}

void DFR0554::setAutoIncrement(uint8_t option) {
    _rgb.setAutoIncrement(option);
}

void DFR0554::setGroupControlMode(uint8_t mode) {
    _rgb.setGroupControlMode(mode);
}

void DFR0554::clear() {
    _lcd.clear();
}

void DFR0554::returnHome() {
    _lcd.returnHome();
}

void DFR0554::setAutoScrollEnabled(bool enabled) {
    _lcd.setAutoScrollEnabled(enabled);
}

void DFR0554::setCursorBlinkingEnabled(bool enabled) {
    _lcd.setCursorBlinkingEnabled(enabled);
}

void DFR0554::setCursorVisible(bool visible) {
    _lcd.setCursorVisible(visible);
}

void DFR0554::setCursorPosition(uint8_t row, uint8_t col) {
    _lcd.setCursorPosition(row, col);
}

void DFR0554::setTextInsertionMode(TextInsertionMode mode) {
    _lcd.setTextInsertionMode(mode);
}

void DFR0554::moveCursorLeft() {
    _lcd.moveCursorLeft();
}

void DFR0554::moveCursorRight() {
    _lcd.moveCursorRight();
}

void DFR0554::scrollDisplayLeft() {
    _lcd.scrollDisplayLeft();
}

void DFR0554::scrollDisplayRight() {
    _lcd.scrollDisplayRight();
}

void DFR0554::setCustomSymbol(CustomSymbol customSymbol, uint8_t charmap[]) {
    _lcd.setCustomSymbol(customSymbol, charmap);
}

void DFR0554::printCustomSymbol(CustomSymbol customSymbol) {
    _lcd.printCustomSymbol(customSymbol);
}

void DFR0554::setProgressBarEnabled(bool enabled) {
    _lcd.setProgressBarEnabled(enabled);
}

void DFR0554::setProgressBarRow(uint8_t row) {
    _lcd.setProgressBarRow(row);
}

void DFR0554::setProgress(float progress) {
    _lcd.setProgress(progress);
}

inline size_t DFR0554::write(uint8_t value) {
    return _lcd.write(value);
}
