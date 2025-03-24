from datetime import datetime, timedelta
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
from datetime import datetime, timedelta

def construct_lists(data):
   
    print(len(data))
   
    parsed_data = [
        {
            "datetime": datetime.strptime(f"{row['Date'][:10]} {row['Time'][11:19]}", "%Y-%m-%d %H:%M:%S"),
            "temperature": row['Tempreature'],
            "humidity": row['Humidity'],
            "source": row['Source']
        }
        for row in data
    ]

    # Get the last reading (now_value)
    now_value = parsed_data[-1]["temperature"]
    now_time = parsed_data[-1]["datetime"]

    # Helper function to filter readings by a specific condition
    def filter_by_condition(condition):
        return [entry["temperature"] for entry in parsed_data if condition(entry)]

    # Construct monthly_readings (last 30 temp values with identical month)
    monthly_readings = filter_by_condition(
        lambda entry: entry["datetime"].month == now_time.month
    )[-30:]

    # Construct weekly_readings (last 4 temp values with identical day or month)
    weekly_readings = filter_by_condition(
        lambda entry: entry["datetime"].day == now_time.day or entry["datetime"].month == now_time.month
    )[-4:]

    # Construct daily_readings (last 24 temp readings with identical day_number)
    daily_readings = filter_by_condition(
        lambda entry: entry["datetime"].day == now_time.day
    )[-24:]

    # Construct hourly_readings (last 24 temp readings with identical hour)
    hourly_readings = filter_by_condition(
        lambda entry: entry["datetime"].hour == now_time.hour
    )[-24:]

    # Construct minutly_readings (last 60 readings with identical minute)
    minutly_readings = filter_by_condition(
        lambda entry: entry["datetime"].minute == now_time.minute
    )[-60:]

    # Construct secondly_reading (last 60 readings with identical second or minute)
    secondly_reading = filter_by_condition(
        lambda entry: entry["datetime"].second == now_time.second or entry["datetime"].minute == now_time.minute
    )[-60:]

    # Return the constructed dictionary
    return {
        "now": now_value,
        "monthly_readings": monthly_readings,
        "weekly_readings": weekly_readings,
        "daily_readings": daily_readings,
        "hourly_readings": hourly_readings,
        "minutly_readings": minutly_readings,
        "secondly_reading": secondly_reading,
    }


# Example usage
if __name__ == '__main__':
    # Replace this with your actual function to get data
    data = get_data_from_sheet()
    reconstructed_data = construct_lists(data)
    print(reconstructed_data)
