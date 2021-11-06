#include <Arduino_EdgeControl.h>

constexpr unsigned int calibResistor { 7870 };

void setup()
{
    Serial.begin(115200);

    auto startNow = millis() + 2500;
    while (!Serial && millis() < startNow)
        ;

    delay(2000);

    Serial.println("Hello, 10k");

    Power.enable3V3();
    Power.enable5V();

    Wire.begin();
    Expander.begin();

    Serial.print("Waiting for IO Expander Initialisation...");
    while (!Expander) {
        Serial.print(".");
        delay(100);
    }
    Serial.println(" done.");

    Watermark.begin();
    Serial.println("Watermark OK");

    Watermark.calibrationMode(OUTPUT);
    Watermark.calibrationWrite(LOW);

    Watermark.commonMode(OUTPUT);
    Watermark.commonWrite(HIGH);

    Watermark.enable();
}

void loop()
{
    auto val = wmkAvgAnalogRead(WATERMARK_CH01);
    Serial.print("Watermark Channel 01");
    Serial.print(" - average analogRead value: ");
    Serial.print(val);
    Serial.print(" -  Calculated Resistor: ");
    Serial.println(calibResistor * (1023 - val) / val);

    delay(1000);
}

int wmkAvgAnalogRead(pin_size_t pin)
{
    constexpr size_t count { 10 };
    unsigned int sum;

    for (auto i = 0; i < count; i ++)
        sum += Watermark.analogRead(pin);

    return sum / count;
}