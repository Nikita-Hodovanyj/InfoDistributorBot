import aiogram
import asyncio
from aiogram import (Bot, 
                     types, 
                     Dispatcher
)
from aiogram.filters import (Command, 
                             CommandStart
)
import modules

async def main():
    await modules.dispacher.dispatcher.start_polling(modules.api_token)

aiogram._asyncio.run(main())