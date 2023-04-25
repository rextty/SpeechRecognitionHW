# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 16:25:11 2019

@author: BRASLab
"""
from scipy.io.wavfile import read
import scipy.io.wavfile as wav
from scipy import signal
import numpy as np
import matplotlib.pyplot as plt
import librosa


def levinson(Signal, order):
    x = Signal
    p = order
    autocorr = np.correlate(x, x, mode='full')
    r = autocorr[len(x) - 1:len(x) + p]

    a = np.zeros(p + 1)
    k = np.zeros(p)
    a[0] = 1
    a[1] = -r[1] / r[0]
    k[0] = a[1]
    E = r[0] + r[1] * a[1]

    for q in range(1, p):
        k[q] = -np.sum(a[0:q + 1] * r[q + 1:0:-1]) / E
        U = a[0:q + 2]
        V = U[::-1]
        a[0:q + 2] = U + k[q] * V
        E *= 1 - k[q] * k[q]

    return a, E


lpcOrder = 32  # LPC order
if __name__ == '__main__':
    filename = 'i.wav'

    x, sr = librosa.load(filename, sr=None)

    # 整個音訊檔的頻譜
    # spectrum from the LPC coefficients
    # --- 使用librosa.lpc來計算 LPC係數
    a = librosa.lpc(x, order=lpcOrder)  # 註: librosa.lpc(x,lpcOrder),其中輸入的x必須為浮點數
    lpc_spectrum = np.fft.fft(a, len(x))
    log_lpc_spectrum = -10 * np.log10(np.abs(lpc_spectrum))  # lpc_spectrum的倒數 再取log

    # --- 使用自己實現的 levinson 來計算 LPC係數
    a, e = levinson(x, lpcOrder)
    lpc_spectrum_lev = np.fft.fft(a, len(x))

    # 可加入squared prediction error e, 作為更正項;
    # 因為這裡我們取的是magnitude spectrum (NOT squared spectrum), 所以e要開根號
    log_lpc_spectrum_lev = 10 * np.log10(np.sqrt(e)) - 10 * np.log10(np.abs(lpc_spectrum_lev))

    # spectrum of the input signal x
    fft_x = np.fft.fft(x)
    log_fft_x = 10 * np.log10((np.abs(fft_x)))
    f_range = int(len(fft_x) / 2)  # 由於頻譜對稱 繪圖只需要一半
    freq = (np.arange(0, f_range) * sr) / len(fft_x)
    plt.plot(freq, log_fft_x[0:f_range], label='Signal')
    plt.plot(freq, log_lpc_spectrum[0:f_range], label='LPC')
    plt.plot(freq, log_lpc_spectrum_lev[0:f_range], label='levinson')
    plt.legend(loc='upper right')
    plt.title('/i/ order {0}'.format(lpcOrder))
    plt.xlabel('frequency [Hz]')
    plt.ylabel('Amplitute[dB]')
    plt.grid()

    # 音訊檔中的某一個frame之頻譜
    # fftL=512 #even number
    frame_size = 1024
    start = 0
    x_frame = x[start:start + frame_size]

    a = librosa.lpc(x_frame, order=lpcOrder)
    lpc_spectrum = np.fft.fft(a, len(x_frame))
    log_lpc_spectrum_ = -10 * np.log10(np.abs(lpc_spectrum))

    fft_x = np.fft.fft(x_frame)
    log_fft_x = 10 * np.log10(np.abs(fft_x))
    f_range_ = int(len(fft_x) / 2)  # 由於頻譜對稱 繪圖只需要一半
    freq_ = (np.arange(0, f_range_) * sr) / len(fft_x)

    # plt.plot(freq_, log_fft_x[0:f_range_], label='Signal')
    plt.plot(freq_, log_lpc_spectrum_[0:f_range_], label='LPC')
    # plt.legend(loc='upper right')
    # plt.title('one frame')
    # plt.xlabel('frequency [Hz]')
    # plt.ylabel('Amplitute[dB]')
    # plt.grid()

    # plt.plot(freq, log_lpc_spectrum[0:f_range], label='LPC (entire utterance)')
    # plt.plot(freq_, log_lpc_spectrum_[0:f_range_], label='LPC (one frame)')
    # plt.legend(loc='upper right')
    # plt.xlabel('frequency [Hz]')
    # plt.ylabel('Amplitute[dB]')
    # plt.grid()
    plt.show()

#    y_hat = signal.lfilter([0] + -1*a[1:], [1], x)
#    plt.figure()
#    plt.plot(x)
#    plt.plot(y_hat, linestyle='--')
#    plt.show()
