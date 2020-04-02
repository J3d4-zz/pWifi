#!/usr/bin/env python

import os, configparser, subprocess

class Config:
    def __init__(self):
        self._runDir = os.path.dirname(__file__)
        self._config = configparser.ConfigParser() 
        self._confPath = self._config.read(self._runDir + '/config.ini')
        self._pWifiConf = self._config['pWifi']
        
        self.fields = self._pWifiConf['fields']
        self.position = int(self._pWifiConf['position'])
        self._yoff = int(self._pWifiConf['yoff'])
        self._xoff = int(self._pWifiConf['xoff'])
        self.font = self._pWifiConf['font']
    
    @property
    def fields (self):
        return self._fields
    @fields.setter
    def fields (self, value):
        if not type(value) is str and ", " not in value:
             raise TypeError("You can only place stings separated with a ', ' as fields.")
        self._fields = value

    @property
    def position(self):
        return self._position
    @position.setter
    def position(self, value):
        if value < 0 and value > 8:
            raise ValueError("The value must be between 0 and 8.")
        self._position = value

    @property
    def yoff(self):
        return self._yoff

    @property
    def xoff(self):
        return self._xoff
    
    @property
    def font(self):
        return self._font
    @font.setter
    def font(self, value):
        if not type(value) is str:
            raise TypeError("Must be a valid font type and a valid font size")
        self._font = value

if __name__ == "__main__":
    conf = Config()
    def conList(fields):
        conlist = subprocess.run(["nmcli", "--fields", fields, "device", "wifi", "list"], stdout=subprocess.PIPE)
        value = [conlist.stdout]
        return value
    def conWidth(conList):
        return subprocess.run(["echo", conList])
    def conLength(conList):
        return conList
    def knownConnections():
        return subprocess.run(["nmcli", "connection", "show"])
    def isConnected():
        conInfo = subprocess.run(["nmcli", "-fields", "WIFI", "g"], stdout=subprocess.PIPE)
        conOut = [conInfo.stdout]
        print(conOut)
        if 'enabled' in conOut:
            return True
    
    print(isConnected())
    print(conList(conf.fields))