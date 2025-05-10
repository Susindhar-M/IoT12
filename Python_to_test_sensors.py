#Sensor test functions

import grovepi
import time

# Sensor ports (update if connected differently)
LIGHT_SENSOR = 0          # A0
SOUND_SENSOR = 1          # A1
ANGLE_SENSOR = 2          # A2
TEMP_HUM_SENSOR = 4       # D4
PIR_SENSOR = 7            # D7

# Light Sensor Test

def test_light_sensor():
    try:
        value = grovepi.analogRead(LIGHT_SENSOR)
        print(f"Light Sensor Reading: {value}")
    except Exception as e:
        print("Error reading light sensor:", e)


# Sound Sensor Test

def test_sound_sensor():
    try:
        value = grovepi.analogRead(SOUND_SENSOR)
        print(f"Sound Sensor Reading: {value}")
    except Exception as e:
        print("Error reading sound sensor:", e)


# Angle Sensor Test

def test_angle_sensor():
    try:
        value = grovepi.analogRead(ANGLE_SENSOR)
        print(f"Angle Sensor Reading: {value}")
    except Exception as e:
        print("Error reading angle sensor:", e)


# Temperature and Humidity Sensor Test

def test_temp_humidity():
    try:
        temp, humidity = grovepi.dht(TEMP_HUM_SENSOR, 0)  # 0 for DHT11, 1 for DHT22
        print(f"Temperature: {temp:.1f}°C, Humidity: {humidity:.1f}%")
    except Exception as e:
        print("Error reading temperature and humidity sensor:", e)


# PIR Motion Sensor Test

def test_pir_sensor():
    try:
        grovepi.pinMode(PIR_SENSOR, "INPUT")
        value = grovepi.digitalRead(PIR_SENSOR)
        print("Motion Detected!" if value else "No Motion")
    except Exception as e:
        print("Error reading PIR sensor:", e)


# Test All Sensors

def test_all_sensors():
    print("\n--- Sensor Test Start ---")
    test_light_sensor()
    test_sound_sensor()
    test_angle_sensor()
    test_temp_humidity()
    test_pir_sensor()
    print("--- Sensor Test Complete ---\n")

# Example: run the test every 5 seconds
if __name__ == "__main__":
    while True:
        test_all_sensors()
        time.sleep(5)
