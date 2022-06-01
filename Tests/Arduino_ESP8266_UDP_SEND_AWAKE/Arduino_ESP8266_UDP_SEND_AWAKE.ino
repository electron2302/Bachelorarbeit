/* 
 * Meant to be flashed onto an ESP8266 and be conectetd to the same network as the test Pi (via WIFI).
 * Also PIN 14 / D5 should be connected to the Pi.
 */

#include <ESP8266WiFi.h>
#include <WiFiUdp.h>
   
// Set WiFi credentials
#define WIFI_SSID "WIFI"
#define WIFI_PASS "password1234567890"

//remote
#define RECIVER_IP "10.10.10.21"
#define UDP_PORT 6666

#define INPUT_PIN 14  //D5 -> ppk2 D2
//#define INPUT_PIN 0 //Flash Button

#define PIN_SHOW_WIFI_SETUP 4 //D2 -> ppk2 D0
#define PIN_SHOW_RECEIVED 5   //D1 -> ppk2 D1

WiFiUDP Udp;

char  ReplyBuffer[] = "Hi";       // a string to send back

unsigned long last_interrupt_time = 0;

void ICACHE_RAM_ATTR sendUDP(){
  unsigned long interrupt_time = millis();
  if (interrupt_time - last_interrupt_time > 500UL)  // ignores interupts for 500milliseconds
  {
    last_interrupt_time = interrupt_time;
    if (digitalRead(INPUT_PIN)){  // reading again after read short delay ocuring becaus of the timing check prohibits small bouncers on falling flanks comming throu.
      digitalWrite(PIN_SHOW_RECEIVED, HIGH);
      Udp.beginPacket(RECIVER_IP, UDP_PORT);
      Udp.write(ReplyBuffer);
      Udp.endPacket();
      digitalWrite(PIN_SHOW_RECEIVED, LOW);
      Serial.println("sended");
    }
  }
  else
  {
    last_interrupt_time = interrupt_time;
  }
  
}

void setup() {
  pinMode(INPUT_PIN, INPUT);
  pinMode(PIN_SHOW_WIFI_SETUP, OUTPUT);
  pinMode(PIN_SHOW_RECEIVED, OUTPUT);
  digitalWrite(PIN_SHOW_WIFI_SETUP, LOW);
  digitalWrite(PIN_SHOW_RECEIVED, LOW);

  // Setup serial port
  Serial.begin(115200);
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


  attachInterrupt(digitalPinToInterrupt(INPUT_PIN), sendUDP, RISING);
   
}
   
void loop() {
  delay(1000);                       
}
