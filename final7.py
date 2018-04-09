import numpy as np

import matplotlib.pyplot as plt

from iqtools import *



def main():
    
    filename = '0000000.iq.tdms'
    iq_data = TDMSData(filename)
    fs=8000000
   
    iq_data.read(4088,2**18,1)
    print(np.shape(iq_data.data_array))
	
    
    zz1 = np.reshape(iq_data.data_array, (511, 2**18 *8))

    zz1 = np.fft.fft(zz1,axis=1)
    zz1 = np.abs(np.fft.fftshift(zz1))
    #data_fft_freqs = np.fft.fftshift(np.fft.fftfreq(2**18 * 8, d=1 / fs)) # in Hz
    #zz = np.append(zz, data_abs)
    #print(np.shape(data_abs))
    filename = '0000001.iq.tdms'
    iq_data = TDMSData(filename)
    #fs=8000000
   
    iq_data.read(4088,2**18,1)
    print(np.shape(iq_data.data_array))
	
    
    zz2 = np.reshape(iq_data.data_array, (511, 2**18 *8))

    zz2 = np.fft.fft(zz2,axis=1)
    zz2 = np.abs(np.fft.fftshift(zz2))
    zz = np.concatenate((zz2,zz1),axis=0)

    xx, yy = np.meshgrid(np.arange(2097152), np.arange(1022))
    #xx, yy = np.meshgrid(data_fft_freqs, np.arange(511))
    yy = yy*(0.524288000/2) #in secs
    #xx = xx*data_fft_freqs
    #xx,yy[994836:1006633,0:]

    print(np.shape(zz))
    print(np.shape(xx))
    print(np.shape(yy))
    plot_spectrogram(xx[0:,994896:1006633], yy[0:,994896:1006633], zz[0:,994896:1006633], dbm=False, cmap=cm.jet, 
                                   filename='saka.tdms', dpi=500)


if __name__ == '__main__':
    main() 

