import pyautogui

canta = 736,938
sepet = 943,623
urun = 849,469
onayla = 1029,607
exit = 1078,419
while True:
    pyautogui.click(canta,interval = 1)
    pyautogui.click(sepet,interval = 1)
    pyautogui.click(urun,interval = 1)
    for i in range(640,1400,69):
        pyautogui.click(i,810,interval = 1)
    hasat = True
    i = 640
    while hasat:
        for b in range(0,12):
            pyautogui.dragTo(849, 469, 2, button='left')
            pyautogui.dragTo(i, 810, 2, button='left')
            pyautogui.click(onayla,interval = 1)
            i += 69
        hasat = False
        pyautogui.click(exit,interval = 1)
