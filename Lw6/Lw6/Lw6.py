TURNED_OFF_CHANNEL = 0
MIN_CHANNEL = 1
MAX_CHANNEL = 10
NOT_FOUND_CHANNEL = -1
INIT_STARTED_CHANNEL = 1

class TV:
    def __init__(self):
        self.selectedChannel = INIT_STARTED_CHANNEL
        self.previousChannel = 1
        self.isOn = False
        self.listOfChannels = { 
            1: "1", 
            2: "2", 
            3: "3", 
            4: "4", 
            5: "5",
            6: "6",
            7: "7",
            8: "8",
            9: "9",
            10: "10"}

    def IsTurnedOn(self):                                                    
        return self.isOn
    
    def TurnOn(self):                                                         
        self.isOn = True

    def TurnOff(self):                                                         
        self.isOn = False

    def GetChannel(self):                                                      
        if (self.isOn):
            for key, value in self.listOfChannels.items():
                if(key == self.selectedChannel):
                    FoundChannelName = value
            return {self.selectedChannel: FoundChannelName}
        else:
            return  TURNED_OFF_CHANNEL

    def GetListOfChannel(self):                                                
        if (self.isOn):
            return self.listOfChannels
        else:
            return "TV is off" 


    def SelectChannel(self, channel):                                            
        if (self.CheckChannelRange(channel) and self.isOn):
            self.previousChannel = self.selectedChannel
            self.selectedChannel = channel
        else :
            return "TV is off"

    def SelectChannelByName(self, name):                                           
        if (self.isOn):
            for key, value in self.listOfChannels.items():
                if(value == name):
                    self.previousChannel = self.selectedChannel
                    self.selectedChannel = key
        else :
            return "TV is off"

    def CheckChannelRange(self, channel):
        if (channel >= MIN_CHANNEL and channel <= MAX_CHANNEL):
            return True
        else:
            return  False

    def SelectPreviousChannel(self):                                            
        if (self.isOn):
            temp = self.selectedChannel
            self.selectedChannel = self.previousChannel
            self.previousChannel = temp
            return self.selectedChannel
        else:
            return  TURNED_OFF_CHANNEL
        

