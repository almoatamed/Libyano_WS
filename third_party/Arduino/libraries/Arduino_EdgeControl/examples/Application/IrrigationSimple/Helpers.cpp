#include "Helpers.h"

/**
 * Set system and TimeAlarm clock from compile datetime or RTC
 */
void setSystemClock(String compileDate, String compileTime)
{
    // Retrieve clock time from compile date...
    auto buildTime = compileDateTimeToSystemTime(compileDate, compileTime, true, 2);
    // ... ore use the one from integrated RTC.
    auto rtcTime = time(NULL);

    // Remeber to connect at least the CR2032 battery
    // to keep the RTC running.
    auto actualTime = rtcTime > buildTime ? rtcTime : buildTime;

    // Set both system time and the alarms one
    set_time(actualTime);
    setTime(actualTime);

    Serial.print("Compile Date and Time: ");
    Serial.println(getLocaltime(buildTime));
    Serial.print("RTC Date and Time:     ");
    Serial.println(getLocaltime(rtcTime));
    Serial.print("System Clock:          ");
    Serial.println(getLocaltime());
}

void statusPrint()
{
    String msg;

    Serial.println("Measures...");

    msg = "Moisture [";
    msg += dataPoints.size();
    msg += "]";
    Serial.println(msg);

    msg = "Latest: ";
    auto d = dataPoints.back();
    msg += d.moistureP;
    msg += "%";
    Serial.println(msg);

    Serial.println("Loaded Tasks...");

    msg = "Custom: ";
    msg += alarmTabIDs.size();
    Serial.println(msg);

    msg = "Sketch: ";
    msg += alarmSketchIDs.size();
    Serial.println(msg);
}

float getAverage05VRead(int pin)
{
    constexpr size_t loops { 10 };
    constexpr float toV { 3.3f / float { (1 << ADC_RESOLUTION) - 1 } };

    // Resistor divider on Input ports
    constexpr float rDiv { 17.4f / (10.0f + 17.4f) };

    int tot { 0 };

    analogReadResolution(ADC_RESOLUTION);

    Input.enable();
    for (auto i = 0; i < loops; i++)
        tot += Input.analogRead(pin);
    Input.disable();

    const auto avg = float { tot } * toV / float { loops };

    return avg / rDiv;
}

int getAverageInputRead(int pin, const size_t loops)
{
    unsigned int tot { 0 };

    analogReadResolution(ADC_RESOLUTION);

    Input.enable();
    for (auto i = 0; i < loops; i++)
        tot += Input.analogRead(pin);
    Input.disable();

    return tot / loops;
}

int getMoisturePerc(int pin)
{
    // Keep track ok dry/wet values. YMMV.
    static long dryValue { 2160 };
    static long wetValue { 975 };

    auto val = getAverageInputRead(pin);

    // Self-update dry/wet values range.
    if (val > dryValue)
        dryValue = val;
    if (val < wetValue)
        wetValue = val;

    auto perc = map(val, dryValue, wetValue, 0, 100);

    return perc;
}
