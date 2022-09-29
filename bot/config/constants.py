from dataclasses import dataclass

from aiogram import Bot


@dataclass
class TgBot:
    bot: Bot
    admin_list: list[int]
    customer_list: list[int]
