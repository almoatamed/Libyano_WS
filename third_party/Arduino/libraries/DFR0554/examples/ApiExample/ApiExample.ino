/*
 * Copyright (C) 2020 Hendrik van Essen
 *
 * This file is subject to the terms and conditions of the GNU Lesser
 * General Public License v2.1. See the file LICENSE in the top level
 * directory for more details.
 */

#include "Arduino.h"
#include "DFR0554.h"

DFR0554 dfr0554 = DFR0554();

byte customCharHeart[] = {
        0b00000,
        0b00000,
        0b01010,
        0b11111,
        0b11111,
        0b01110,
        0b00100,
        0b00000,
};

void lcd() {
    // 1. custom symbol
    dfr0554.print("Hello world! ");
    dfr0554.printCustomSymbol(CUSTOM_SYMBOL_1);
    delay(1000);

    // 2.a scroll right with text insertion following LEFT_TO_RIGHT
    dfr0554.clear();
    dfr0554.setTextInsertionMode(LEFT_TO_RIGHT);
    dfr0554.print("scroll right");
    delay(500);

    for (int i = 0; i < 4; i++) {
        dfr0554.scrollDisplayRight();
        delay(500);
    }

    // 2.b scroll left with text insertion following RIGHT_TO_LEFT
    dfr0554.clear();
    dfr0554.setTextInsertionMode(RIGHT_TO_LEFT);
    dfr0554.setCursorPosition(0, COL_COUNT - 1);
    dfr0554.print("tfel llorcs");
    delay(500);

    for (int i = 0; i < 5; i++) {
        dfr0554.scrollDisplayLeft();
        delay(500);
    }
    dfr0554.setTextInsertionMode(LEFT_TO_RIGHT);

    // 3. turning on/off display
    dfr0554.clear();
    dfr0554.print("turning off...");
    delay(1000);
    dfr0554.turnOff();
    delay(1000);

    dfr0554.clear();
    dfr0554.print("turned on again");
    dfr0554.turnOn();
    delay(1000);

    // 4. autoscroll
    dfr0554.clear();

    if (ROW_COUNT > 1) {
        dfr0554.setCursorPosition(1, 0);
        dfr0554.print("This is also a very long line");
    }

    dfr0554.setCursorPosition(0, COL_COUNT);
    dfr0554.setAutoScrollEnabled(true);

    String longLine = "This is a very long line";
    for (int i = 0; i < longLine.length(); i++) {
        dfr0554.print(longLine.charAt(i));
        delay(250);
    }
    dfr0554.setAutoScrollEnabled(false);
    delay(2000);

    // 5. return home
    dfr0554.returnHome();
    delay(1000);

    // 6. cursor blinking
    dfr0554.clear();
    dfr0554.setCursorBlinkingEnabled(true);
    delay(2000);

    for (int i = 0; i < COL_COUNT; i++) {

        if (i == (int) (COL_COUNT / 2)) {
            dfr0554.setCursorBlinkingEnabled(false);
        }

        if (i == (int) (COL_COUNT / 2) + 2) {
            dfr0554.setCursorBlinkingEnabled(true);
        }

        dfr0554.setCursorPosition(0, i);
        delay(500);
    }
    delay(1000);
    dfr0554.returnHome();
    delay(500);
    dfr0554.setCursorBlinkingEnabled(false);

    // 7. show and move cursor
    dfr0554.setCursorVisible(true);
    dfr0554.clear();
    delay(1000);
    for (int i = 0; i <= 9; i++) {
        dfr0554.print(i);
        delay(250);
    }

    dfr0554.returnHome();
    delay(100);
    for(int i = 0; i < 50; i++) {
        dfr0554.moveCursorRight();
        delay(100);
    }
    for(int i = 50; i > 0 ; i--) {
        dfr0554.moveCursorLeft();
        delay(100);
    }

    dfr0554.setCursorVisible(false);
    dfr0554.clear();

    /* 8. write 10 characters on the next line (if available), because 40
     * characters per line is the maximum */
    if (ROW_COUNT > 1) {
        dfr0554.clear();
        dfr0554.setTextInsertionMode(LEFT_TO_RIGHT);
        for (int i = 0; i < 50; i++) {
            if (i % 2 == 0) {
                dfr0554.print("A");
            }
            else {
                dfr0554.print("B");
            }

            delay(100);
        }

        dfr0554.clear();
        dfr0554.setTextInsertionMode(RIGHT_TO_LEFT);
        dfr0554.setCursorPosition(0, COL_COUNT - 1);
        for (int i = 0; i < 50; i++) {
            if (i % 2 == 0) {
                dfr0554.print("X");
            }
            else {
                dfr0554.print("Y");
            }

            delay(100);
        }
    }

    dfr0554.clear();

    // 9. progress bar
    dfr0554.setProgressBarEnabled(true);
    dfr0554.setCursorPosition(0, 0);
    dfr0554.print("Progress: ");

    for (int j = 0; j <= 100; j++) {

        dfr0554.setCursorPosition(0, 10);

        #ifdef __AVR__
            char string_rep[6];
            sprintf(string_rep, "%d %%", j);
            dfr0554.print(string_rep);
        #else
            // on an esp32 you can use printf instead
            dfr0554.printf("%d %%", j);
        #endif

        dfr0554.setProgress(j);
        delay(100);
    }
    dfr0554.setProgressBarEnabled(false);
    dfr0554.clear();
}

