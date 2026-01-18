# Telegram Audio to Voice Converter Bot

Telegram-бот для конвертации аудиофайлов в голосовые сообщения формата .ogg (Opus), совместимого с Telegram.

## Основные функции

- Поддержка большинства аудиоформатов (MP3, WAV, M4A, OGG, FLAC и др.)
- Автоматическая конвертация в формат, рекомендованный Telegram: Opus, 24 кГц, моно, битрейт 32 кбит/с
- Удаление временных файлов после обработки
- Минимальная нагрузка на ресурсы сервера

## Установка

1. Создайте бота через @BotFather и получите токен доступа.:
2. Склонируйте репозиторий:
   ```bash
   git clone https://github.com/yourusername/bot-telegram-audio-to-voice.git
   cd bot-telegram-audio-to-voice
3. Установите зависимости:
   ```bash
   pip install aiogram
4. Установите FFmpeg (необходим для конвертации):
   - Ubuntu/Debian:
   ```bash
   sudo apt update && sudo apt install ffmpeg
  - macOS:
   ```bash
   brew install ffmpeg
  - Windows:
   Скачайте с официального сайта https://ffmpeg.org/download.html и добавьте в PATH
5. Укажите токен бота в коде (файл bot_audio_voice_converter.py):
   ```bash
   BOT_TOKEN = "ваш_токен_бота"
6. Укажите токен бота в коде (файл main.py или аналогичный):
   ```bash
   git clone https://github.com/yourusername/bot-telegram-audio-to-voice.git
   cd bot-telegram-audio-to-voice
7. Запустите приложение:
   ```bash
    python main.py
