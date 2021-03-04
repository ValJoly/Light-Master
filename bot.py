# bot.py => first attempt

import os
from twitchio.ext import commands
from twitchio.webhook import UserFollows
from yeelight import Bulb
import time

bot = commands.Bot(
    # set up the bot
    irc_token=os.environ['TMI_TOKEN'],
    client_id=os.environ['CLIENT_ID'],
    nick=os.environ['BOT_NICK'],
    prefix=os.environ['BOT_PREFIX'],
    initial_channels=[os.environ['CHANNEL']]
)
newFollower = UserFollows(to_id=55422605)
bulb = Bulb("192.168.0.15")
deskLampe = Bulb("192.168.0.25")


@bot.event
async def event_ready():
    'Called once when the bot goes online.'
    print(f"{os.environ['BOT_NICK']} is online!")
    ws = bot._ws  # this is only needed to send messages within event_ready
    await ws.send_privmsg(os.environ['CHANNEL'], f"/me has landed!")

@bot.command(name='pink')
async def pink(ctx):
    bulb.turn_on()
    bulb.set_brightness(100)
    bulb.set_rgb(255, 153, 204)
    print(type(ctx))

@bot.command(name='white')
async def white(ctx):
    bulb.turn_on()
    bulb.set_brightness(100)
    bulb.set_color_temp(3500)

@bot.command(name='orange')
async def orange(ctx):
    bulb.turn_on()
    bulb.set_brightness(100)
    bulb.set_rgb(240, 99, 0)

@bot.command(name='green')
async def green(ctx):
    bulb.turn_on()
    bulb.set_brightness(100)
    bulb.set_rgb(0, 255, 0)

@bot.command(name='blue')
async def blue(ctx):
    bulb.turn_on()
    bulb.set_brightness(100)
    bulb.set_rgb(0, 0, 255)

@bot.command(name='red')
async def red(ctx):
    bulb.turn_on()
    bulb.set_brightness(100)
    bulb.set_rgb(255, 0, 0)

@bot.command(name='black')
async def black(ctx):
    # bulb.turn_off()
    blink(bulb)



@bot.command(name='rgb')
async def rgb(ctx, r: int, g: int, b: int):
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

def blink(blb: Bulb):
    # bulb.turn_on()
    for i in range(0, 10):
        blb.toggle(effect="sudden")
        time.sleep(0.7)
    bulb.turn_on()

if __name__ == "__main__":
    bot.run()

