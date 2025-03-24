from datetime import datetime
from flask import jsonify
import requests


# Google Apps Script URL
GOOGLE_SCRIPT_URL = "https://script.googleusercontent.com/macros/echo?user_content_key=AehSKLidia3sk1OBo5TMUlG3p5ua2bLMBFs0djsRNdu8l5bUq6x3NKozHQbL1mfDEzXKuHUBCqb_4KmZoiGC6sekfopMv8Iikfq2pjKMKEIETUeSLq-YFHAEyo9nKJBFyZGoC2GufXKCFp8PCjIZtfRi1mPUqn5BXPgiKt7oiqarwW-k3ZuEhAKwS1A_1N9XKS2sXziV13yOBA9MvoyjlW1eykDMfiNv78PRZv738jSHKeJTRn176ovu_gOoJpUKonN8x_ytQiGB7ElFWWfXJh8xUOI-ckZD2w&lib=MBmmrBXDVD4wOkIb81o--wOKnFQueNhEk"

def get_data_from_sheet():
    try:
        response = requests.get(GOOGLE_SCRIPT_URL)
        if response.status_code == 200:
            data = response.json()  # Parse JSON response 
            return data
        else:
            return jsonify({"error": f"Failed to fetch data, status code: {response.status_code}"})
    except Exception as e:
        return jsonify({"error": str(e)})



def construct_lists(data):
    print(len(data))

    # Parse and organize the data
    parsed_data = [
        {
            "datetime": datetime.strptime(f"{row['Date'][:10]} {row['Time'][11:19]}", "%Y-%m-%d %H:%M:%S"),
            "temperature": row['Tempreature'],
            "humidity": row['Humidity']
        }
        for row in data
    ]

    # Get the last reading values
    now_temp = parsed_data[-1]["temperature"]
    now_humidity = parsed_data[-1]["humidity"]
    now_time = parsed_data[-1]["datetime"]

    # Helper function to filter readings by a specific condition
    def filter_by_condition(condition, key):
        return [entry[key] for entry in parsed_data if condition(entry)]

    # Construct temperature readings
    temp_monthly = filter_by_condition(
        lambda entry: entry["datetime"].month == now_time.month, "temperature"
    )[-30:]
    temp_weekly = filter_by_condition(
        lambda entry: entry["datetime"].day == now_time.day or entry["datetime"].month == now_time.month, "temperature"
    )[-4:]
    temp_daily = filter_by_condition(
        lambda entry: entry["datetime"].day == now_time.day, "temperature"
    )[-24:]
    temp_hourly = filter_by_condition(
        lambda entry: entry["datetime"].hour == now_time.hour, "temperature"
    )[-24:]
    temp_minutely = filter_by_condition(
        lambda entry: entry["datetime"].minute == now_time.minute, "temperature"
    )[-60:]
    temp_secondly = filter_by_condition(
        lambda entry: entry["datetime"].second == now_time.second or entry["datetime"].minute == now_time.minute, "temperature"
    )[-60:]

    # Construct humidity readings
    hum_monthly = filter_by_condition(
        lambda entry: entry["datetime"].month == now_time.month, "humidity"
    )[-30:]
    hum_weekly = filter_by_condition(
        lambda entry: entry["datetime"].day == now_time.day or entry["datetime"].month == now_time.month, "humidity"
    )[-4:]
    hum_daily = filter_by_condition(
        lambda entry: entry["datetime"].day == now_time.day, "humidity"
    )[-24:]
    hum_hourly = filter_by_condition(
        lambda entry: entry["datetime"].hour == now_time.hour, "humidity"
    )[-24:]
    hum_minutely = filter_by_condition(
        lambda entry: entry["datetime"].minute == now_time.minute, "humidity"
    )[-60:]
    hum_secondly = filter_by_condition(
        lambda entry: entry["datetime"].second == now_time.second or entry["datetime"].minute == now_time.minute, "humidity"
    )[-60:]

    # Construct and return both dictionaries
    temp_readings_dict = {
        "now": now_temp,
        "monthly_readings": temp_monthly,
        "weekly_readings": temp_weekly,
        "daily_readings": temp_daily,
        "hourly_readings": temp_hourly,
        "minutely_readings": temp_minutely,
        "secondly_reading": temp_secondly,
    }

    humidity_readings_dict = {
        "now": now_humidity,
        "monthly_readings": hum_monthly,
        "weekly_readings": hum_weekly,
        "daily_readings": hum_daily,
        "hourly_readings": hum_hourly,
        "minutely_readings": hum_minutely,
        "secondly_reading": hum_secondly,
    }

    return temp_readings_dict, humidity_readings_dict


# Example usage
if __name__ == '__main__':
    # Replace this with your actual function to get data
    data = get_data_from_sheet()
    temp_readings, humidity_readings = construct_lists(data)
    print("Temperature Readings:", temp_readings)
    print("Humidity Readings:", humidity_readings)
