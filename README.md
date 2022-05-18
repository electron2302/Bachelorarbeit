# Bachelorarbeit

| |wifi|thread|BLE|
|:----|:----|:----|:----|
|senden (ON)|a|b|c|
|senden (deepsleep)|d|e|f|
|senden (OFF)|g|h|i|
|empfangen (ON)|j|k|l|
|empfangen (deepsleep)|nein|m|n|

|Scenario|Messgrößen|Sender|Empfänger|Fertig|
|:----|:----|:----|:----|:----|
|a|Stromverbrauch - idel <br> Stromverbrauch - senden <br> Reliability <br> Latency|esp8266|PI| |
|b|Stromverbrauch - idel <br> Stromverbrauch - senden <br> Reliability <br> Latency|nrf52840 - Thread|PI| |
|c|Stromverbrauch - idel <br> Stromverbrauch - senden <br> Reliability <br> Latency|nrf52840 - BLE|PI| |
|d|Stromverbrauch - deepsleep <br> Stromverbrauch - wakup <br> Dauer-wakeup <br> Stromverbrauch - senden <br> Reliability <br> Latency|esp8266|PI| |
|e|Stromverbrauch - deepsleep <br> Stromverbrauch - wakup <br> Dauer-wakeup <br> Stromverbrauch - senden <br> Reliability <br> Latency|nrf52840 - Thread|PI| |
|f|Stromverbrauch - deepsleep <br> Stromverbrauch - wakup <br> Dauer-wakeup <br> Stromverbrauch - senden <br> Reliability <br> Latency|nrf52840 - BLE|PI| |
|g|Dauer-wakeup <br> Stromverbrauch - wakup <br> Stromverbrauch - senden <br> Reliability <br> Latency|esp8266|PI| |
|h|Dauer-wakeup <br> Stromverbrauch - wakup <br> Stromverbrauch - senden <br> Reliability <br> Latency|nrf52840 - Thread|PI| |
|i|Dauer-wakeup <br> Stromverbrauch - wakup <br> Stromverbrauch - senden <br> Reliability <br> Latency|nrf52840 - BLE|PI| |
|j|Stromverbrauch - idel <br> Stromverbrauch - empfang <br> Reliability <br> Latency|PI|esp8266| |
|k|Stromverbrauch - idel <br> Stromverbrauch - empfang <br> Reliability <br> Latency|PI|nrf52840 - Thread| |
|l|Stromverbrauch - idel <br> Stromverbrauch - empfang <br> Reliability <br> Latency|PI|nrf52840 - BLE| |
|m|Stromverbrauch - deepsleep <br> Dauer-wakeup <br> Stromverbrauch - wakup <br> Stromverbrauch - empfang <br> Reliability <br> Latency|PI|nrf52840 - Thread| |
|n|Stromverbrauch - deepsleep <br> Dauer-wakeup <br> Stromverbrauch - wakup <br> Stromverbrauch - empfang <br> Reliability <br> Latency|PI|nrf52840 - BLE| |

Scripte die ich brauche:
 - [ ] PI udp send
 - [ ] PI udp receive
 - [ ] PI BLE send
 - [ ] PI BLE receive
 - [ ] PI Thread send / (border router ?)
 - [ ] PI Thread receive
 - [ ] esp send udp awake
 - [ ] esp send udp deepsleep
 - [ ] esp send udp shutdown
 - [ ] esp receive udp awake
 - [ ] nrf BLE Switch Node awake
 - [ ] nrf BLE Switch Node deepsleep
 - [ ] nrf BLE Switch Node shutdown ? 
 - [ ] nrf BLE Light Node awake
 - [ ] nrf BLE Light Node deepsleep
 - [ ] nrf BLE Friend Role on a chip
 - [ ] nrf Thread “schwitch / sender” awake / MED
 - [ ] nrf Thread “schwitch / sender” deepsleep / SED
 - [ ] nrf Thread “schwitch / sender” shutdown/ SED ?
 - [ ] nrf Thread “Light / receiver” awake / MED
 - [ ] nrf Thread “Light / receiver” deepsleep / SED ? or ssed ? 
 - [ ] nrf Thread just FTD Role on a chip