void rgb() {

    dfr0554.setRGB(255, 255, 255);
    delay(500);

    // 1. turn on/off
    dfr0554.turnOff();
    delay(500);

    dfr0554.turnOn();
    delay(500);

    // 2. individual dimming (setRGB() uses setPwm() internally)
    dfr0554.setRGB(255, 255, 255);
    delay(500);

    dfr0554.setRGB(255, 0, 0);
    delay(500);

    dfr0554.setRGB(0, 255, 0);
    delay(500);

    dfr0554.setRGB(0, 0, 255);
    delay(500);

    // 3. group dimming
    dfr0554.setRGB(255, 255, 255);
    dfr0554.setLdrStateAll(LDR_STATE_IND_GRP);

    for (int pwm = 255; pwm >= 0; pwm--) {
        dfr0554.setGrpPwm(pwm);
        delay(20);
    }
    delay(1000);

    // 4. changing ldr state
    dfr0554.setGrpPwm(255);
    dfr0554.setRGB(255, 255, 255);
    dfr0554.setLdrState(LDR_STATE_OFF, BIT_LDR1);
    // color should be magenta
    delay(500);

    dfr0554.setGrpPwm(0);
    dfr0554.setRGB(0, 0, 0);
    dfr0554.setLdrState(LDR_STATE_ON, BIT_LDR1);
    // color should be green
    delay(500);

    dfr0554.setGrpPwm(255);
    dfr0554.setRGB(255, 128, 0);
    dfr0554.setLdrState(LDR_STATE_IND, BIT_LDR1);
    // color should be orange
    delay(500);

    dfr0554.setGrpPwm(0);
    dfr0554.setRGB(255, 255, 255);
    dfr0554.setLdrState(LDR_STATE_IND_GRP, BIT_LDR1);
    // should be no color at all
    delay(500);

    // 5. test blinking
    dfr0554.setGrpPwm(255);
    dfr0554.setRGB(255, 255, 255);
    dfr0554.setGroupControlMode(GROUP_CONTROL_MODE_BLINKING);
    dfr0554.setBlinking(BLINKING_PERIOD_1_S, BLINKING_RATIO_BALANCED);
    delay(10000);
    dfr0554.setGroupControlMode(GROUP_CONTROL_MODE_DIMMING);

    // 6. sleep mode
    dfr0554.setRGB(0, 255, 255);
    delay(500);

    dfr0554.sleep();
    delay(2000);

    dfr0554.wakeUp();
    delay(500);
}

void setup() {
    Serial.begin(115200);
    dfr0554.begin(&Wire);

    dfr0554.setCustomSymbol(CUSTOM_SYMBOL_1, customCharHeart);

    dfr0554.turnOn();
    dfr0554.setLdrStateAll(LDR_STATE_IND_GRP);
    dfr0554.setGroupControlMode(GROUP_CONTROL_MODE_DIMMING);
    dfr0554.setRGB(255, 255, 255);
}

void loop() {
    dfr0554.clear();
    lcd();

    dfr0554.print("TESTING RGB");
    rgb();
}
