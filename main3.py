
import numpy as np

import matplotlib.pyplot as plt

from iqtools import *



def main():
    filename = '0000072.iq.tdms'

    time_passed_upto_now = 0

    iq_data = TDMSData(filename)
   
    
  

    # extract hour min sec
    hr, placeholder = divmod(time_passed_upto_now, 3600)
    mnt, sec = divmod(placeholder, 60)
    total_time = '{}h-{}m-{}s'.format(int(hr), int(mnt), int(sec))
    title = 'Time: {}:{}:{}'.format(int(hr), int(mnt), int(sec))
  

    zz = np.array([])
    for j in range(1, 4096, 16):
        data = np.array([])
        
        for i in range(j, j + 16*262144):
            data = np.append(data, iq_data.read(i))
        data = np.reshape(data, (8, 262144 * 2))
        data_fft = np.fft.fft(data, axis=1)
        data_fft = np.average(data_fft, axis=0)
        data_fft = np.abs(np.fft.fftshift(data_fft))
        zz = np.append(zz, data_fft)

    zz = np.reshape(zz, (256, 262144 * 2))
    data_fft_freqs = np.fft.fftshift(
        np.fft.fftfreq(262144 * 2, d=1 / fs))  # in Hz
    xx, yy = np.meshgrid(data_fft_freqs, np.arange(256))
    
    plt_filename = '{}_{}'.format(iq_data.filename_wo_ext, total_time)
    print('Printing into file: ' + plt_filename)
    plot_spectrogram(xx, yy, zz, dbm=False, cmap=cm.jet,
                     filename=plt_filename, dpi=500, title=title)



if __name__ == '__main__':
    main()
