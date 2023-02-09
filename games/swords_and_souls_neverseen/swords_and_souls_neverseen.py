# winpip install var_dump pyautogui pywin32 pymem pillow pyscreeze
import base64
import os
import pyautogui as pyautogui
from pymem import Pymem
from var_dump import var_dump
import time
import math
from random import randrange
import ctypes
import PIL
import win32gui
import inspect
import pyscreeze
import sys

pyautogui.FAILSAFE = False
#var_dump(pyautogui.PAUSE, pyautogui.FAILSAFE);exit()
# for dodging/agility training:
# uint32(2178405CAE8): 10 means sleeping.
# uint32(2178405CAE8): 5 means middle-attack incoming
# uint32(2178405CAE8): 7 means low attack OR jump attack incoming...
# NEW ADDRESS
# uint8(2178405CAE4): 1 means low attack incoming
# uint8(2178405CAE4): 3 means jump attack incoming
# uint8(2178405CAE4): 6 means sleeping
# uint8(2178405CAE4): 13 means middle attack incoming
# uint8(211DCB90594)
exe_name = 'Swords & Souls Neverseen.exe'
pm = Pymem('Swords & Souls Neverseen.exe')


def dd(*args, **kwargs):
    source = inspect.getframeinfo(inspect.currentframe().f_back)
    source = source.filename + ":" + str(source.lineno)
    sys.stdout.write("dd: " + source + ":\n");
    var_dump(*args, **kwargs)
    exit()

def practice_agility_v1() -> None:
    # first we initialize, wait for it to become 6
    def getval(): return int.from_bytes(pm.read_bytes(
        0x29AAE8805B4-0x20, 1), byteorder='little', signed=False)
    presleep = 0.6
    postsleep = 0  # .5
    shouldWaitFor6 = True
    lastClick = 0  # 1970
    sleepTimeBetweenClicks = 0.64
    while True:
        timeSinceLastClick = time.time() - lastClick
        sleepTime = (sleepTimeBetweenClicks - timeSinceLastClick)
        if sleepTime > 0:
            if sleepTime > 0.1:
                time.sleep(sleepTime - 0.1)
            continue
        val = getval()
        var_dump(val)
        if shouldWaitFor6 and val != 6:
            continue
        elif val == 6:
            shouldWaitFor6 = False
            continue
        elif val == 1:
            # low attack
            time.sleep(presleep)
            pyautogui.press('up')
            lastClick = time.time()
            time.sleep(postsleep)
            #shouldWaitFor6 = True
        elif val == 3:
            # jump attack
            time.sleep(presleep)
            pyautogui.press(['left', 'right'])
            lastClick = time.time()
            time.sleep(postsleep)
            #shouldWaitFor6 = True
        elif val == 13:
            # middle attack
            time.sleep(presleep)
            pyautogui.press('down')
            lastClick = time.time()
            time.sleep(postsleep)
            #shouldWaitFor6 = True
        elif val == 29:
            # i think this means "plz press right-left"
            # time.sleep(presleep)
            pyautogui.press("right")
            #lastClick = time.time()
            # time.sleep(postsleep)
        elif val == 0 or val == 9:
            # unknown state but known to happen..
            continue
        else:
            raise Exception("Unknown value " + str(val))


