from enum import Enum
from typing import Optional

from openai import OpenAI


class OpenAITTSVoiceName(Enum):
    Alloy = "alloy"
    Ash = "ash"
    Ballad = "ballad"
    Coral = "coral"
    Echo = "echo"
    Fable = "fable"
    Nova = "nova"
    Onyx = "onyx"
    Sage = "sage"
    Shimmer = "shimmer"


class OpenAITTSModel(Enum):
    TTS_1_HD = "tts-1-hd"
    TTS_1 = "tts-1"
    TTS_4O_MINI = "gpt-4o-mini-tts"


class OpenAIClient:
    def __init__(self):
        self.client = OpenAI()

    def generate(
        self,
        text: str,
        voice_name: OpenAITTSVoiceName = OpenAITTSVoiceName.Alloy,
        model: OpenAITTSModel = OpenAITTSModel.TTS_1_HD,
    ) -> Optional[bytes]:
        try:
            response = self.client.audio.speech.create(
                model=model.value, voice=voice_name.value, input=text, response_format="pcm", speed=1.0
            )
            return response.content
        except Exception as e:
            print(f"OpenAI TTS API error: {e}")
            return None
