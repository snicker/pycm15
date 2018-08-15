from yapsy.IPlugin import IPlugin
from pprint import pprint
from datetime import datetime


def nibble(byte):
    high, low = byte >> 4, byte & 0x0F
    return high, low


def nibble_high(byte):
    return nibble(byte)[0]


def nibble_low(byte):
    return nibble(byte)[1]


class BaseX10Message(object):
    def __init__(self, data):
        self.data = data
        self.received = datetime.now()
        
    def __repr__(self):
        return "{}: {}".format(self.__class__.__name__, self.data)
        
class PowerFailureMessage(BaseX10Message):
    pass
        
class X10MessageParser(object):
    """http://www.linuxha.com/USB/cm15a.html"""
    """http://www.linuxha.com/athome/common/cm15d/cm15d.html"""
    MessageTypes = {
        0xA5: PowerFailureMessage
    }
    def parse(self, data):
        if len(data) > 0:
            return X10MessageParser.MessageTypes.get(data[0],BaseX10Message)(data)
        return None

class Decoded_Echo(IPlugin):
    Parser = X10MessageParser()
    def cm15DataReceivedHandler(self, data):
        message = Decoded_Echo.Parser.parse(data)
        print("Data received: ")
        pprint(Message)
    def cm15DataWrittenHandler(self, data):
        print("Data written: ")
        pprint(data)
