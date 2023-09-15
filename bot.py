# bot.py => first attempt

import os
from twitchio.ext import commands
from yeelight import Bulb
import time
import pyttsx3
import numpy as np
import pyautogui
from threading import Thread
from colorsys import rgb_to_hsv, hsv_to_rgb

floor_bulb = Bulb("192.168.1.20")
desk_bulb = Bulb("192.168.1.65")

# create a dict of lights
lights = {
    "floor": floor_bulb,
    "desk": desk_bulb
}

floor_bulb.turn_on()
desk_bulb.turn_on()

floor_bulb.set_brightness(100)
desk_bulb.set_brightness(100)

turnoverbackground = True

engine = pyttsx3.init()


class Bot(commands.Bot):
    
    def __init__(self):
        super().__init__(token=os.environ['ACCESS_TOKEN'], prefix=os.environ['BOT_PREFIX'], initial_channels=[os.environ['CHANNEL']])

    async def event_ready(self):
        'Called once when the bot goes online.'
        print(f"{os.environ['BOT_NICK']} is online!")
        engine.say("Hello, I am online and ready to go!")
        engine.runAndWait()

    @commands.command(name='pink')
    async def pink(self, ctx: commands.Context):
        turnoverbackground = False
        for light in lights:
            lights[light].turn_on()
            lights[light].set_brightness(100)
            lights[light].set_rgb(255, 153, 204)
        time.sleep(10)
        turnoverbackground = True

    @commands.command(name='white')
    async def white(self, ctx: commands.Context):
        turnoverbackground = False
        # turn white all the lights
        for light in lights:
            lights[light].turn_on()
            lights[light].set_brightness(100)
            lights[light].set_color_temp(3500)
        time.sleep(10)
        turnoverbackground = True

    @commands.command(name='orange')
    async def orange(self, ctx: commands.Context):
        turnoverbackground = False # for 10 seconds
        for light in lights:
            lights[light].turn_on()
            lights[light].set_brightness(100)
            lights[light].set_rgb(240, 99, 0)
        time.sleep(10)
        turnoverbackground = True

    @commands.command(name='green')
    async def green(self, ctx: commands.Context):
        turnoverbackground = False # for 10 seconds
        for light in lights:
            lights[light].turn_on()
            lights[light].set_brightness(100)
            lights[light].set_rgb(0, 255, 0)
        time.sleep(10)
        turnoverbackground = True

    @commands.command(name='blue')
    async def blue(self, ctx: commands.Context):
        turnoverbackground = False # for 10 seconds
        for light in lights:
            lights[light].turn_on()
            lights[light].set_brightness(100)
            lights[light].set_rgb(0, 0, 255)
        time.sleep(10)
        turnoverbackground = True

    @commands.command(name='red')
    async def red(self, ctx: commands.Context):
        turnoverbackground = False # for 10 seconds
        for light in lights:
            lights[light].turn_on()
            lights[light].set_brightness(100)
            lights[light].set_rgb(255, 0, 0)
        time.sleep(10)
        turnoverbackground = True

    @commands.command(name='off')
    async def black(self, ctx: commands.Context):
        turnoverbackground = False # for 10 seconds
        for light in lights:
            lights[light].turn_off()
        time.sleep(10)
        turnoverbackground = True
        


    @commands.command(name='rgb')
    async def rgb(self, ctx: commands.Context, r: int, g: int, b: int):
        turnoverbackground = False
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
        for light in lights:
            lights[light].turn_on()
            lights[light].set_brightness(100)
            lights[light].set_rgb(r, g, b)
        time.sleep(10)
        turnoverbackground = True

    @commands.command(name='hex')
    async def rgbHex(self, ctx: commands.Context, hex: str):
        turnoverbackground = False # for 10 seconds
        # check if 3 or 6 digits
        if (len(hex) == 3):
            hex = hex[0] + hex[0] + hex[1] + hex[1] + hex[2] + hex[2]
        
        # convert hex to rgb
        hex = hex.lstrip('#')
        r = int(hex[0:2], 16)
        g = int(hex[2:4], 16)
        b = int(hex[4:6], 16)
        for light in lights:
            lights[light].turn_on()
            lights[light].set_brightness(100)
            lights[light].set_rgb(r, g, b)
        time.sleep(10)
        turnoverbackground = True

    @commands.command(name='blink')
    async def blink(self, ctx: commands.Context):
        # await ctx.send('blink')
        turnoverbackground = False 
        
        # identify half of the lights
        tmplights = list(lights.values())
        for i in range(0, len(tmplights)):
            if (i % 2 == 0):
                tmplights[i].turn_on()
                tmplights[i].set_brightness(100)
                tmplights[i].set_color_temp(3500)
            else:
                tmplights[i].set_brightness(100)
                tmplights[i].set_color_temp(3500)
                tmplights[i].turn_off()


        for i in range(0, 10):
            for light in lights:
                lights[light].toggle(effect="sudden")
            time.sleep(0.5)
        
        for light in lights:
            lights[light].turn_on()
        turnoverbackground = True
    
    @commands.command(name='say')
    async def say(self, ctx: commands.Context, say: str):
        engine.say(say)
        engine.runAndWait()

    # for every light in the dict of lights register a command with the name of the light and make it can be turned on or off blink or set to a color

    # create a command relative to the lights dict
    @commands.command(name='light')
    async def light(self, ctx: commands.Context, light: str, state: str):
        turnoverbackground = False # for 10 seconds
        # check if the light is in the dict
        if (light in lights):
            if (state == "on"):
                lights[light].turn_on()
            elif (state == "off"):
                lights[light].turn_off()
            elif (state == "blink"):
                for i in range(0, 10):
                    lights[light].toggle(effect="sudden")
                    time.sleep(0.5)
                lights[light].turn_on()
            elif (state == "white"):
                lights[light].turn_on()
                lights[light].set_brightness(100)
                lights[light].set_color_temp(3500)
            elif (state == "red"):
                lights[light].turn_on()
                lights[light].set_brightness(100)
                lights[light].set_rgb(255, 0, 0)
            elif (state == "green"):
                lights[light].turn_on()
                lights[light].set_brightness(100)
                lights[light].set_rgb(0, 255, 0)
            elif (state == "blue"):
                lights[light].turn_on()
                lights[light].set_brightness(100)
                lights[light].set_rgb(0, 0, 255)
            elif (state == "orange"):
                lights[light].turn_on()
                lights[light].set_brightness(100)
                lights[light].set_rgb(240, 99, 0)
            elif (state == "pink"):
                lights[light].turn_on()
                lights[light].set_brightness(100)
                lights[light].set_rgb(255, 153, 204)
            elif (state[0]=='#'):
                # check if 3 or 6 digits
                if (len(state) == 4):
                    state = state[0] + state[0] + state[1] + state[1] + state[2] + state[2]
                
                # convert hex to rgb
                state = state.lstrip('#')
                r = int(state[0:2], 16)
                g = int(state[2:4], 16)
                b = int(state[4:6], 16)
                lights[light].turn_on()
                lights[light].set_brightness(100)
                lights[light].set_rgb(r, g, b)
            else:
                await ctx.send("Invalid state")
        else:
            await ctx.send("Invalid light")
        time.sleep(10)
        turnoverbackground = True

