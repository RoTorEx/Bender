from aiogram import F, Router, filters, html, types
from aiogram.types import Message

from bot.config.config_reader import load_config


router = Router()


@router.message(~(F.from_user.id.in_(load_config().tg_bot.admin_ids)), commands=["start"])
async def cmd_start(message: Message):
    await message.answer(f"Nice to see you, {message.from_user.first_name}.")


@router.message(F.from_user.id.in_(load_config().tg_bot.admin_ids), commands=["start"])
async def cmd_start_admin(message: Message):
    await message.answer("Hello, <b>Creator</b>!\n^_^", parse_mode="HTML")


@router.message(commands=["name"])
async def cmd_name(message: types.Message, command: filters.command.CommandObject):
    if command.args:
        await message.answer(f"Hello, <b>{command.args}</b>!", parse_mode="HTML")
    else:
        await message.answer("Please, enter your name after '/name' command!")
