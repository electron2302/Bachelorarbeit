/* 
 * Meant to be flashed onto an ESP8266 and be conectetd to the same network as the test Pi (via WIFI).
 * 
 * After startup this code sends a udp packaeg and then trys to go into deep sleep
 * 
 */

#include <ESP8266WiFi.h>
#include <WiFiUdp.h>
   
// Set WiFi credentials
#define WIFI_SSID "WIFI"
#define WIFI_PASS "password1234567890"

//remote
#define RECIVER_IP "10.10.10.21"
#define UDP_PORT 6666

#define PIN_SHOW_WIFI_SETUP 4 //D2 -> ppk2 D0
#define PIN_SHOW_RECEIVED 5   //D1 -> ppk2 D1

WiFiUDP Udp;

char  ReplyBuffer[] = "Hi";       // a string to send back

void setup() {
  pinMode(PIN_SHOW_WIFI_SETUP, OUTPUT);
  pinMode(PIN_SHOW_RECEIVED, OUTPUT);
  digitalWrite(PIN_SHOW_WIFI_SETUP, LOW);
  digitalWrite(PIN_SHOW_RECEIVED, HIGH);

  
  // Setup serial port
  Serial.begin(74880);
  Serial.println();
   
  // Begin WiFi
  digitalWrite(PIN_SHOW_WIFI_SETUP, HIGH);
  WiFi.begin(WIFI_SSID, WIFI_PASS);
   
  // Connecting to WiFi...
  Serial.print("Connecting to ");
  Serial.print(WIFI_SSID);
  // Loop continuously while WiFi is not connected
  int count = 0;
  while (WiFi.status() != WL_CONNECTED)
  {
    count++;
    if(count > 32){
      WiFi.begin(WIFI_SSID, WIFI_PASS);
      count = 0;
    }
    delay(500);
    Serial.print(".");
  }
   
  // Connected to WiFi
  Serial.println();
  Serial.print("Connected! IP address: ");
  Serial.println(WiFi.localIP());
  digitalWrite(PIN_SHOW_WIFI_SETUP, LOW);

  Udp.beginPacket(RECIVER_IP, UDP_PORT);
  Udp.write(ReplyBuffer);
  Udp.endPacket();
  Serial.println("sended");

  delay(10);
  digitalWrite(PIN_SHOW_RECEIVED, LOW);
  ESP.deepSleep(0);
   
}
   
void loop() {  
  ESP.deepSleep(0);  // should never reach this, but just for good measure
  Serial.println("Error"); // should never reach this
  delay(500);            
}