def practice_agility_v2() -> None:
    windowPosition = win32gui.GetWindowRect(
        win32gui.FindWindow(None, "Swords & Souls Neverseen"))
    imageCounter = 0
    lastPixel = (0, 0, 0)
    while True:
        imageCounter += 1
        attackDetected = False
        image = PIL.ImageGrab.grab(windowPosition)
        #image.save("screenshots/screenshot" + str(imageCounter) + ".bmp");
        # first check for middle-attack, attacker-on-right
        #pixel = image.getpixel((956, 393))
        middleAttackPixelsRight = ((169, 120, 59), (200, 157, 78), (164, 113, 56),
                                   (106, 125, 50), (105, 126, 49),  (106, 126, 49), (108,129, 50), (109, 130, 51), (110, 132, 52), (188, 144, 71), (197, 154, 76), (166, 117, 57), (181, 135, 67), (200, 158, 78))
        #if pixel in middleAttackPixelsRight:
        pixel = image.getpixel((1032, 394))
        if pixel[0] < 100 and pixel[1] < 100 and pixel[2] < 100:
            attackDetected = True
            var_dump("middle attack from right detected: ", pixel);
            time.sleep(0.2)
            pyautogui.press('down')
            # time.sleep(0.1)
            # continue
        else:
            debug_middle_attack_right = False
            if debug_middle_attack_right:
                if pixel != lastPixel:
                    print("unknown middle attack pixel: " + str(pixel))
                    lastPixel = pixel
        # now check for middle-attack, attacker-on-left
        pixel = image.getpixel((277, 402))
        middleAttackPixelsLeft = ((97, 63, 40), (104, 68, 42), (99, 65, 41), (61, 40, 22), 
        (76, 89, 37),(95, 62, 39), (93, 62, 39), (45, 42, 18), (122, 143, 58),
(109, 129, 51), (104, 68, 43), (98, 64, 41), (95, 62, 40), (69, 46, 27), (63, 72, 31),
(48, 43, 21), (94, 62, 39), (50, 51, 22), (97, 64, 41),(92, 61, 38),(44, 39, 17),
(91, 61, 38), (48, 46, 20), (95, 63, 40), (87, 58, 36), (52, 56, 24),(93, 61, 39),
(86, 57, 36), (86, 57, 36),(54, 59, 25)
        ); #okay so basically if this pixel is brownish, it's a middle attack
        if (pixel[0]  < 100 and pixel[1] < 100 and pixel[2] < 100):
            #var_dump("middle attack from left detected: ", pixel);
            attackDetected = True
            time.sleep(0.2)
            pyautogui.press('down')
            # time.sleep(0.1)
            # continue
        else:
            debug_middle_attack_left = False
            if debug_middle_attack_left:
                if pixel != lastPixel:
                    print(str(time.time()) + ":unknown middle attack pixel left: " + str(pixel))
                    lastPixel = pixel
        # now check for low-attack, attacker-on-right
        pixel = image.getpixel((915, 494))
        lowAttackPixels = ((200, 158, 78), (100, 66, 42),
                           (102, 67, 43), (104, 69, 44), (105, 69, 44))
        if pixel in lowAttackPixels:
            attackDetected = True
            #var_dump("low attack detected", pixel)
            time.sleep(0.1)
            pyautogui.press('up')
            # time.sleep(0.1)
            # continue
        else:
            debug_low_attack = False
            if debug_low_attack:
                if pixel != lastPixel:
                    pass
                    print("Unknown low pixel: " + str(pixel))
                    lastPixel = pixel
        # now check for low-attack, attacker-on-left
        pixel = image.getpixel((265, 496))
        lowAttackPixels = ((0,0,0))
        if pixel[0] < 100 and pixel[1] < 100 and pixel[2] < 100:
            attackDetected = True
            #var_dump("low attack detected", pixel)
            time.sleep(0.1)
            pyautogui.press('up')
            # time.sleep(0.1)
            # continue
        else:
            debug_low_attack = False
            if debug_low_attack:
                if pixel != lastPixel:
                    pass
                    print("Unknown low pixel: " + str(pixel))
                    lastPixel = pixel
        # TODO
        # now check for jump-attack, attacker-on-right
        # this one is particularly tricky..
        #pixel = image.getpixel((0, 0))
        #jumpAttackPixels = ((0,0,0), (0,0,0))
        if (image.getpixel((1015, 477)) == (255, 237, 181)
            or image.getpixel((1044, 432)) == (255, 237, 181)
            or image.getpixel((1053, 412)) == (255, 237, 181)
            or image.getpixel((1057, 397)) == (255, 237, 181)
            or image.getpixel((1064, 365)) == (255, 237, 181)
          ):
            attackDetected = True
            time.sleep(0.1)
            pyautogui.press('left')
            # time.sleep(0.1)
            # continue
        else:
            debug_jump_attack = False
            if debug_jump_attack:
                if pixel != lastPixel:
                    pass
                    print("Unknown jump pixel: " + str(pixel))
                    lastPixel = pixel
        # now check for jump-attack, attacker-on-left
        # this one is particularly tricky..
        if (image.getpixel((326, 502)) == (255, 236, 181)
        or image.getpixel((273, 452)) == (255, 236, 181)
        or image.getpixel((259, 429)) == (255,236,181)
        or image.getpixel((327, 217)) == (255, 237, 181)
        or image.getpixel((316, 496)) == (255, 236, 181)
        or image.getpixel((251, 408)) == (255, 236, 181)
        or image.getpixel((247, 393)) == (255, 236, 181)
        or image.getpixel((245, 386)) == (255, 236, 181)
        or image.getpixel((248, 284)) == (254, 236, 181)
        ):
            attackDetected = True
            time.sleep(0.1)
            pyautogui.press('right')
            # time.sleep(0.1)
            # continue
        else:
            debug_jump_attack = False
            if debug_jump_attack:
                if pixel != lastPixel:
                    pass
                    print("Unknown jump pixel: " + str(pixel))
                    lastPixel = pixel
        # now detect exlamation mark on left
        if image.getpixel((403, 349)) == (0, 0, 0):
            attackDetected = True
            time.sleep(0.01)
            pyautogui.press('left')
            # time.sleep(0.1)
            # continue
        else:
            debug_exclamation = False
            if debug_exclamation:
                if pixel != lastPixel:
                    pass
                    print("Unknown exclamation pixel: " + str(pixel))
                    lastPixel = pixel
        # now detect exlamation mark on right
        if image.getpixel((883, 349)) == (0, 0, 0):
            attackDetected = True
            time.sleep(0.01)
            pyautogui.press('right')
            # time.sleep(0.1)
            # continue
        else:
            debug_exclamation = False
            if debug_exclamation:
                if pixel != lastPixel:
                    pass
                    print("Unknown exclamation pixel: " + str(pixel))
                    lastPixel = pixel
        if not attackDetected:
            pass
            # time.sleep(0.1)


