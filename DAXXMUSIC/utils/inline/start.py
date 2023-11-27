from pyrogram.types import InlineKeyboardButton

import config
from DAXXMUSIC import app


def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_1"], url=f"https://t.me/{app.username}?startgroup=true"
            ),
            InlineKeyboardButton(text=_["https://t.me/THE_DRAMA_CLUB_01"], url=config.SUPPORT_CHAT),
        ],
    ]
    return buttons


def private_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_3"],
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        ],
        [InlineKeyboardButton(text=_["S_B_4"], callback_data="settings_back_helper")],
        [
            InlineKeyboardButton(text=_["https://t.me/BAD_MUNDA_0"], user_id=config.OWNER_ID),
            InlineKeyboardButton(text=_["https://t.me/THE_DRAMA_CLUB_01"], url=config.SUPPORT_CHAT),
        ],
        [
            InlineKeyboardButton(text=_["https://t.me/ABT_BAD"], url=config.SUPPORT_CHANNEL),
            InlineKeyboardButton(text=_["https://t.me/BAD_BABY_01"], url=config.UPSTREAM_REPO),
        ],
    ]
    return buttons
