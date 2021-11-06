/*
 * Copyright (C) 2020 Hendrik van Essen
 *
 * This file is subject to the terms and conditions of the GNU Lesser
 * General Public License v2.1. See the file LICENSE in the top level
 * directory for more details.
 */

#ifndef DFR0554_H
#define DFR0554_H

#include "LiquidCrystalWired.h"
#include "PCA9633.h"

#define LCD_ADDRESS (0x7c >> 1)
#define RGB_ADDRESS (0xc0 >> 1)

#define ROW_COUNT   2
#define COL_COUNT   16

class DFR0554 : public Print {

public:

    /**
     * Constructor for DFR0554.
     */
    DFR0554();

    /**
     * Initialization.
     *
     * @param wire          Reference to TwoWire for I2C communication
     */
    void begin(TwoWire *wire);

    /**
     * Turn on the display.
     *
     * WARNING: If you call turnOff() twice, without calling turnOn() in between,
     *          then the restored state will be the turned off state!
     */
    void turnOn();

    /**
     * Turn off the display.
     *
     * WARNING: If you call turnOff() twice, without calling turnOn() in between,
     *          then the restored state will be the turned off state!
     */
    void turnOff();

    /**
     * Switch to normal mode.
     *
     * WARNING: If you call sleep() twice, without calling wakeUp() in between,
     *          then the restored state of the rgb background will be the turned
     *          off state!
     */
    void wakeUp();

    /**
     * Switch to low power mode.
     *
     * WARNING: If you call sleep() twice, without calling wakeUp() in between,
     *          then the restored state of the rgb background will be the turned
     *          off state!
     */
    void sleep();



    /* BEGIN OF RGB-ONLY METHODS */
    /**
     * Set individual PWM signal for a given channel.
     *
     * @param regPwm    Register address for PWM channel
     * @param pwm       PWM value
     */
    void setPwm(uint8_t regPwm, uint8_t pwm);

    /**
     * Set global PWM signal.
     *
     * @param pwm   PWM value
     */
    void setGrpPwm(uint8_t pwm);

    /**
     * Set up values for blinking mode. Blinking mode needs to be activated
     * manually by calling setGroupControlMode(GROUP_CONTROL_MODE_BLINKING).
     *
     * @param blinkPeriod   Period for one blink (turning off and on)
     * @param onOffRatio    Value between 0.0 and 1.0, where e.g. a value of
     *                      0.25 means 1/4 of the time the LEDs are on and
     *                      3/4 of the time the LEDs are off
     */
    void setBlinking(uint8_t blinkPeriod, float onOffRatio);

    /**
    * Set PWM values for RGB.
    *
    * @param r  Value for red color channel
    * @param g  Value for green color channel
    * @param b  Value for blue color channel
    */
    void setRGB(uint8_t r, uint8_t g, uint8_t b);

    /**
    * Set PWM values for RGBW. Only available when PCA9633 object was created
    * with the RGBW constructor.
    *
    * @param r  Value for red color channel
    * @param g  Value for green color channel
    * @param b  Value for blue color channel
    * @param w  Value for white color channel
    */
    void setRGBW(uint8_t r, uint8_t g, uint8_t b, uint8_t w);

    /**
    * Set the LED driver output state for a given channel. There are four states:
    *   - LDR_STATE_OFF
    *   - LDR_STATE_ON
    *   - LDR_STATE_IND
    *   - LDR_STATE_IND_GRP
    *
    * @param state  One of the four possible states
    * @param ldrBit Lower bit of LDR* (see BIT_LDR*)
    */
    void setLdrState(uint8_t state, uint8_t ldrBit);

    /**
    * Set the LED driver output state for all channels. There are four states:
    *   - LDR_STATE_OFF
    *   - LDR_STATE_ON
    *   - LDR_STATE_IND
    *   - LDR_STATE_IND_GRP
    *
    * @param state  One of the four possible states
    */
    void setLdrStateAll(uint8_t state);

    /**
    * Set an option for auto increment. There are five options:
    *   - AI_DISABLED
    *   - AI_ALL
    *   - AI_IND
    *   - AI_GBL
    *   - AI_IND_GBL
    *
    * @param option One of the possible five options
    */
    void setAutoIncrement(uint8_t option);

    /**
    * Set the group control mode. There are two modes:
    *   - GROUP_CONTROL_MODE_BLINKING
    *   - GROUP_CONTROL_MODE_DIMMING
    *
    * @param mode   One of the two possible modes
    */
    void setGroupControlMode(uint8_t mode);
    /* END OF RGB-ONLY METHODS */



