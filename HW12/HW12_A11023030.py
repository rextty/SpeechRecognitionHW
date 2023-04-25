import matplotlib.pyplot as plt
import scipy.io.wavfile as wav
from scipy import stats
import dspBox as dsp
import numpy as np
import statistics
import math


def frame2sample(frameIndex, frameSize, overlap):
    step = frameSize - overlap
    sampleIndex = frameIndex * step
    return sampleIndex


class Main:
    def __init__(self):
        pass

    def run(self):
        # Initialize wav file.
        frameSize = 256
        overlap = 128
        wav_rate, wav_y = wav.read("hello.wav")

        # Normalization
        if wav_y.dtype == "int16":
            wav_y = wav_y / math.pow(2, 15)

        # zero-mean subtraction
        wav_y = stats.zscore(wav_y)

        frameMat = dsp.frameMat(wav_y, frameSize, overlap)  # 計算frame matrix (作業9)
        volume = dsp.volume(frameMat)  # 求出各個frame的音量

        # Determine Threshold → volumeThreshold?
        volumeTh1 = max(volume) * 0.1
        volumeTh2 = statistics.median(volume) * 0.1
        volumeTh3 = min(volume) * 10

        # 尋找在volume 陣列中有哪些值大於 volume threshold 的值, 並回傳值所對應的index
        index1 = [index for index, v in enumerate(volume) if v > volumeTh1]
        index2 = [index for index, v in enumerate(volume) if v > volumeTh2]
        index3 = [index for index, v in enumerate(volume) if v > volumeTh3]

        # 將EPD開始的frame 和 結束的frame 的時間找出來
        endpoint1 = frame2sample(np.array([index1[0], index1[-1]]), frameSize, overlap)
        endpoint2 = frame2sample(np.array([index2[0], index2[-1]]), frameSize, overlap)
        endpoint3 = frame2sample(np.array([index3[0], index3[-1]]), frameSize, overlap)

        # -------------------------------plot part---------------------------

        # np.sum(array)  # 將array元素全部加起來 ?
        # np.log10(x)  # 對x取 log10 ?

        plt.plot(wav_y)
        # 說明: 畫出(endpoint1[0] / rate, AmpMax) 與(endpoint1[0] / rate, AmpMin)
        # 這兩點所連成的直線 其中AmpMax為signal陣列中最大值, AmpMin反之, ‘r -‘:設定為紅線， lw: 設定線的寬度
        plt.plot([endpoint1[0] / wav_rate, endpoint1[0] / wav_rate], [max(wav_y), min(wav_y)], 'r-', lw=0.8)
        # plt.plot([endpoint2[0] / wav_rate, endpoint2[0] / wav_rate], [max(wav_y), min(wav_y)], 'r-', lw=0.8)
        # plt.plot([endpoint3[0] / wav_rate, endpoint3[0] / wav_rate], [max(wav_y), min(wav_y)], 'r-', lw=0.8)
        plt.show()


if __name__ == "__main__":
    obj = Main()
    obj.run()
