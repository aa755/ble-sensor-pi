#!/usr/bin/env python
# Michael Saunby. April 2013
#
# Notes.
# pexpect uses regular expression so characters that have special meaning
# in regular expressions, e.g. [ and ] must be escaped with a backslash.
#
#   Copyright 2013 Michael Saunby
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.

# CC2650 SensorTag attribute table
# 
# http://e2e.ti.com/cfs-file/__key/communityserver-discussions-components-files/538/attr_5F00_cc2650-sensortag.html
# TI Base UUID: F000XXXX-0451-4000-B000-000000000000. 128 bit UUIDs are typed 'bold blue'
# 
# Handle
# (hex)    Handle
# (dec)    Type
# (hex)    Type (text)    Hex value    GATT Server
# Permissions    Description/Value (text)
# 0x1    1    0x2800    GATT Primary Service Declaration    0x1800    R    Generic Access Service
# 0x2    2    0x2803    GATT Characteristic Declaration    02:03:00:00:2A    R    Device Name
# 0x3    3    0x2A00    Device Name    53:65:6E:73:6F:72:54:61:67:20:32:2E:30    R    SensorTag 2.0
# 0x4    4    0x2803    GATT Characteristic Declaration    02:05:00:01:2A    R    Appearance
# 0x5    5    0x2A01    Appearance    00:00    R    
# 0x6    6    0x2803    GATT Characteristic Declaration    02:07:00:04:2A    R    Peripheral Preferred Connection Parameters
# 0x7    7    0x2A04    Peripheral Preferred Connection Parameters    50:00:A0:00:00:00:E8:03    R    P
# 0x8    8    0x2800    GATT Primary Service Declaration    0x1801    R    Generic Attribute Service
# 0x9    9    0x2803    GATT Characteristic Declaration    20:0A:00:05:2A    R    Service Changed
# 0xA    10    0x2A05    Service Changed        I    
# 0xB    11    0x2902    Client Characteristic Configuration    00:00    RW    Write "01:00" to enable notifications, "00:00" to disable
# 0xC    12    0x2800    GATT Primary Service Declaration    0x180A    R    Device Information Service
# 0xD    13    0x2803    GATT Characteristic Declaration    02:0E:00:23:2A    R    System ID
# 0xE    14    0x2A23    System ID    85:A9:71:00:00:84:BE:C4    R    q
# 0xF    15    0x2803    GATT Characteristic Declaration    02:10:00:24:2A    R    Model Number String
# 0x10    16    0x2A24    Model Number String    43:43:32:36:35:30:20:53:65:6E:73:6F:72:54:61:67:00    R    CC2650 SensorTag
# 0x11    17    0x2803    GATT Characteristic Declaration    02:12:00:25:2A    R    Serial Number String
# 0x12    18    0x2A25    Serial Number String    4E:2E:41:2E:00    R    N.A.
# 0x13    19    0x2803    GATT Characteristic Declaration    02:14:00:26:2A    R    Firmware Revision String
# 0x14    20    0x2A26    Firmware Revision String    31:2E:30:31:20:28:4D:61:72:20:31:33:20:32:30:31:35:29:00    R    1.01 (Mar 13 2015)
# 0x15    21    0x2803    GATT Characteristic Declaration    02:16:00:27:2A    R    Hardware Revision String
# 0x16    22    0x2A27    Hardware Revision String    50:43:42:20:31:2E:32:00    R    PCB 1.2
# 0x17    23    0x2803    GATT Characteristic Declaration    02:18:00:28:2A    R    Software Revision String
# 0x18    24    0x2A28    Software Revision String    4E:2E:41:2E:00    R    N.A.
# 0x19    25    0x2803    GATT Characteristic Declaration    02:1A:00:29:2A    R    Manufacturer Name String
# 0x1A    26    0x2A29    Manufacturer Name String    54:65:78:61:73:20:49:6E:73:74:72:75:6D:65:6E:74:73:00    R    Texas Instruments
# 0x1B    27    0x2803    GATT Characteristic Declaration    02:1C:00:2A:2A    R    IEEE 11073-20601 Regulatory Certification Data List
# 0x1C    28    0x2A2A    IEEE 11073-20601 Regulatory Certification Data List    FE:00:65:78:70:65:72:69:6D:65:6E:74:61:6C    R    experimental
# 0x1D    29    0x2803    GATT Characteristic Declaration    02:1E:00:50:2A    R    PnP ID
# 0x1E    30    0x2A50    PnP ID    01:0D:00:00:00:10:01    R    
# 0x1F    31    0x2800    GATT Primary Service Declaration    F000AA00-0451-4000-B000-000000000000    R    IR Temperature Service
# 0x20    32    0x2803    GATT Characteristic Declaration    12:21:00:00:00:00:00:00:00:00:B0:00:40:51:04:01:AA:00:F0    R    IR Temperature Data
# 0x21    33    0xAA01    IR Temperature Data    00:00:00:00    RN    ObjectLSB:ObjectMSB:AmbientLSB:AmbientMSB
# 0x22    34    0x2902    Client Characteristic Configuration    01:00    RW    Write "01:00" to enable notifications, "00:00" to disable
# 0x23    35    0x2803    GATT Characteristic Declaration    0A:24:00:00:00:00:00:00:00:00:B0:00:40:51:04:02:AA:00:F0    R    IR Temperature Config
# 0x24    36    0xAA02    IR Temperature Config    00    RW    Write "01" to start Sensor and Measurements, "00" to put to sleep
# 0x25    37    0x2803    GATT Characteristic Declaration    0A:26:00:00:00:00:00:00:00:00:B0:00:40:51:04:03:AA:00:F0    R    IR Temperature Period
# 0x26    38    0xAA03    IR Temperature Period    64    RW    Period = [Input*10] ms, (lower limit 300 ms), default 1000 ms
# 0x27    39    0x2800    GATT Primary Service Declaration    F000AA20-0451-4000-B000-000000000000    R    Humidity Service
# 0x28    40    0x2803    GATT Characteristic Declaration    12:29:00:00:00:00:00:00:00:00:B0:00:40:51:04:21:AA:00:F0    R    Humidity Data
# 0x29    41    0xAA21    Humidity Data    00:00:00:00    RN    TempLSB:TempMSB:HumidityLSB:HumidityMSB
# 0x2A    42    0x2902    Client Characteristic Configuration    01:00    RW    Write "01:00" to enable notifications, "00:00" to disable
# 0x2B    43    0x2803    GATT Characteristic Declaration    0A:2C:00:00:00:00:00:00:00:00:B0:00:40:51:04:22:AA:00:F0    R    Humidity Config
# 0x2C    44    0xAA22    Humidity Config    00    RW    Write "01" to start measurements, "00" to stop
# 0x2D    45    0x2803    GATT Characteristic Declaration    0A:2E:00:00:00:00:00:00:00:00:B0:00:40:51:04:23:AA:00:F0    R    Humidity Period
# 0x2E    46    0xAA23    Humidity Period    64    RW    Period = [Input*10] ms, (lower limit 100 ms), default 1000 ms
# 0x2F    47    0x2800    GATT Primary Service Declaration    F000AA40-0451-4000-B000-000000000000    R    Barometer Service
# 0x30    48    0x2803    GATT Characteristic Declaration    12:31:00:00:00:00:00:00:00:00:B0:00:40:51:04:41:AA:00:F0    R    Barometer Data
# 0x31    49    0xAA41    Barometer Data    00:00:00:00:00:00    RN    TempLSB:TempMSB(:TempEXt):PressureLSB:PressureMSB(:PressureExt). If the length is 6 bytes the extension byte is included.
# 0x32    50    0x2902    Client Characteristic Configuration    01:00    RW    Write "01:00" to enable notifications, "00:00" to disable
# 0x33    51    0x2803    GATT Characteristic Declaration    0A:34:00:00:00:00:00:00:00:00:B0:00:40:51:04:42:AA:00:F0    R    Barometer Configuration
# 0x34    52    0xAA42    Barometer Configuration    00    RW    Write "01" to start Sensor and Measurements, "00" to put to sleep, "02" to read calibration values from sensor
# 0x35    53    0x2803    GATT Characteristic Declaration    0A:36:00:00:00:00:00:00:00:00:B0:00:40:51:04:44:AA:00:F0    R    Barometer Period
# 0x36    54    0xAA44    Barometer Period    64    RW    Period = [Input*10] ms, (lower limit 100 ms), default 1000 ms
# 0x37    55    0x2800    GATT Primary Service Declaration    F000AA80-0451-4000-B000-000000000000    R    Movement Service
# 0x38    56    0x2803    GATT Characteristic Declaration    12:39:00:00:00:00:00:00:00:00:B0:00:40:51:04:81:AA:00:F0    R    Movement Data
# 0x39    57    0xAA81    Movement Data    00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00    RN    GXLSB:GXMSB:GYLSB:GYMSB:GZLSB:GZMSB, AXLSB:AXMSB:AYLSB:AYMSB:AZLSB:AZMSB
# 0x3A    58    0x2902    Client Characteristic Configuration    01:00    RW    Write "01:00" to enable notifications, "00:00" to disable
# 0x3B    59    0x2803    GATT Characteristic Declaration    0A:3C:00:00:00:00:00:00:00:00:B0:00:40:51:04:82:AA:00:F0    R    Movement Config
# 0x3C    60    0xAA82    Movement Config    00:02    RW    Axis enable bits:gyro-z=0,gyro-y,gyro-x,acc-z=3,acc-y,acc-x,mag=6 Range: bit 8,9
# 0x3D    61    0x2803    GATT Characteristic Declaration    0A:3E:00:00:00:00:00:00:00:00:B0:00:40:51:04:83:AA:00:F0    R    Movement Period
# 0x3E    62    0xAA83    Movement Period    64    RW    Period = [Input*10]ms (lower limit 100ms), default 1000ms
# 0x3F    63    0x2800    GATT Primary Service Declaration    F000AA70-0451-4000-B000-000000000000    R    Luxometer Service
# 0x40    64    0x2803    GATT Characteristic Declaration    12:41:00:00:00:00:00:00:00:00:B0:00:40:51:04:71:AA:00:F0    R    Luxometer Data
# 0x41    65    0xAA71    Luxometer Data    00:00    RN    LSB:MSB
# 0x42    66    0x2902    Client Characteristic Configuration    01:00    RW    Write "01:00" to enable notifications, "00:00" to disable
# 0x43    67    0x2803    GATT Characteristic Declaration    0A:44:00:00:00:00:00:00:00:00:B0:00:40:51:04:72:AA:00:F0    R    Luxometer Config
# 0x44    68    0xAA72    Luxometer Config    00    RW    Write "01" to start Sensor and Measurements, "00" to put to sleep
# 0x45    69    0x2803    GATT Characteristic Declaration    0A:46:00:00:00:00:00:00:00:00:B0:00:40:51:04:73:AA:00:F0    R    Luxometer Period
# 0x46    70    0xAA73    Luxometer Period    50    RW    Period = [Input*10]ms (lower limit 1000ms), default 2000ms
# 0x47    71    0x2800    GATT Primary Service Declaration    0xFFE0    R    Simple Keys Service
# 0x48    72    0x2803    GATT Characteristic Declaration    10:49:00:E1:FF    R    Key press state
# 0x49    73    0xFFE1    Key press state        N    
# 0x4A    74    0x2902    Client Characteristic Configuration    01:00    RW    Write "01:00" to enable notifications, "00:00" to disable
# 0x4B    75    0x2901    Characteristic User Description    4B:65:79:20:50:72:65:73:73:20:53:74:61:74:65    R    Key Press State
# 0x4C    76    0x2800    GATT Primary Service Declaration    F000AA64-0451-4000-B000-000000000000    R    IO Service
# 0x4D    77    0x2803    GATT Characteristic Declaration    0A:4E:00:00:00:00:00:00:00:00:B0:00:40:51:04:65:AA:00:F0    R    IO Data
# 0x4E    78    0xAA65    IO Data    7F    RW    Local and remote mode: bit 0 - red led; bit 1 - green led; bit 2 - buzzer. In test mode: sensor self test result (exp. 0x5F)
# 0x4F    79    0x2803    GATT Characteristic Declaration    0A:50:00:00:00:00:00:00:00:00:B0:00:40:51:04:66:AA:00:F0    R    IO Config
# 0x50    80    0xAA66    IO Config    00    RW    0:local mode; 1:remote mode; 2:test mode
# 0x51    81    0x2800    GATT Primary Service Declaration    F000AC00-0451-4000-B000-000000000000    R    Register Service
# 0x52    82    0x2803    GATT Characteristic Declaration    1A:53:00:00:00:00:00:00:00:00:B0:00:40:51:04:01:AC:00:F0    R    Register Data
# 0x53    83    0xAC01    Register Data    00:00    RWN    Data from serial device, variable length (see Register Address)
# 0x54    84    0x2902    Client Characteristic Configuration    00:00    RW    Write "01:00" to enable notifications, "00:00" to disable
# 0x55    85    0x2803    GATT Characteristic Declaration    0A:56:00:00:00:00:00:00:00:00:B0:00:40:51:04:02:AC:00:F0    R    Register Address
# 0x56    86    0xAC02    Register Address    02:02:00:00:00    RW    length(byte, max 16);internal addr (1 to 4 bytes)
# 0x57    87    0x2803    GATT Characteristic Declaration    0A:58:00:00:00:00:00:00:00:00:B0:00:40:51:04:03:AC:00:F0    R    Register Device ID
# 0x58    88    0xAC03    Register Device ID    00:44    RW    byte 1 (interface): 0=I2C0,1=I2C1,2=SPI1,3=SPI2,4=SPI3,5=MCU; byte 2: device addr
# 0x59    89    0x2800    GATT Primary Service Declaration    F000CCC0-0451-4000-B000-000000000000    R    Connection Control Service
# 0x5A    90    0x2803    GATT Characteristic Declaration    12:5B:00:00:00:00:00:00:00:00:B0:00:40:51:04:C1:CC:00:F0    R    Connection Parameters
# 0x5B    91    0xCCC1    Connection Parameters    06:00:00:00:64:00    RN    ConnInterval,SlaveLatency,SupervisionTimeout (2 bytes each)
# 0x5C    92    0x2902    Client Characteristic Configuration    00:00    RW    Write "01:00" to enable notifications, "00:00" to disable
# 0x5D    93    0x2803    GATT Characteristic Declaration    08:5E:00:00:00:00:00:00:00:00:B0:00:40:51:04:C2:CC:00:F0    R    Request Connection Parameters
# 0x5E    94    0xCCC2    Request Connection Parameters        W    MinConnInterval,MaxConnInterval,SlaveLatency,SupervisionTimeout (2 bytes each)
# 0x5F    95    0x2803    GATT Characteristic Declaration    08:60:00:00:00:00:00:00:00:00:B0:00:40:51:04:C3:CC:00:F0    R    Disconnect request
# 0x60    96    0xCCC3    Disconnect request        W    Change the value to disconnect
# 0x61    97    0x2800    GATT Primary Service Declaration    F000FFC0-0451-4000-B000-000000000000    R    OAD Service
# 0x62    98    0x2803    GATT Characteristic Declaration    1C:63:00:00:00:00:00:00:00:00:B0:00:40:51:04:C1:FF:00:F0    R    OAD Image Identify
# 0x63    99    0xFFC1    OAD Image Identify        WN    Write '0' to identify image type 'A', '1' to identify 'B'. Data in notfication 8 bytes: image type (2), size/4 (2), user data (4).
# 0x64    100    0x2902    Client Characteristic Configuration    01:00    RW    Write "01:00" to enable notifications, "00:00" to disable
# 0x65    101    0x2901    Characteristic User Description    49:6D:67:20:49:64:65:6E:74:69:66:79    R    Img Identify
# 0x66    102    0x2803    GATT Characteristic Declaration    1C:67:00:00:00:00:00:00:00:00:B0:00:40:51:04:C2:FF:00:F0    R    OAD Image Block
# 0x67    103    0xFFC2    OAD Image Block        WN    Image block (18 bytes). Block no. (2 bytes), OAD image block (16 bytes)
# 0x68    104    0x2902    Client Characteristic Configuration    01:00    RW    Write "01:00" to enable notifications, "00:00" to disable
# 0x69    105    0x2901    Characteristic User Description    49:6D:67:20:42:6C:6F:63:6B    R    Img Block