def practice_attack_v1() -> None:
    moves = ["left", "up",  "right"]
    sleeptime = 0.01
    while True:
        pyautogui.press(moves[0])
        time.sleep(sleeptime)
        pyautogui.press(moves[1])
        time.sleep(sleeptime)
        pyautogui.press(moves[2])
        time.sleep(sleeptime)
#        time.sleep(0.1)


def practice_attack_v2() -> None:
    windowPosition = win32gui.GetWindowRect(
        win32gui.FindWindow(None, "Swords & Souls Neverseen"))
    imageCounter = 0
    lastLeftPixelClickTime = 0
    lastUpPixelClickTime = 0
    lastRightPixelClickTime = 0
    minimumTimeBetweenClicks = 0.3
    bestTimeBetweenClicks = math.inf
    worstTimeBetweenClicks = -math.inf
    while True:
        startTime = time.time()
        moves = tuple()
        imageCounter += 1
        imageGrabTime = time.time()
        image = PIL.ImageGrab.grab(windowPosition)
        imageGrabTime = time.time() - imageGrabTime
        #image.save("screenshots/screenshot" + str(imageCounter) + ".png");continue;
        # first do left attack pixel
        timeSinceLastLeftPixelClick = time.time() - lastLeftPixelClickTime
        if timeSinceLastLeftPixelClick > minimumTimeBetweenClicks:
            pixel = image.getpixel((509, 636))
            if(not (pixel[0] == 169 and pixel[1] == 193 and pixel[2] == 129)):
                moves = (*moves, "left")
                #pyautogui.press("left")
                #var_dump("left pixel", pixel)
                lastLeftPixelClickTime = time.time()
                #time.sleep(0.01)
        # now do up attack pixel
        timeSinceLastUpPixelClick = time.time() - lastUpPixelClickTime
        if timeSinceLastUpPixelClick > minimumTimeBetweenClicks:
            pixel1 = image.getpixel((647, 499))
            pixel2 = image.getpixel((647, 507))
            pixel3 = image.getpixel((647, 494))
            pixelFail = None

            if(not (pixel1[0] == 186 and pixel1[1] == 205 and pixel1[2] == 138)):
                pixelFail = 1
            elif(not (pixel2[0] == 177 and pixel2[1] == 195 and pixel2[2] == 91)):
                pixelFail = 2
            elif(not ((pixel3[0] == 152 or pixel3[0] == 151) and pixel3[1] == 180 and pixel3[2] == 78)):
                pixelFail = 3
                #print("pixel3: " + str(pixel3))
            else:
                pass
                #pixelFail = None
            if pixelFail is not None:
                #print("pixelFail: " + str(pixelFail))
                moves = (*moves, "up")
                #pyautogui.press("up")
                #var_dump("up pixel", pixel)
                lastUpPixelClickTime = time.time()
                #time.sleep(0.01)
        # now do right attack pixel
        timeSinceLastRightPixelClick = time.time() - lastRightPixelClickTime
        if timeSinceLastRightPixelClick > minimumTimeBetweenClicks:
            pixel = image.getpixel((786, 636))
            if(not (pixel[0] == 181 and pixel[1] == 201 and pixel[2] == 136)):
                moves = (*moves, "right")
                #pyautogui.press("right")
                #var_dump("right pixel", pixel)
                lastRightPixelClickTime = time.time()
                #time.sleep(0.01)
        iterationTime = time.time() - startTime
        if len(moves) > 0:
            pyautogui.press(keys=moves)
        if iterationTime < bestTimeBetweenClicks:
            bestTimeBetweenClicks = iterationTime
            print("Best time between clicks: " + str(bestTimeBetweenClicks) + " - grab time: " + str(imageGrabTime))
        if iterationTime > worstTimeBetweenClicks:
            worstTimeBetweenClicks = iterationTime
            print("Worst time between clicks: " + str(worstTimeBetweenClicks) + " - grab time: " + str(imageGrabTime))


