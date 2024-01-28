import config
import RPi.GPIO as GPIO


channel_A   = 0x30
channel_B   = 0x34

DAC_Value_MAX = 65535

DAC_VREF = 3.3

class DAC8532:
    def __init__(self):
        self.cs_line = config.CS_DAC_LINE
        # config.module_init()
        
    
    def DAC8532_Write_Data(self, Channel, Data):
        config.digital_write(self.cs_line, 0) #cs  0
        config.spi_writebyte([Channel, Data >> 8, Data & 0xff])
        config.digital_write(self.cs_line, 1) #cs  0
        
    def DAC8532_Out_Voltage(self, Channel, Voltage):
        if((Voltage <= DAC_VREF) and (Voltage >= 0)):
            temp = int(Voltage * DAC_Value_MAX / DAC_VREF)
            self.DAC8532_Write_Data(Channel, temp)
  
### END OF FILE ###

