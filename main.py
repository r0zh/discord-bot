import asyncio
async def chek_stop(message):
    if message == 'para perra':
        print("vale")
        

async def on_message(message):
    if message == "nuke":
      for i in range(100):
        task = asyncio.create_task(chek_stop(message))
        print('xd\n')
        await asyncio.sleep(0.1)


asyncio.run(on_message(input()))