    /* BEGIN OF LCD-ONLY METHODS */
    /**
     * Clear the display and set the cursor to position (0, 0).
     * ATTENTION: Also changes to setTextInsertionMode(LEFT_TO_RIGHT)
     */
    void clear();

    /**
     * Reset cursor position to (0, 0) and scroll display to original position.
     */
    void returnHome();

    /**
     * Enable or disable automated scrolling.
     *
     * @param enabled   Enable or disable
     */
    void setAutoScrollEnabled(bool enabled);

    /**
     * Enable or disable cursor blinking.
     *
     * @param enabled   Enable or disable
     */
    void setCursorBlinkingEnabled(bool enabled);

    /**
     * Show or hide the cursor.
     *
     * @param visible   Show or hide
     */
    void setCursorVisible(bool visible);

    /**
     * Move the cursor to a given position.
     *
     * @param row   Row of the new cursor position (starting at 0)
     * @param col   Column of the new cursor position (starting at 0)
     */
    void setCursorPosition(uint8_t row, uint8_t col);

    /**
     * Set the direction from which the text is inserted, starting from the cursor.
     *
     * @param mode  Insertion mode
     */
    void setTextInsertionMode(TextInsertionMode mode);

    /**
     * Move the cursor one unit to the left. When the cursor passes the 40th
     * character of the first line and a second line is available, the cursor
     * will move to the second line.
     */
    void moveCursorLeft();

    /**
     * Move the cursor one unit to the right. When the cursor passes the 40th
     * character of the first line and a second line is available, the cursor
     * will move to the second line.
     *
     * NOTE: The cursor respects the setting for the insertion mode and is set
     *       to (1, 0) for LEFT_TO_RIGHT and to (1, COL_MAX) for RIGHT_TO_LEFT.
     */
    void moveCursorRight();

    /**
     * Scroll the entire display content (all lines) one unit to the left.
     *
     * NOTE: The cursor respects the setting for the insertion mode and is set
     *       to (1, 0) for LEFT_TO_RIGHT and to (1, COL_MAX) for RIGHT_TO_LEFT.
     */
    void scrollDisplayLeft();

    /**
     * Scroll the entire display content (all lines) one unit to the right.
     */
    void scrollDisplayRight();

    /*
     * Create a custom symbol.
     * Useful link: https://maxpromer.github.io/LCD-Character-Creator/
     *
     * @param customSymbol  Key to which a custom symbol should be assigned
     * @param charmap       Bitmap definition of the custom symbol
     * */
    void setCustomSymbol(CustomSymbol customSymbol, uint8_t charmap[]);

    /*
     * Print a custom symbol by key reference.
     *
     * @param customSymbol  Key of the custom symbol to be printed
     * */
    void printCustomSymbol(CustomSymbol customSymbol);

    /*
     * Enable or disable the progress bar. When enabled, the last five custom
     * symbols are reserved to display the progress bar (CUSTOM_SYMBOL_4 to
     * CUSTOM_SYMBOL_8) and can't be used. Assignments via setCustomSymbol() to
     * these keys will be ignored. The given line will be reserved completely
     * for the progress bar. Any text written to that line will be overwritten
     * by the progress bar on an update.
     *
     * NOTE: Auto scroll will be disabled and the display will be scrolled to
     * its original position. Don't use scrolling when using the
     * progressbar, otherwise it won't display correctly.
     *
     * NOTE: Text insertion mode will be set to LEFT_TO_RIGHT.
     *
     * @param enabled   Enable or disable
     * */
    void setProgressBarEnabled(bool enabled);

    /*
     * Set the row for displaying the progress bar. Defaults to the last row,
     * according to the given row count in the constructor.
     *
     * @param row    Row where the progress bar is displayed
     * */
    void setProgressBarRow(uint8_t row);

    /*
     * Set the progress of the progress bar and draw the update.
     *
     * NOTE: This function changes the cursor position. You will have to use
     * setCursorPosition in order to return to your required cursor position.
     *
     * @param progress  Progress in percentage (0.0 to 100.0)
     * */
    void setProgress(float progress);
    /* END OF LCD-ONLY METHODS */



    /*
     * Implement virtual function write(uint8_t value) from Arduino's Print class
     *
     * @param value     Data to write
     * */
    virtual size_t write(uint8_t value);

private:

    LiquidCrystalWired _lcd = LiquidCrystalWired(
            ROW_COUNT, COL_COUNT, FONT_SIZE_5x8, BITMODE_8_BIT);
    PCA9633 _rgb = PCA9633(REG_PWM2, REG_PWM1, REG_PWM0);
};

#endif //DFR0554_H
