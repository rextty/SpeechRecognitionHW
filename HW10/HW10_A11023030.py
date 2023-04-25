import matplotlib.pyplot as plt
import scipy.io.wavfile as wav
import numpy as np
import DSPbox as dsp
import math


class Main:
    def __init__(self):
        pass

    def plot(self, data1, data2, title, sub_title):
        fig, axs = plt.subplots(2)

        # Enable zoom to rectangle
        fig.canvas.toolbar.zoom()

        axs[0].set_title(title)
        axs[0].plot(data1)

        axs[1].set_xlabel(sub_title)
        axs[1].plot(data2)

        plt.show()

    def run(self):
        frameSize = 512
        overlap = 128

        # Initialize wav file.
        wav_rate, wav_y = wav.read("HappyNewYear.wav")

        # Normalization
        if wav_y.dtype == "int16":
            wav_y = wav_y / math.pow(2, 15)
        frameCut = dsp.frameMat(wav_y, frameSize, overlap)
        rows, cols = frameCut.shape
        volumeArray = np.zeros(cols)
        volumeDBArray = np.zeros(cols)

        for i in range(0, cols, 1):
            # abs sum
            frame = frameCut[:, i] - np.mean(frameCut[:, i])
            volumeArray[i] = np.sum(np.absolute(frame))
            # Decibels
            frame = frameCut[:, i] - np.median(frameCut[:, i])
            volumeDBArray[i] = 10 * np.log10(np.sum(frame ** 2))

        sampleTime = np.linspace(1, np.size(wav_y), np.size(wav_y)) / wav_rate
        frameTime = (np.linspace(0, cols, cols) * (frameSize - overlap)) / wav_rate

        plt.subplot(311)
        plt.plot(sampleTime, wav_y)

        plt.ticklabel_format(style='sci', axis='y', scilimits=(0, 0))
        plt.ylabel('Amplitude')

        plt.subplot(312)
        plt.plot(frameTime, volumeArray)
        plt.ticklabel_format(style='sci', axis='y')
        plt.ylabel('volume, Abs_sum')
        # 設定y軸刻度單位為科學符號
        plt.ticklabel_format(style='sci', axis='y', scilimits=(0, 0))

        plt.subplot(313)
        plt.plot(frameTime, volumeDBArray)
        plt.xlabel('Time')
        plt.ylabel('volume ,decibels')
        plt.show()


if __name__ == "__main__":
    obj = Main()
    obj.run()
