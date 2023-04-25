import matplotlib.pyplot as plt
import scipy.io.wavfile as wav
import onesidespectra as one
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

        # Initialize wav file.
        a_rate, a_y = wav.read("a.wav")

        # Normalization
        if a_y.dtype == "int16":
            a_y = a_y / math.pow(2, 15)

        frame = a_y[10000:10512]
        frq, y = one.One_sided_spectra(frame, 16)

        wav.write("AfHightPass.wav", a_rate, one.One_sided_spectra(a_y, 16)[1])

        self.plot(frame, y, "Original Wave", "After Pre-emphasis")


if __name__ == "__main__":
    obj = Main()
    obj.run()
