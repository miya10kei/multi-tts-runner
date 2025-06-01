from enum import Enum
from typing import Optional

from google import genai
from google.genai import types


class GeminiTTSVoiceName(Enum):
    Zephyr = "Zephyr"  # 明るい
    Puck = "Puck"  # アップビート
    Charon = "Charon"  # 情報提供
    Fenrir = "Fenrir"  # 興奮しやすい
    Leda = "Leda"  # 若々しい
    Aoede = "Aoede"  # Breezy
    Callirrhoe = "Callirrhoe"  # おおらか
    Orus = "Orus"  # 会社
    Autonoe = "Autonoe"  # 明るい
    Enceladus = "Enceladus"  # 息づかい
    Iapetus = "Iapetus"  # クリア
    Umbriel = "Umbriel"  # 気楽な
    Algieba = "Algieba"  # スムーズ
    Despina = "Despina"  # スムーズ
    Erinome = "Erinome"  # クリア
    Algenib = "Algenib"  # 砂利
    Rasalgethi = "Rasalgethi"  # 情報に富んでいる
    Laomedeia = "Laomedeia"  # アップビート
    Achernar = "Achernar"  # ソフト
    Alnilam = "Alnilam"  # 確実
    Schedar = "Schedar"  # Even
    Gacrux = "Gacrux"  # 成人向け
    Pulcherrima = "Pulcherrima"  # 前方
    Achird = "Achird"  # フレンドリー
    Zubenelgenubi = "Zubenelgenubi"  # カジュアル
    Vindemiatrix = "Vindemiatrix"  # 優しい
    Sadachbia = "Sadachbia"  # 活発
    Sadaltager = "Sadaltager"  # 知識豊富
    Sulafat = "Sulafat"  # 温かい


class GeminiTTSModel(Enum):
    Pro_2_5 = "gemini-2.5-pro-preview-tts"
    Flash_2_5_ = "gemini-2.5-flash-preview-tts"


class GeminiClient:

    def __init__(self):
        self.gemini = genai.Client()

    def generate(
        self,
        text: str,
        voice_name: GeminiTTSVoiceName = GeminiTTSVoiceName.Sulafat,
        model: GeminiTTSModel = GeminiTTSModel.Pro_2_5,
    ) -> Optional[bytes]:
        try:
            response = self.gemini.models.generate_content(
                model=model.value,
                contents=text,
                config=types.GenerateContentConfig(
                    response_modalities=["AUDIO"],
                    speech_config=types.SpeechConfig(
                        language_code="ja-JP",
                        voice_config=types.VoiceConfig(
                            prebuilt_voice_config=types.PrebuiltVoiceConfig(
                                voice_name=voice_name.value,
                            )
                        ),
                    ),
                ),
            )
            return response.candidates[0].content.parts[0].inline_data.data
        except Exception as e:
            print(f"Gemini TTS error: {e}")
            return None
