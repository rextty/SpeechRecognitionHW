import matplotlib.pyplot as plt
import scipy.io.wavfile as wav
import math


class Main:
    def __init__(self):
        pass

    def plot(self, data1, data2, title, sub_title="frame size=1024"):
        fig, axs = plt.subplots(2)
        axs[0].set_title(title)
        axs[0].plot(data1)

        axs[1].set_xlabel(sub_title)
        axs[1].plot(data2)
        plt.show()

    def run(self):
        # Initialize wav file.
        rate_440, y_440 = wav.read("440.wav")  # type = int16
        rate_tuningFork, y_tuningFork = wav.read("tuningFork.wav")  # type = uint8
        rate_Zhonghua, y_Zhonghua = wav.read("Zhonghua.wav")  # type = int16

        # Normalization
        y_440 = y_440 / math.pow(2, 15)
        y_tuningFork = (y_tuningFork - math.pow(2, 7)) / math.pow(2, 7)
        y_Zhonghua = y_Zhonghua / math.pow(2, 15)

        # Fundamental Frequency Extraction
        # 440.wav, tuningFork.wav   sampling period=1024, total Sampling point=256
        # Zhonghua.wav              sampling period=512 , total Sampling point=402
        waveform_440 = []
        for i in range(80000, 81024, int(1024/256)):
            waveform_440.append(y_440[i])

        waveform_tuningFork = []
        for i in range(11000, 11256, int(1024/256)):
            waveform_tuningFork.append(y_tuningFork[i])

        waveform_Zhonghua = []
        for i in range(20000, 20512, int(512/402)):
            waveform_Zhonghua.append(y_Zhonghua[i])

        # Plot 440.wav
        self.plot(y_440, waveform_440, "440fork.wav")

        # Plot tuningFork.wav
        self.plot(y_tuningFork, waveform_tuningFork, "tuningFork.wav")

        # Plot tuningFork.wav
        self.plot(y_Zhonghua, waveform_Zhonghua, "Zhonghua.wav", "frame size=512")


if __name__ == "__main__":
    obj = Main()
    obj.run()
