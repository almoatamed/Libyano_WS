
//SHT30*****************************

// VREF: Analog reference
#define VREF 5.0
#define TEMPERATURE1_PIN A0
#define HUMIDITY1_PIN A1

#define ADC_RESOLUTION 1024
float TEMPERATURE1, Tf1, HUMIDITY1, analogVolt1;


void setup() {
  Serial.begin(115200);
  Serial.println("Starts up.");
}
void loop() {
  
  //***************************************** SHT30
  //-------------------------------------------- T&H 1---UPPER
  analogVolt1 = (float)analogRead(TEMPERATURE1_PIN) / ADC_RESOLUTION * VREF;
  // Convert voltage to temperature (℃, centigrade)
  TEMPERATURE1 = -66.875 + 72.917 * analogVolt1;
  // Convert voltage to temperature (°F, fahrenheit )
  Tf1 = -88.375 + 131.25 * analogVolt1;
  Serial.print("Termperature1:" );
  Serial.print(TEMPERATURE1);
  Serial.print(" C / " );
  Serial.print(Tf1);
  Serial.println(" F" );

  analogVolt1 = (float)analogRead(HUMIDITY1_PIN) / ADC_RESOLUTION * VREF;
  // Convert voltage to relative humidity (%)
  HUMIDITY1 = -12.5 + 41.667 * analogVolt1;

  Serial.print("Humidity1:" );
  Serial.print(HUMIDITY1, 1);
  Serial.println(" %RH" );

  Serial.println();
  delay (999);
}
