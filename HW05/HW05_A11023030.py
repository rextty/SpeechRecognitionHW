import matplotlib.pyplot as plt
import scipy.io.wavfile as wav
import math


class Main:
    def __init__(self):
        pass

    def run(self):
        # Step a.
        rate, y = wav.read("hide.wav")  # type is int16

        fig, axs = plt.subplots(2)
        axs[0].set_title('Original Audio')
        axs[0].plot(y)

        # Step b.
        z = y / math.pow(2, 15)
        axs[1].set_title('After Normalization')
        axs[1].plot(z)
        plt.show()


if __name__ == "__main__":
    obj = Main()
    obj.run()
