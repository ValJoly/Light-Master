# bot.py => first attempt

import os
from twitchio.ext import commands
from yeelight import Bulb
import time
import pyttsx3

bulb = Bulb("192.168.1.21")

engine = pyttsx3.init()


class Bot(commands.Bot):
    
    def __init__(self):
        super().__init__(token=os.environ['ACCESS_TOKEN'], prefix=os.environ['BOT_PREFIX'], initial_channels=[os.environ['CHANNEL']])

    async def event_ready(self):
        'Called once when the bot goes online.'
        print(f"{os.environ['BOT_NICK']} is online!")


    @commands.command(name='pink')
    async def pink(self, ctx: commands.Context):
        bulb.turn_on()
        bulb.set_brightness(100)
        bulb.set_rgb(255, 153, 204)
        print(type(ctx))

    @commands.command(name='white')
    async def white(self, ctx: commands.Context):
        bulb.turn_on()
        bulb.set_brightness(100)
        bulb.set_color_temp(3500)

    @commands.command(name='orange')
    async def orange(self, ctx: commands.Context):
        bulb.turn_on()
        bulb.set_brightness(100)
        bulb.set_rgb(240, 99, 0)

    @commands.command(name='green')
    async def green(self, ctx: commands.Context):
        bulb.turn_on()
        bulb.set_brightness(100)
        bulb.set_rgb(0, 255, 0)

    @commands.command(name='blue')
    async def blue(self, ctx: commands.Context):
        bulb.turn_on()
        bulb.set_brightness(100)
        bulb.set_rgb(0, 0, 255)

    @commands.command(name='red')
    async def red(self, ctx: commands.Context):
        bulb.turn_on()
        bulb.set_brightness(100)
        bulb.set_rgb(255, 0, 0)

    @commands.command(name='black')
    async def black(self, ctx: commands.Context):
        bulb.turn_off()
        # blink(bulb)



    @commands.command(name='rgb')
    async def rgb(self, ctx: commands.Context, r: int, g: int, b: int):
        if (r > 255):
            r = 255
        elif (r < 0):
            r = 0
        if (g > 255):
            g = 255
        elif (g < 0):
            g = 0
        if (b > 255):
            b = 255
        elif (b < 0):
            b = 0
        bulb.set_brightness(100)
        bulb.set_rgb(r, g, b)

    @commands.command(name='rgbHex')
    async def rgbHex(self, ctx: commands.Context, hex: str):
        # convert hex to rgb
        r = int(hex[0:2], 16)
        g = int(hex[2:4], 16)
        b = int(hex[4:6], 16)
        bulb.turn_on()
        bulb.set_brightness(100)
        bulb.set_rgb(r, g, b)

    @commands.command(name='blink')
    async def blink(self, ctx: commands.Context):
        # await ctx.send('blink')
        bulb.turn_on()
        for i in range(0, 10):
            bulb.toggle(effect="sudden")
            time.sleep(0.5)
        bulb.turn_on()
    
    @commands.command(name='say')
    async def say(self, ctx: commands.Context, say: str):
        engine.say(say)
        engine.runAndWait()



if __name__ == "__main__":
    bot = Bot()
    bot.run()

