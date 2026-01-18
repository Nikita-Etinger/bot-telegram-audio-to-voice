import asyncio
import logging
from pathlib import Path
import subprocess
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from aiogram.types import FSInputFile, Message

# ────────────────────────────────────────────────
BOT_TOKEN = "YOUR_BOT_TOKEN"


TEMP_DIR = Path("temp_audio")
TEMP_DIR.mkdir(exist_ok=True)

logging.basicConfig(level=logging.INFO)
bot = Bot(BOT_TOKEN)
dp = Dispatcher()


@dp.message(CommandStart())
async def start(message: Message):
    await message.answer(
        "Пришли мне аудиофайл (.mp3, .wav, .m4a и т.д.)\n"
        "Я превращу его в голосовое сообщение 🎤"
    )


@dp.message(lambda m: m.audio or (m.document and m.document.mime_type and m.document.mime_type.startswith("audio/")))
async def audio_to_voice(message: Message):
    file = message.audio or message.document

    if not file:
        await message.reply("Это не аудиофайл...")
        return

    try:

        file_info = await bot.get_file(file.file_id)
        original_path = TEMP_DIR / f"orig_{file.file_id}{Path(file.file_name or '').suffix or '.mp3'}"
        await bot.download_file(file_info.file_path, original_path)


        voice_path = TEMP_DIR / f"voice_{file.file_id}.ogg"


        cmd = [
            "ffmpeg", "-y", "-i", str(original_path),
            "-acodec", "libopus",
            "-ac", "1",
            "-ar", "24000",
            "-b:a", "32k",
            "-vbr", "off",
            "-compression_level", "10",
            str(voice_path)
        ]

        result = subprocess.run(cmd, capture_output=True, text=True)

        if result.returncode != 0:
            logging.error(f"FFmpeg error:\n{result.stderr}")
            await message.reply("Не получилось конвертировать файл 😓")
            return

        # Отправляем как голосовое
        await message.reply_voice(
            voice=FSInputFile(voice_path),
            caption="Вот твоё аудио в виде голосового 🎙️",
            duration=getattr(file, "duration", None)
        )


        original_path.unlink(missing_ok=True)
        voice_path.unlink(missing_ok=True)

    except Exception as e:
        logging.exception("Ошибка при обработке аудио")
        await message.reply("Что-то сломалось... попробуй другой файл")


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())