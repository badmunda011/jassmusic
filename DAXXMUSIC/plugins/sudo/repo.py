import asyncio

from pyrogram import filters

import config
from DAXXMUSIC import app
from DAXXMUSIC.utils.formatters import convert_bytes





@app.on_message(filters.command("repo"))
async def varsFunc(client, message):
    mystic = await message.reply_text(
        "⎯꯭̽🇨🇦꯭꯭ ⃪В꯭α꯭∂ ꯭м꯭υ꯭η∂꯭α_꯭آآ⎯꯭ ꯭̽🌸"
    )

 ##############
 
    text = f"""ਤਕ‌ੜੇ💪 ਮੂਹਰੇ👉 ਕਦੇ ਜੀ ਜੀ🙏 ਨੀ ❌ਕੀਤਾ ਤੇ,
ਮਾੜੇ 😡ਨੂੰ ਦੇਖ👀 ਕੇ ਹੱਸਦੇ 😂ਨੀਂ,
ਆਪਣੀ ☝🏻🌎ਦੁਨੀਆਂ👉 ਵਿੱਚ ਮਸਤ😎 ਰਹਿੰਦੇ ਆ।
ਐਵੇਂ 😏ਕਿਸੇ 👉ਨੂੰ ਦੇਖ 👀ਕੇ ਮੱਚਦੇ 😅ਨੀ,
ਜੋ 👉ਦਿਲ ♥️ਚ ਉਹੀ ਮੂੰਹ 🗣️ਤੇ ਆ,
ਤਾਂ 👉ਹੀ ਬਹੁਤਿਆਂ👥 ਨੂੰ ਅਸੀਂ😎 ਜੱਚਦੇ😏 ਨੀ।।
✍🏻
"""
    await asyncio.sleep(1)
    await mystic.edit_text(text)
