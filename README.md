# HomematicIP Processor

Push Homematic IP sensor values to various targets:
- command line
- Adafruit IO

TBD:
- CSV

## Supported Homematic IP devices
- Weathersensor Plus

## Prerequisites
Requires the homematicip Python package:
- Installation via: ```pip3 install homematicip```
- Afterwards follow configuration instructions described here: https://github.com/coreGreenberet/homematicip-rest-api

Requires the Adafruit IO Python package:
- Installation via: ```pip3 install adafruit-io```
- Set environment variables 
    - ADAFRUIT_IO_USERNAME
    - ADAFRUIT_IO_KEY
- create according feeds (adapt code or use those)
