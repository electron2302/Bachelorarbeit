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
|<ul><li>- [ ] a</li></ul>|Stromverbrauch - idel <br> Stromverbrauch - senden <br> Reliability <br> Latency|esp8266|PI| |
|<ul><li>- [ ] b</li></ul>|Stromverbrauch - idel <br> Stromverbrauch - senden <br> Reliability <br> Latency|nrf52840 - Thread|PI| |
|<ul><li>- [ ] c</li></ul>|Stromverbrauch - idel <br> Stromverbrauch - senden <br> Reliability <br> Latency|nrf52840 - BLE|PI| |
|<ul><li>- [ ] d</li></ul>|Stromverbrauch - deepsleep <br> Stromverbrauch - wakup <br> Dauer-wakeup <br> Stromverbrauch - senden <br> Reliability <br> Latency|esp8266|PI| |
|<ul><li>- [ ] e</li></ul>|Stromverbrauch - deepsleep <br> Stromverbrauch - wakup <br> Dauer-wakeup <br> Stromverbrauch - senden <br> Reliability <br> Latency|nrf52840 - Thread|PI| |
|<ul><li>- [ ] f</li></ul>|Stromverbrauch - deepsleep <br> Stromverbrauch - wakup <br> Dauer-wakeup <br> Stromverbrauch - senden <br> Reliability <br> Latency|nrf52840 - BLE|PI| |
|<ul><li>- [ ] g</li></ul>|Dauer-wakeup <br> Stromverbrauch - wakup <br> Stromverbrauch - senden <br> Reliability <br> Latency|esp8266|PI| |
|<ul><li>- [ ] h</li></ul>|Dauer-wakeup <br> Stromverbrauch - wakup <br> Stromverbrauch - senden <br> Reliability <br> Latency|nrf52840 - Thread|PI| |
|<ul><li>- [ ] i</li></ul>|Dauer-wakeup <br> Stromverbrauch - wakup <br> Stromverbrauch - senden <br> Reliability <br> Latency|nrf52840 - BLE|PI| |
|<ul><li>- [ ] j</li></ul>|Stromverbrauch - idel <br> Stromverbrauch - empfang <br> Reliability <br> Latency|PI|esp8266| |
|<ul><li>- [ ] k</li></ul>|Stromverbrauch - idel <br> Stromverbrauch - empfang <br> Reliability <br> Latency|PI|nrf52840 - Thread| |
|<ul><li>- [ ] l</li></ul>|Stromverbrauch - idel <br> Stromverbrauch - empfang <br> Reliability <br> Latency|PI|nrf52840 - BLE| |
|<ul><li>- [ ] m</li></ul>|Stromverbrauch - deepsleep <br> Dauer-wakeup <br> Stromverbrauch - wakup <br> Stromverbrauch - empfang <br> Reliability <br> Latency|PI|nrf52840 - Thread| |
|<ul><li>- [ ] n</li></ul>|Stromverbrauch - deepsleep <br> Dauer-wakeup <br> Stromverbrauch - wakup <br> Stromverbrauch - empfang <br> Reliability <br> Latency|PI|nrf52840 - BLE| |

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
