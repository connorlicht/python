class Television():
    """
    A class representing actions of a television.
    """
    MIN_VOLUME: int = 0
    MAX_VOLUME: int = 2
    MIN_CHANNEL: int = 0
    MAX_CHANNEL: int = 3
    
    def __init__(self) -> None:
        """
        Method to initialize the attributes of the Television class.
        """
        self.__status: bool = False
        self.__muted: bool = False
        self.__volume: int = Television.MIN_VOLUME
        self.__channel: int = Television.MIN_CHANNEL
        self.__stored_volume: int = 0
        
    def power(self) -> None:
        """
        Method to toggle the power of the television.
        """
        self.__status = not self.__status
        
    def mute(self) -> None:
        """
        Method to mute and unmute the television.
        """
        if self.__status == True:
            if self.__muted == False:
                self.__muted = True
                self.__stored_volume = self.__volume
                self.__volume = Television.MIN_VOLUME
            else:
                self.__muted = False
                self.__volume = self.__stored_volume
    
    def channel_up(self) -> None:
        """
        Method to increase the channel of the television.
        """
        if self.__status == True:
            if self.__channel < Television.MAX_CHANNEL:
                self.__channel += 1
            else:
                self.__channel = Television.MIN_CHANNEL
                
    def channel_down(self) -> None:
        """
        Method to decrease the channel of the television.
        """
        if self.__status == True:
            if self.__channel > Television.MIN_CHANNEL:
                self.__channel -= 1
            else:
                self.__channel = Television.MAX_CHANNEL
                
    def volume_up(self) -> None:
        """
        Method to increase the volume of the television.
        """
        if self.__status == True:
            if self.__muted == True:
                self.__muted = False
                self.__volume = self.__stored_volume
            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1

    def volume_down(self) -> None:
        """
        Method to decrease the volume of the television.
        """
        if self.__status == True:
            if self.__muted == True:
                self.__muted = False
                self.__volume = self.__stored_volume
            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1
                
    def __str__(self) -> str:
        """
        Method to return the string representation of the Television class.
        :return: The string representation of the Television class.
        """
        return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}'
