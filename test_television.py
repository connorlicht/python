import pytest
from television import *

class Test:
    """
    Class to test the Television class.
    """
    
    def test__init__(self) -> None:
        """
        Method to test the __init__ method of the Television class.
        """
        tv = Television()
        assert tv.__str__() == "Power = False, Channel = 0, Volume = 0" # Default values when initialized
        
    def test_power(self) -> None:
        """
        Method to test the power method of the Television class.
        """
        tv = Television()
        tv.power()
        assert tv.__str__() == "Power = True, Channel = 0, Volume = 0" # Powered on
        tv.power()
        assert tv.__str__() == "Power = False, Channel = 0, Volume = 0" # Powered off

    def test_mute(self) -> None:
        """
        Method to test the mute method of the Television class.
        """
        tv = Television()
        tv.power()
        tv.volume_up()
        tv.mute()
        assert tv.__str__() == "Power = True, Channel = 0, Volume = 0" # Powered on volume turned up then muted
        tv.mute()
        assert tv.__str__() == "Power = True, Channel = 0, Volume = 1" # Powered on volume turned up then unmuted
        tv.power()
        assert tv.__str__() == "Power = False, Channel = 0, Volume = 1" # Powered off with volume already turned up then tries to mute with it off.
        tv.power()
        tv.mute()
        tv.power()
        assert tv.__str__() == "Power = False, Channel = 0, Volume = 0" # Turned back on muted then turned off with volume already turned up.
        
    def test_channel_up(self) -> None:
        """
        Method to test the channel_up method of the Television class.
        """
        tv = Television()
        tv.channel_up()
        assert tv.__str__() == "Power = False, Channel = 0, Volume = 0" # Attempt to channel up with tv off
        tv.power()
        tv.channel_up()
        assert tv.__str__() == "Power = True, Channel = 1, Volume = 0" # Channel up with tv on
        tv.channel_up()
        tv.channel_up()
        tv.channel_up()
        assert tv.__str__() == "Power = True, Channel = 0, Volume = 0" # Channel up with tv on and at max channel
        
    def test_channel_down(self) -> None:
        """
        Method to test the channel_down method of the Television class.
        """
        tv = Television()
        tv.channel_down()
        assert tv.__str__() == "Power = False, Channel = 0, Volume = 0" # Attempt to channel down with tv off
        tv.power()
        tv.channel_down()
        assert tv.__str__() == "Power = True, Channel = 3, Volume = 0" # Channel down with tv on and at minimum channel
        
    def test_volume_up(self) -> None:
        """
        Method to test the volume_up method of the Television class.
        """
        tv = Television()
        tv.volume_up()
        assert tv.__str__() == "Power = False, Channel = 0, Volume = 0" # Attempt to volume up with tv off
        tv.power()
        tv.volume_up()
        assert tv.__str__() == "Power = True, Channel = 0, Volume = 1" # Volume up with tv on
        tv.mute()
        tv.volume_up()
        assert tv.__str__() == "Power = True, Channel = 0, Volume = 2" # Volume up with tv on and muted
        tv.volume_up()
        assert tv.__str__() == "Power = True, Channel = 0, Volume = 2" # Volume up with tv on and at max volume
        
    def test_volume_down(self) -> None:
        """
        Method to test the volume_down method of the Television class.
        """
        tv = Television()
        tv.volume_down()
        assert tv.__str__() == "Power = False, Channel = 0, Volume = 0" # Attempt to volume down with tv off
        tv.power()
        tv.volume_up()
        tv.volume_up()
        tv.volume_down()
        assert tv.__str__() == "Power = True, Channel = 0, Volume = 1" # Volume down with tv on
        tv.volume_down()
        tv.mute()
        assert tv.__str__() == "Power = True, Channel = 0, Volume = 0" # Volume down with tv on and muted
        tv.volume_down()
        assert tv.__str__() == "Power = True, Channel = 0, Volume = 0" # Volume down with tv on and at min volume