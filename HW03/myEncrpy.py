import matplotlib.pyplot as plt
import scipy.io.wavfile as wav
import numpy as np


class Main:
    def __init__(self):
        pass

    def run(self):
        # Step a.
        rate, y = wav.read("hello.wav")

        # Step b.
        z = np.flipud(y)

        # Step c.
        wav.write("encrypt.wav", rate, z)

        # Step d.
        fig, axs = plt.subplots(2)
        axs[0].set_title('Original Signal')
        axs[0].plot(y)
        axs[1].set_title('After Signal')
        axs[1].plot(z)
        plt.show()


if __name__ == "__main__":
    obj = Main()
    obj.run()
