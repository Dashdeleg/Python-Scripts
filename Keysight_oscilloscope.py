# start of the program
import visa
import time
import numpy as np

# Parameters
frequency=1
amplitude=0.00001
offset=0
percent=50
source1='CHANNEL1'
source2='CHANNEL3'
count = 0
n = 10
# =========================================================
# Initialize:
# =========================================================
rm = visa.ResourceManager()
oscil = rm.open_resource('USB0::0x0957::0x1796::MY56202118::0::INSTR')
modelSerialnumber = oscil.query('*IDN?')
print("Serial number of the oscillocope is %s" %modelSerialnumber)
# =========================================================
# Waveform generation:
# =========================================================
oscil.write(':WGEN:OUTPut %d' % (1))
oscil.write(':WGEN:FUNCtion %s' % ('SQUare'))
oscil.write(':WGEN:FREQuency %G' % (frequency))
oscil.write(':WGEN:VOLTage %G' % (amplitude))
oscil.write(':WGEN:VOLTage:OFFSet %G' % (offset))
oscil.write(':WGEN:FUNCtion:SQUare:DCYCle %d' % (percent))
# =========================================================
# Sending commands to Oscilloscope interface:
# =========================================================
oscil.write(':MEASure:VPP %s' % ('CHANNEL1'))
oscil.write(':DIGitize %s' % (source1))
Vpp = oscil.query(':MEASure:VPP?')
print(Vpp)
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
oscil.close()
rm.close()

# end of Untitled
























