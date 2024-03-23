import asyncio
import logging

from apscheduler.schedulers.asyncio import AsyncIOScheduler
from aiogram import Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage


from src.check_status import check_status
from src.handlers.help_handlers import router as help_r
from src.handlers.admin_handlers import bot, router as admin_r
from src.handlers.tarif_handlers import router as tarif_r
from src.handlers.commands_handlers import router as command_r
from src.handlers.statusPay_handlers import router as sp_router
from src.handlers.loadData_handlers import router as ld_router



dp = Dispatcher()
storage = MemoryStorage()

dp.include_router(help_r)
dp.include_router(admin_r)
dp.include_router(tarif_r)
dp.include_router(command_r)
dp.include_router(sp_router)
dp.include_router(ld_router)

async def main():
    sheduler = AsyncIOScheduler(timezone="Europe/Moscow")
    sheduler.add_job(check_status, trigger='interval', seconds=3600)
    sheduler.start()
    logging.basicConfig(level=logging.DEBUG)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())