def bg_color():
    last = np.array([0, 0, 0])
    current = np.array([0, 0, 0])
    # loop forever
    while True:
        if (turnoverbackground):
            # get the image of the screen
            image = pyautogui.screenshot()
            # transform the image into a numpy array
            image = np.array(image)
            # get the mean value rgb of the image without pixel under 50 brightness
            tmp = np.mean(image[image[:,:,0] > 50], axis=0)
            # print(f"float rgb({tmp})")
            # if the average conatains nan values skip this iteration
            if (np.isnan(tmp).any() == False):
                # convert tmp to int
                current = np.array(tmp, dtype=int)
                # convert current to regular int
                # check if current is too different from last
                if (np.linalg.norm(current - last) > 12):
                    print(np.linalg.norm(current - last))
                    current = current.tolist()
                    # set the lights to the average color
                    try:
                        print(f"current rgb({current[0]}, {current[1]}, {current[2]})")
                        lights["floor"].turn_on()
                        lights["floor"].set_brightness(100)
                        lights["floor"].set_rgb(current[0], current[1], current[2])
                        
                        complement = complementary(current[0], current[1], current[2])
                        
                        print(f"complement rgb({complement})\n")
                        lights["desk"].turn_on()
                        lights["desk"].set_brightness(100)
                        lights["desk"].set_rgb(complement[0], complement[1], complement[2])
                        last = current
                    except Exception as e:
                        print(e)
                        # if error try to look for 'client quota exceeded'
                        if (str(e).find("client quota exceeded") != -1):
                            # try to reconnect to the bulbs
                            reconnect()
                        pass
                    
                # sleep for 1 second
        time.sleep(0.5)

def complementary(r, g, b):
    substract = 255 - np.array([r, g, b])
    # every value % 255
    substract = substract % 255
    # print the substract
    print(f"substract rgb({substract})")

    # return the rgb
    return substract.tolist()

def get_complementary(color):
    # strip the # from the beginning
    color = color[1:]

    # convert the string into hex
    color = int(color, 16)

    # invert the three bytes
    # as good as substracting each of RGB component by 255(FF)
    comp_color = 0xFFFFFF ^ color

    # convert the color back to hex by prefixing a #
    comp_color = "#%06X" % comp_color

    # return the result
    return comp_color

def rgb_to_hex(r, g, b):
    return '#%02x%02x%02x' % (r, g, b)

def hex_to_rgb(hex):
    hex = hex.lstrip('#')
    tmp = tuple(int(hex[i:i+2], 16) for i in (0, 2, 4))
    return np.array(tmp).tolist()


def reconnect():
    turnoverbackground = False
    
    # remove the bulbs from the dict
    lights.clear()
    print("reconnecting")
    floor_bulb = Bulb("192.168.1.20")
    desk_bulb = Bulb("192.168.1.65")

    lights["floor"] = floor_bulb
    lights["desk"] = desk_bulb
    
    turnoverbackground = True

if __name__ == "__main__":
    # create a thread to run pyautogui
    thread = Thread(target=bg_color)
    # start the thread
    thread.start()
    # run the bot
    bot = Bot()
    bot.run()

