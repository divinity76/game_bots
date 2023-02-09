# automates level-grinding in "swords and sandals 2" Taunt/Charisma builds
import pyautogui as pyautogui
from var_dump import var_dump
import time
import PIL
import win32gui
import inspect
import pyscreeze
import sys


pyautogui.FAILSAFE = False


def dd(*args, **kwargs):
    source = inspect.getframeinfo(inspect.currentframe().f_back)
    source = source.filename + ":" + str(source.lineno)
    sys.stdout.write("dd: " + source + ":\n")
    var_dump(*args, **kwargs)
    exit()


def autoplay():
    windowPosition = win32gui.GetWindowRect(
        win32gui.FindWindow(None, "Swords and Sandals Classic Collection"))
    currentMouseX, currentMouseY = pyautogui.position()
    if currentMouseX >= windowPosition[0] and currentMouseX <= windowPosition[2] and currentMouseY >= windowPosition[1] and currentMouseY <= windowPosition[3]:
        pyautogui.moveTo(0, 0)
        pass
    currentImage = PIL.ImageGrab.grab(windowPosition)
    teleportIfTooCloseToEnemy = True
    if teleportIfTooCloseToEnemy:
        pushAwayFromEnemyImages = (
            PIL.Image.open("images/push_away_from_enemy1.bmp"),
            PIL.Image.open("images/push_away_from_enemy2.bmp"),
        )
        for pushAwayFromEnemyImage in pushAwayFromEnemyImages:
            pushAwayPosition = pyscreeze.locate(
                pushAwayFromEnemyImage, currentImage)
            if pushAwayPosition != None:
                teleportImage = PIL.Image.open("images/teleport.bmp")
                teleportPosition = pyscreeze.locate(
                    teleportImage, currentImage)
                if teleportPosition != None:
                    x, y = pyautogui.center(teleportPosition)
                    x = x + windowPosition[0]
                    y = y + windowPosition[1]
                    pyautogui.click(x=x, y=y, button='left')
                    pyautogui.click(x=x, y=y, button='left')
                    pass
                pass
            pass
        pass
    pressOnShoutAttack = True
    if pressOnShoutAttack:
        shoutAttackImages = (
            PIL.Image.open("images/shouting_attack1.bmp"),
            PIL.Image.open("images/shouting_attack2.bmp"),
            PIL.Image.open("images/shouting_attack3.bmp"),
            PIL.Image.open("images/shouting_attack4.bmp"),
            PIL.Image.open("images/shouting_attack5.bmp"),
            PIL.Image.open("images/shouting_attack6.bmp"),
            PIL.Image.open("images/shouting_attack7.bmp"),
            PIL.Image.open("images/shouting_attack8.bmp"),
            PIL.Image.open("images/shouting_attack9.bmp"),
            PIL.Image.open("images/shouting_attack10.bmp"),
            PIL.Image.open("images/shouting_attack11.bmp"),
            PIL.Image.open("images/shouting_attack12.bmp"),
            PIL.Image.open("images/shouting_attack13.bmp"),
            PIL.Image.open("images/shouting_attack14.bmp"),
            PIL.Image.open("images/shouting_attack15.bmp"),
            PIL.Image.open("images/shouting_attack16.bmp"),
            PIL.Image.open("images/shouting_attack17.bmp"),
            PIL.Image.open("images/shouting_attack18.bmp"),
            PIL.Image.open("images/shouting_attack19.bmp"),
            PIL.Image.open("images/shouting_attack20.bmp"),
        )
        for shoutAttackImage in shoutAttackImages:
            ShoutAttackPosition = pyscreeze.locate(
                shoutAttackImage, currentImage)
            if ShoutAttackPosition != None:
                x, y = pyautogui.center(ShoutAttackPosition)
                x = x + windowPosition[0]
                y = y + windowPosition[1]
                pyautogui.click(x=x, y=y, button='left')
                pyautogui.click(x=x, y=y, button='left')
                pass
            pass
        pass
    pass
    pressOnVictoryNextButton = True
    if pressOnVictoryNextButton:
        victoryNextButtonImage = PIL.Image.open(
            "images/victory_next_button.bmp")
        victoryNextButtonPosition = pyscreeze.locate(
            victoryNextButtonImage, currentImage)
        if victoryNextButtonPosition != None:
            x, y = pyautogui.center(victoryNextButtonPosition)
            x = x + windowPosition[0]
            y = y + windowPosition[1]
            pyautogui.click(x=x, y=y, button='left')
            pyautogui.click(x=x, y=y, button='left')
            pass
        pass
    pass
    pressOnArenaButton = True
    if pressOnArenaButton:
        arenaButtonImage = PIL.Image.open("images/arena_button.bmp")
        arenaButtonPosition = pyscreeze.locate(arenaButtonImage, currentImage)
        if arenaButtonPosition != None:
            x, y = pyautogui.center(arenaButtonPosition)
            x = x + windowPosition[0]
            y = y + windowPosition[1]
            pyautogui.click(x=x, y=y, button='left')
            pyautogui.click(x=x, y=y, button='left')
            pass
        pass
    pass
    pressOnDuelButton = True
    if pressOnDuelButton:
        duelButtonImage = PIL.Image.open("images/duel_button.bmp")
        duelButtonPosition = pyscreeze.locate(duelButtonImage, currentImage)
        if duelButtonPosition != None:
            x, y = pyautogui.center(duelButtonPosition)
            x = x + windowPosition[0]
            y = y + windowPosition[1]
            pyautogui.click(x=x, y=y, button='left')
            pyautogui.click(x=x, y=y, button='left')
            pass
        pass
    pass
    pressOnAcceptNextVsButton = True
    if pressOnAcceptNextVsButton:
        acceptNextVsButtonImage = PIL.Image.open(
            "images/accept_next_vs_button.bmp")
        acceptNextVsButtonPosition = pyscreeze.locate(
            acceptNextVsButtonImage, currentImage)
        if acceptNextVsButtonPosition != None:
            x, y = pyautogui.center(acceptNextVsButtonPosition)
            x = x + windowPosition[0]
            y = y + windowPosition[1]
            pyautogui.click(x=x, y=y, button='left')
            pyautogui.click(x=x, y=y, button='left')
            pass
        pass
    pass


while True:
    # break
    autoplay()
    time.sleep(0.1)
