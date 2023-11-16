import pytest
from television import *

class Test:
    """
    Class to test the Television class.
    """
    
    def setup_method(self) -> None:
        """
        Method to setup the test fixture for the Television class.
        """
        self.tv = Television()
    
    def test__init__(self) -> None:
        """
        Method to test the __init__ method of the Television class.
        """
        assert self.tv.__str__() == "Power = False, Channel = 0, Volume = 0" # Default values when initialized
        
    def test_power(self) -> None:
        """
        Method to test the power method of the Television class.
        """
        self.tv.power()
        assert self.tv.__str__() == "Power = True, Channel = 0, Volume = 0" # Powered on
        self.tv.power()
        assert self.tv.__str__() == "Power = False, Channel = 0, Volume = 0" # Powered off

    def test_mute(self) -> None:
        """
        Method to test the mute method of the Television class.
        """
        self.tv.power()
        self.tv.volume_up()
        self.tv.mute()
        assert self.tv.__str__() == "Power = True, Channel = 0, Volume = 0" # Powered on volume turned up then muted
        self.tv.mute()
        assert self.tv.__str__() == "Power = True, Channel = 0, Volume = 1" # Powered on volume turned up then unmuted
        self.tv.power()
        assert self.tv.__str__() == "Power = False, Channel = 0, Volume = 1" # Powered off with volume already turned up then tries to mute with it off.
        self.tv.power()
        self.tv.mute()
        self.tv.power()
        assert self.tv.__str__() == "Power = False, Channel = 0, Volume = 0" # Turned back on muted then turned off with volume already turned up.
        
    def test_channel_up(self) -> None:
        """
        Method to test the channel_up method of the Television class.
        """
        self.tv.channel_up()
        assert self.tv.__str__() == "Power = False, Channel = 0, Volume = 0" # Attempt to channel up with tv off
        self.tv.power()
        self.tv.channel_up()
        assert self.tv.__str__() == "Power = True, Channel = 1, Volume = 0" # Channel up with tv on
        self.tv.channel_up()
        self.tv.channel_up()
        self.tv.channel_up()
        assert self.tv.__str__() == "Power = True, Channel = 0, Volume = 0" # Channel up with tv on and at max channel
        
    def test_channel_down(self) -> None:
        """
        Method to test the channel_down method of the Television class.
        """
        self.tv.channel_down()
        assert self.tv.__str__() == "Power = False, Channel = 0, Volume = 0" # Attempt to channel down with tv off
        self.tv.power()
        self.tv.channel_down()
        assert self.tv.__str__() == "Power = True, Channel = 3, Volume = 0" # Channel down with tv on and at minimum channel
        
    def test_volume_up(self) -> None:
        """
        Method to test the volume_up method of the Television class.
        """
        self.tv.volume_up()
        assert self.tv.__str__() == "Power = False, Channel = 0, Volume = 0" # Attempt to volume up with tv off
        self.tv.power()
        self.tv.volume_up()
        assert self.tv.__str__() == "Power = True, Channel = 0, Volume = 1" # Volume up with tv on
        self.tv.mute()
        self.tv.volume_up()
        assert self.tv.__str__() == "Power = True, Channel = 0, Volume = 2" # Volume up with tv on and muted
        self.tv.volume_up()
        assert self.tv.__str__() == "Power = True, Channel = 0, Volume = 2" # Volume up with tv on and at max volume
        
    def test_volume_down(self) -> None:
        """
        Method to test the volume_down method of the Television class.
        """
        self.tv.volume_down()
        assert self.tv.__str__() == "Power = False, Channel = 0, Volume = 0" # Attempt to volume down with tv off
        self.tv.power()
        self.tv.volume_up()
        self.tv.volume_up()
        self.tv.volume_down()
        assert self.tv.__str__() == "Power = True, Channel = 0, Volume = 1" # Volume down with tv on
        self.tv.volume_down()
        self.tv.mute()
        assert self.tv.__str__() == "Power = True, Channel = 0, Volume = 0" # Volume down with tv on and muted
        self.tv.volume_down()
        assert self.tv.__str__() == "Power = True, Channel = 0, Volume = 0" # Volume down with tv on and at min volume