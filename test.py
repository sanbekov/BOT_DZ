from time import sleep
import asyncio

import aioschedule
from aiogram import types, Dispatcher
from config import bot




# async def download_photo(current_photo):
#     await asyncio.sleep(0.1)
#     print(f"Download photo {current_photo}...")
#
#
# async def main():
#     count = int(input("ENter amount: "))
#     current_photo = 0
#     task_list = []
#
#     while current_photo < count:
#         current_photo += 1
#         # await download_photo(current_photo)
#         task = asyncio.create_task(download_photo(current_photo))
#         task_list.append(task)
#
#     await asyncio.gather(*task_list)
#     print("DOne!")
#
#
# asyncio.run(main())

# async def download_photo(photo_count):
#      while True:
#          photo_count += 1
#          await asyncio.sleep(1)
#          print(f"Photo number {photo_count}...")
#
#
# async def download_video(video_count):
#     while True:
#         video_count += 1
#         await asyncio.sleep(5)
#         print(f"Video number {video_count}...")
#
#
# async def main():
#     photo_count = 0
#     video_count = 0
#     task_list = [
#         download_photo(photo_count),
#         download_video(video_count)
#     ]
#
#     await asyncio.gather(*task_list)
#
# asyncio.run(main())