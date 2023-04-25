import matplotlib.pyplot as plt
import scipy.io.wavfile as wav
import librosa
import math


class Main:
    def __init__(self):
        pass

    def run(self):
        # Initialize wav file.
        wav_rate, wav_y = wav.read("hello.wav")

        # Normalization
        if wav_y.dtype == "int16":
            wav_y = wav_y / math.pow(2, 15)

        mfcc = librosa.feature.mfcc(y=wav_y, sr=wav_rate, n_mfcc=13, n_fft=int(wav_rate*0.025), hop_length=int(wav_rate*0.01))

        fig, axs = plt.subplots(3)
        # Enable zoom to rectangle
        fig.canvas.toolbar.zoom()

        axs[0].set_title("MFCC")
        axs[0].plot(mfcc[0])
        axs[0].plot(mfcc[1])
        axs[0].plot(mfcc[2])

        mfcc_2 = librosa.feature.delta(mfcc)

        axs[1].set_title("△MFCC")
        axs[1].plot(mfcc_2[0])
        axs[1].plot(mfcc_2[1])
        axs[1].plot(mfcc_2[2])

        mfcc_3 = librosa.feature.delta(mfcc_2)

        axs[2].set_title("△2MFCC")
        axs[2].plot(mfcc_3[0])
        axs[2].plot(mfcc_3[1])
        axs[2].plot(mfcc_3[2])

        plt.show()


if __name__ == "__main__":
    obj = Main()
    obj.run()