import pexpect
import sys
import time
from sensor_calcs import *
import json
import select
import traceback
import homeassistant.remote as remote

def floatfromhex(h):
    #print(h)
    t = float.fromhex(h)
    if t > float.fromhex('7FFF'):
        t = -(float.fromhex('FFFF') - t)
        pass
    return t

class SensorTag:

    def __init__(self, bluetooth_adr):
        self.con = pexpect.spawn('gatttool -b ' + bluetooth_adr + ' --interactive')
        self.con.expect('\[LE\]>')
        #print self.con.before
        #print self.con.after
        print ("Preparing to connect. You might need to press the side button...")
        result = self.con.sendline('connect')
        print (result)
        # test for success of connect
        result = self.con.expect('Connection successful.*\[LE\]>')
        print (result)
        #print self.con.before
        #print self.con.after
        # Earlier versions of gatttool returned a different message.  Use this pattern -
        # self.con.expect('\[CON\].*>')
        self.cb = {}
        return

        self.con.expect('\[CON\].*>')
        self.cb = {}
        return

    def char_write_cmd(self, handle, value):
        # The 0%x for value is VERY naughty!  Fix this!
        cmd = 'char-write-cmd 0x%02x 0%x' % (handle, value)
        print (cmd)
        self.con.sendline(cmd)
        return

    def char_read_hnd(self, handle):
        self.con.sendline('char-read-hnd 0x%02x' % handle)
        self.con.expect('descriptor: .*? \r')
        after = self.con.after
        rval = after.split()[1:]
        #return [int(n) for n in rval]
        #print ([n[1:] for n in rval])
        return [int(float.fromhex(n.decode("utf-8") )) for n in rval]

    # misnamed : no notifications. just polling.
    def notification_loop(self):
        api = remote.API('brixpro.lan', 'enter-home-assistant-password-here')
        while True:
            try:
                v = self.char_read_hnd(0x21)
	            # objT = (v[1]<<8)+v[0]
                ambT = (v[3] << 8) + v[2]
                ambT = tosigned(ambT)
                c_tmpAmb = ambT / 128.0
                f_tmpAmb = 9.0 / 5.0 * c_tmpAmb + 32
                remote.set_state(api, 'sensor.bedroom_temp', new_state=f_tmpAmb)
                # targetT = calcTmpTarget(objT, ambT)
              # self.data['t006'] = targetT
              # print "T006 %.1f" % c_tmpAmb            
                v = self.char_read_hnd(0x29)
                rawT = (v[1] << 8) + v[0]
                rawH = (v[3] << 8) + v[2]
                (t, rh) = calcHum(rawT, rawH)
                remote.set_state(api, 'sensor.bedroom_humidity', new_state=rh)
                #print ("%s -- %.1f %.1f" % (time.strftime('%l:%M:%S%p %Z on %b %d, %Y'), f_tmpAmb, rh))
                time.sleep(5) # save battery on sensortag? 
            except pexpect.TIMEOUT:
                print ("TIMEOUT exception!")
                break

    def register_cb(self, handle, fn):
        self.cb[handle] = fn;
        return

barometer = None
datalog = sys.stdout

def main():
    global datalog
    global barometer    
    if len(sys.argv) > 2:
        bluetooth_adr = sys.argv[1]
    else:
        bluetooth_adr = "A0:E6:F8:AE:3B:86"
    # data['addr'] = bluetooth_adr
    
    if len(sys.argv) > 2:
        datalog = open(sys.argv[2], 'w+')

    while True:
     try:   
      print ("[re]starting..")

      tag = SensorTag(bluetooth_adr)

      # enable TMP006 sensor
      # tag.register_cb(0x25,cbs.tmp006)
      tag.char_write_cmd(0x24, 0x01)
      # enable humidity sensor
      tag.char_write_cmd(0x2C, 0x01)
      
      time.sleep(5)  # give the sensor some time. otherwise initial values are garbage
      # tag.char_write_cmd(0x26,0x0100)
      tag.notification_loop()
     except:
      traceback.print_exc(file=sys.stdout)
      # sys.exit()
      # pass

if __name__ == "__main__":
    main()