def practice_ranged_attack() -> None:
    windowPosition = win32gui.GetWindowRect(
        win32gui.FindWindow(None, "Swords & Souls Neverseen"))
    height = windowPosition[3] - windowPosition[1]
    width = windowPosition[2] - windowPosition[0]
    imageCounter = 0
    minimumTimeBetweenClicks = 0.3
    badPixels= ((380, 270), (380, 280),(370, 270), (1040, 230), (370, 280));
    trainingDollBullseye = PIL.Image.open("images/training/distance/training_doll_bullseye.bmp")
    #pyscreeze.locateAll(NeedleImage, HaystackImage, grayscale=False, limit=None, region=None)
    while True:
        attackList = list()
        imageCounter += 1
        image = PIL.ImageGrab.grab(windowPosition)
        locations = pyscreeze.locateAll(trainingDollBullseye, image)
        for location in locations:
            x = location[0] + windowPosition[0]
            y = location[1] + windowPosition[1]
            attackList.append((x, y))
        for x in range(0, width, 20):
            for y in range(0, height, 20):
                if((x, y) in badPixels):
                    continue
                pixel = image.getpixel((x, y))
                isRed = pixel[0] > 200 and pixel[1] < 100 and pixel[2] < 100
                if(isRed):
                    attackList.append((x + windowPosition[0], y + windowPosition[1]))
        if len(attackList) > 0:
            #redPixelPositions.sort(key=lambda x: x[1])
            #redPixelPositions.sort(key=lambda x: x[0])
            for position in attackList:
                pyautogui.click(position[0], position[1])
                time.sleep(0.1)
        #dd(windowPosition, height, width)
        #image.save("screenshots/screenshot" + str(imageCounter) + ".bmp");continue;
        # first do left attack pixel



# practice_agility_v1();
practice_attack_v2();
#practice_agility_v2()
#practice_ranged_attack()
exit(0)


imagepath = "images\\training\\attack\\apple_right.bmp"
image = file_get_contents(imagepath)
var_dump(
    image
    #   gui.locateOnScreen("images\\training\\attack\\apple_right.bmp", grayscale=True),f(),
)
