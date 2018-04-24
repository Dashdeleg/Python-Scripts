"""
Sample code for taking voltage measurement with the multimeter Agilent 34110A
    .. last edit: 24/4/2018
    .. section author:: Dashdeleg Baasanjav <d.baasanjav@uu.nl>
"""

import visa
import time
import numpy as np

"""
Initialize the device and print out the serial number
"""

rm = visa.ResourceManager()
multi = rm.open_resource('USB0::2391::1543::MY47004087::INSTR')
modelSerialnumber = multi.query('*IDN?')
print("Serial number of the oscillocope is %s" %modelSerialnumber)

#%%
"""
Send commands to the multimeter
"""

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

f = open("Measurement.dat", "w")
while count < n:
    multi.write(':DIGitize %s' % (source1))
    Vpp = multi.query(':MEASure:VPP?')
    f.write(str(Vpp))
    count = count +1
f.close()

multi.close()  # close the device 
rm.close()  # close visa
