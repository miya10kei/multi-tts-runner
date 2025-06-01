# Multi TTS Runner

複数のTTS（Text-to-Speech）サービスを使用して、テキストから音声を生成するツールです。現在は以下のサービスをサポートしています：

- OpenAI TTS API
- Google Gemini TTS API

## 機能

- 複数のTTSサービスを並列で実行
- 各サービスの異なる音声とモデルを試すことが可能
- 生成された音声はWAVファイルとして保存

## 必要条件

- Python 3.13以上
- [uv](https://github.com/astral-sh/uv) (高速なPythonパッケージインストーラー)
- OpenAI APIキー
- Google Gemini APIキー

## セットアップ

1. リポジトリをクローン
```bash
git clone https://github.com/miya10kei/multi-tts-runner.git
cd multi-tts-runner
```

2. 仮想環境の作成と依存パッケージのインストール
```bash
# 仮想環境の作成と依存パッケージのインストール
uv sync
```

3. 環境変数の設定
```bash
# OpenAI APIキー
export OPENAI_API_KEY="your-openai-api-key"

# Google Gemini APIキー
export GOOGLE_API_KEY="your-google-api-key"
```

## 使用方法

1. テキストを標準入力から渡して実行
```bash
echo "こんにちは、世界" | uv run python src/main.py
```

2. 生成された音声ファイルは `out` ディレクトリに保存されます
   - OpenAI: `out/openai_[model]_[voice].wav`
   - Gemini: `out/gemini_[model]_[voice].wav`

## サポートされている音声とモデル

### OpenAI
- モデル:
  - tts-1
  - tts-1-hd
  - gpt-4o-mini-tts
- 音声:
  - alloy
  - ash
  - ballad
  - coral
  - echo
  - fable
  - nova
  - onyx
  - sage
  - shimmer

### Gemini
- モデル:
  - gemini-2.5-pro-preview-tts
  - gemini-2.5-flash-preview-tts
- 音声:
  - Zephyr (明るい)
  - Puck (アップビート)
  - Charon (情報提供)
  - Fenrir (興奮しやすい)
  - Leda (若々しい)
  - Aoede (Breezy)
  - Callirrhoe (おおらか)
  - Orus (会社)
  - Autonoe (明るい)
  - Enceladus (息づかい)
  - Iapetus (クリア)
  - Umbriel (気楽な)
  - Algieba (スムーズ)
  - Despina (スムーズ)
  - Erinome (クリア)
  - Algenib (砂利)
  - Rasalgethi (情報に富んでいる)
  - Laomedeia (アップビート)
  - Achernar (ソフト)
  - Alnilam (確実)
  - Schedar (Even)
  - Gacrux (成人向け)
  - Pulcherrima (前方)
  - Achird (フレンドリー)
  - Zubenelgenubi (カジュアル)
  - Vindemiatrix (優しい)
  - Sadachbia (活発)
  - Sadaltager (知識豊富)
  - Sulafat (温かい)
