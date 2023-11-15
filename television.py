

class Television():
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3
    
    def __init__(self):
        self.__status = False
        self.__muted = False
        self.__volume = self.MIN_VOLUME
        self.__channel = self.MIN_CHANNEL
        self.__stored_volume = 0
        
    def power(self):
        self.__status = not self.__status
        
    def mute(self):
        if self.__status == True:
            if self.__muted == False:
                self.__muted = True
                self.__stored_volume = self.__volume
                self.__volume = self.MIN_VOLUME
            else:
                self.__muted = False
                self.__volume = self.__stored_volume
    
    def channel_up(self):
        if self.__status == True:
            if self.__channel < self.MAX_CHANNEL:
                self.__channel += 1
            else:
                self.__channel = self.MIN_CHANNEL
                
    def channel_down(self):
        if self.__status == True:
            if self.__channel > self.MIN_CHANNEL:
                self.__channel -= 1
            else:
                self.__channel = self.MAX_CHANNEL
                
    def volume_up(self):
        if self.__status == True:
            if self.__muted == True:
                self.__muted = False
                self.__volume = self.__stored_volume
            if self.__volume < self.MAX_VOLUME:
                self.__volume += 1

    def volume_down(self):
        if self.__status == True:
            if self.__muted == True:
                self.__muted = False
                self.__volume = self.__stored_volume
            if self.__volume > self.MIN_VOLUME:
                self.__volume -= 1
                
    def __str__(self):
        return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}'
