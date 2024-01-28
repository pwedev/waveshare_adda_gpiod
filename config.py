# /*****************************************************************************
# * | File        :	  EPD_1in54.py
# * | Author      :   Waveshare team
# * | Function    :   Hardware underlying interface
# * | Info        :
# *----------------
# * |	This version:   V1.0
# * | Date        :   2019-01-24
# * | Info        :   
# ******************************************************************************/
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documnetation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to  whom the Software is
# furished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS OR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
#


import spidev
import gpiod
import time

# Pin definition
RST_PIN         = 18
CS_PIN          = 22
CS_DAC_PIN      = 23
DRDY_PIN        = 17

# SPI device, bus = 0, device = 0
SPI = spidev.SpiDev(0, 0)

# Open gpiod Chip 
chip = gpiod.Chip("gpiochip4")

RST_LINE = chip.get_line(RST_PIN)
CS_LINE = chip.get_line(CS_PIN) 
CS_DAC_LINE = chip.get_line(CS_DAC_PIN)
DRDY_LINE = chip.get_line(DRDY_PIN)

def digital_write(line, value):
    line.set_value(value)

def digital_read(line):
    return line.get_value()

def delay_ms(delaytime):
    time.sleep(delaytime // 1000.0)

def spi_writebyte(data):
    SPI.writebytes(data)
    
def spi_readbytes(reg):
    return SPI.readbytes(reg)
    

def module_init():
    # Define lines
    RST_LINE.request(consumer="ads1256", type=gpiod.LINE_REQ_DIR_OUT)
    CS_LINE.request(consumer="ads1256", type=gpiod.LINE_REQ_DIR_OUT)
    CS_DAC_LINE.request(consumer="ads1256", type=gpiod.LINE_REQ_DIR_OUT)
    DRDY_LINE.request(consumer="ads1256", type=gpiod.LINE_REQ_DIR_IN)
   
    SPI.max_speed_hz = 20000
    SPI.mode = 0b01
    return 0;

### END OF FILE ###
