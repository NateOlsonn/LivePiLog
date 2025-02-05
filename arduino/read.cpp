// RPM Measurement
volatile int pulseCount = 0;
unsigned long lastMillis = 0;
int rpm = 0;

void countPulses() {
    pulseCount++;  // Increment on each pulse (rising edge)
}

void setup() {
    Serial.begin(9600);
    
    // RPM sensor setup
    pinMode(2, INPUT_PULLUP);  // Using digital pin 2 for RPM
    attachInterrupt(digitalPinToInterrupt(2), countPulses, RISING);
}

void loop() {
    // Read Analog Sensors
    int mafRaw = analogRead(A0);  // Read MAF sensor
    int afrRaw = analogRead(A1);  // Read AFR sensor
    
    // Convert to voltage
    float mafVoltage = mafRaw * (5.0 / 1023.0);
    float afrVoltage = afrRaw * (5.0 / 1023.0);
    
    // RPM Calculation (every second)
    if (millis() - lastMillis >= 1000) {  // Every 1 second
        rpm = (pulseCount * 60);  // Convert pulses to RPM
        pulseCount = 0;  // Reset counter
        lastMillis = millis();
    }

    // Send CSV-formatted data
    Serial.print(rpm);
    Serial.print(",");
    Serial.print(mafVoltage, 2);  // Print 2 decimal places
    Serial.print(",");
    Serial.println(afrVoltage, 2);

    delay(100);  // Short delay to avoid excessive output
}
