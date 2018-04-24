# start of the program
import visa
import time
import numpy as np

# =========================================================
# Initialize:
# =========================================================
rm = visa.ResourceManager()
multi = rm.open_resource('USB0::2391::1543::MY47004087::INSTR')
modelSerialnumber = multi.query('*IDN?')
print("Serial number of the oscillocope is %s" %modelSerialnumber)

# =========================================================
# Signal acquisition:
# =========================================================
"""
oscil.write(':WAVeform:SOURce %s' % (source2))
oscil.write(':WAVeform:POINts %s' % ('1000'))
oscil.write(':WAVeform:FORMat %s' % ('WORD'))
oscil.write(':WAVeform:UNSigned %d' % (0))
oscil.write(':WAVeform:BYTeorder %s' % ('LSBF'))
binaryBlockData = oscil.query_binary_values(':WAVeform:DATA?','h',False)
# =========================================================
# Making measurements:
# =========================================================
f = open("Measurement.dat", "w")
while count < n:
    oscil.write(':DIGitize %s' % (source1))
    Vpp = oscil.query(':MEASure:VPP?')
    f.write(str(Vpp))
    count = count +1
f.close()
"""
# =========================================================
# Finialize:
# =========================================================
multi.close()
rm.close()

























