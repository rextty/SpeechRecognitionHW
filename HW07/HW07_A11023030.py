import matplotlib.pyplot as plt
import scipy.io.wavfile as wav


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
        a_rate, a_y = wav.read("a.wav")  # type = int16
        p_rate, p_y = wav.read("p.wav")  # type = int16

        # Normalization
        # a_y = a_y / math.pow(2, 15)
        # p_y = p_y / math.pow(2, 15)

        p_range_start = 33000
        p_range_end = 40000
        p_step = int((p_range_end - p_range_start) / 512)

        p_speech_segment = []
        for i in range(p_range_start, p_range_end, p_step):
            p_speech_segment.append(p_y[i])

        a_range_start = 48400
        a_range_end = 50000
        a_step = int((a_range_end - a_range_start) / 512)

        a_speech_segment = []
        for i in range(a_range_start, a_range_end, a_step):
            a_speech_segment.append(a_y[i])

        self.plot(p_y, p_speech_segment, "p.wav", "")
        self.plot(a_y, a_speech_segment, "a.wav", "")


if __name__ == "__main__":
    obj = Main()
    obj.run()
