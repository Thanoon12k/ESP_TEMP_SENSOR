#include <WiFi.h>
#include <HTTPClient.h>

const char* ssid = "هلا"; // Your WiFi SSID
const char* password = "22220000"; // Your WiFi password
const char* googleScriptURL = "https://script.google.com/macros/s/AKfycbzUExULvA-Ij6U85TfbsuPQa8GjFCl96mzTaMGQ1mXZmqEqW8JyiOMRl5RYAutneJkV/exec";

void setup() {
  Serial.begin(115200);
  // Connect to Wi-Fi
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("WiFi connected.");
  Serial.println("IP address: ");
  Serial.println(WiFi.localIP());
}

void loop() {
  // Read sensor values
  int humidityValue = analogRead(34); // Replace with your actual humidity sensor pin
  int heatingValue = analogRead(35); // Replace with your actual heating sensor pin

  // Check Wi-Fi connection

  delay(60000); // Send a request every minute
}

void sendToGoogle(float h, float t, float f, float hic, float hif) {
  if(WiFi.status() == WL_CONNECTED){
    HTTPClient http;
    http.begin(googleScriptURL);

    // Create the URL with the sensor data
    String urlWithSensorData = String(googleScriptURL) + "?humidity=" + String(humidityValue) + "&heating=" + String(heatingValue);

    // Send HTTP GET request
    int httpResponseCode = http.GET();

    if(httpResponseCode > 0) {
      String response = http.getString(); // Get the response to the request
      Serial.println(httpResponseCode);   // Print return code
      Serial.println(response);           // Print request answer
    } else {
      Serial.print("Error on sending GET: ");
      Serial.println(httpResponseCode);
    }

    // Free resources
    http.end();
  }


}
