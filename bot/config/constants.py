from dataclasses import dataclass

from aiogram import Bot


@dataclass
class TgBot:
    bot: Bot
    admin_list: list
    customer_list: list
