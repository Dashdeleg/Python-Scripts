"""
Sample code for taking voltage measurement with the multimeter Agilent 34110A
    .. last edit: 25/4/2018
    .. section author:: Dashdeleg Baasanjav <d.baasanjav@uu.nl>
"""

import visa
import time
import threading
import numpy as np

"""
Initialize the device and print out the serial number
"""

rm = visa.ResourceManager()
multi = rm.open_resource('USB0::2391::1543::MY47004087::INSTR')
modelSerialnumber = multi.query('*IDN?')
print("Serial number of the multimeter is %s" %modelSerialnumber)

#%%
"""
Configure the multimeter
"""
# commands below just taken from oscilloscope code, not compatible with the multimeter!
multi.write(':WAVeform:SOURce %s' % (source2))
multi.write(':WAVeform:POINts %s' % ('1000'))
multi.write(':WAVeform:FORMat %s' % ('WORD'))
multi.write(':WAVeform:UNSigned %d' % (0))
multi.write(':WAVeform:BYTeorder %s' % ('LSBF'))
binaryBlockData = multi.query_binary_values(':WAVeform:DATA?','h',False)

#%%
"""
Run measurements
"""

f = open("Measurement3.dat", "w")

class TimerClass(threading.Thread):
    """
    Simple class for taking and reading out measurement every second from the multimeter.
    """
    def __init__(self):
        threading.Thread.__init__(self)
        self.event = threading.Event()

    def run(self):
        while not self.event.is_set():
           f.write(time.ctime() + ' ')  # current time
           V = multi.query('MEAS:VOLT:DC?') # read out measurement value
           f.write(str(V))
           self.event.wait(1)  # take measurement every second

    def stop(self):
        self.event.set()

tmr = TimerClass()
tmr.start()
time.sleep(3)  # specifies number of times measurement is taken
tmr.stop()    

f.close()

#%%
multi.close()  # close the device 
rm.close()  # close visa
