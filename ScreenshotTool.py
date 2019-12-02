import pyautogui
import time

# Sleep for 5 seconds
time.sleep(5)

# Range can be changed depending on the number of pages
for i in range(1):
 pyautogui.keyDown('right')
 pyautogui.keyUp('right')
 
 # Take and save a screenshot
 pyautogui.screenshot('images/page_%d.pdf' % i)
 time.sleep(0.05)
