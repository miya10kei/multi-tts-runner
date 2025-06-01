import wave

import numpy as np
from scipy.signal import butter, resample_poly, sosfilt


class Audio:

    def save_file_as_wav(
        self,
        filepath: str,
        pcm: bytes,
        channel: int = 1,
        src_rate: int = 24000,
        dst_rate: int = 8000,
        sample_width: int = 2,
    ):
        if src_rate != dst_rate:
            pcm = self.__downsample(pcm, src_rate=src_rate, dst_rate=dst_rate)

        with wave.open(filepath, "wb") as wf:
            wf.setnchannels(channel)
            wf.setsampwidth(sample_width)
            wf.setframerate(dst_rate)
            wf.writeframes(pcm)

    def __downsample(self, pcm: bytes, src_rate: int, dst_rate: int):
        audio_int16 = np.frombuffer(pcm, dtype=np.int16)

        # ローパスフィルタで高域ノイズ(3600Hz以上)をカット
        filtered = self.__apply_lowpass_filter(audio_int16, cutoff=3600, fs=src_rate)

        # リサンプル（polyphase法、音質良）
        resampled = resample_poly(filtered, dst_rate, src_rate)

        # 正規化 + クリッピング
        max_val = np.max(np.abs(resampled))
        if max_val > 0:
            resampled /= max_val
        resampled = np.clip(resampled, -1.0, 1.0)

        audio_int16 = np.int16(resampled * 32767)
        return audio_int16.tobytes()

    def __apply_lowpass_filter(self, audio: np.ndarray, cutoff: float, fs: int):
        sos = butter(10, cutoff, btype="low", fs=fs, output="sos")
        return sosfilt(sos, audio)
