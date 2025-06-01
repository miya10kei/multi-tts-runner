import os
import sys
from concurrent.futures import ThreadPoolExecutor

from audio import Audio
from gemini_client import GeminiClient, GeminiTTSModel, GeminiTTSVoiceName
from openai_client import OpenAIClient, OpenAITTSModel, OpenAITTSVoiceName

OUTPUT_DIR = "./out"


def generate_voice_with_gemini(
    gemini: GeminiClient, audio: Audio, text: str, model: GeminiTTSModel, voice_name: GeminiTTSVoiceName
):
    pcm = gemini.generate(text, voice_name, model)
    filepath = f"{OUTPUT_DIR}/gemini_{model.value}_{voice_name.value}.wav".lower()
    if pcm:
        audio.save_file_as_wav(filepath, pcm)
        print(f"{filepath} に保存しました")
    else:
        print(f"音声生成に失敗しました。(model={model.value}, voice_name={voice_name.value}")


def generate_voice_with_openai(
    openai: OpenAIClient, audio: Audio, text: str, model: OpenAITTSModel, voice_name: OpenAITTSVoiceName
):
    audio_data = openai.generate(text, voice_name, model)
    filepath = f"{OUTPUT_DIR}/openai_{model.value}_{voice_name.value}.wav".lower()
    if audio_data:
        audio.save_file_as_wav(filepath, audio_data)
        print(f"{filepath} に保存しました")
    else:
        print(f"音声生成に失敗しました。(model={model.value}, voice_name={voice_name.value}")


def main():
    text = sys.stdin.read()

    if not text:
        print("標準入力にテキストを渡してください。")
        sys.exit(1)
    print(f"テキスト: {text}")

    os.makedirs(OUTPUT_DIR, exist_ok=True)

    gemini = GeminiClient()
    openai = OpenAIClient()
    audio = Audio()
    with ThreadPoolExecutor(max_workers=4) as executor:
        # Geminiの音声生成
        # for model in GeminiTTSModel:
        #     for voice_name in GeminiTTSVoiceName:
        #         executor.submit(generate_voice_with_gemini, gemini, audio, text, model, voice_name)

        # OpenAIの音声生成
        for model in OpenAITTSModel:
            for voice_name in OpenAITTSVoiceName:
                executor.submit(generate_voice_with_openai, openai, audio, text, model, voice_name)


if __name__ == "__main__":
    main()
