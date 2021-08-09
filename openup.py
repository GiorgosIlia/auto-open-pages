import pyautogui,time ,webbrowser
sites = ['youtube.com','facebook.com' ]
time.sleep(1)
#pyautogui.click(483,1062)

webbrowser.open('http://www.google.com')
time.sleep(1)


for i in range (0, len(sites)) :
    pyautogui.hotkey('ctrl' , 'l')
    pyautogui.typewrite(sites[i])
    pyautogui.press('enter')
    pyautogui.hotkey('ctrl', 't' )
    
pyautogui.typewrite(' ')
