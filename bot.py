import asyncio
import os
from dotenv import load_dotenv
from handlers import start, about, products, food, clothes, all_products, add_to_cart
from aiogram import Bot, Dispatcher

load_dotenv()
async def main():
    bot = Bot(token=os.getenv("TOKEN"))
    dp = Dispatcher()
    dp.include_routers(start.router, about.router, products.router, food.router, clothes.router, all_products.router,add_to_cart.router)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
