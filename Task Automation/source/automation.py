import pyautogui
import time
import pandas as pd

# setting a time between pyautogui commands
pyautogui.PAUSE = 0.5

# opening chrome
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

# opening the website link to register the products
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
# waiting a time to ensure that website is open
time.sleep(3)

# logging into the system
pyautogui.press("tab")
pyautogui.write("meuemail@email.com")
pyautogui.press("tab")
pyautogui.write("senha")
pyautogui.click(x=2879, y=573) # position of the login button on my screen

# dealing with a chrome warning
time.sleep(3)
pyautogui.press("enter")

# importing the product database
table = pd.read_csv("Task Automation/source/products.csv")

# registering product data in the system
information = ["codigo","marca","tipo","categoria","preco_unitario","custo","obs"]

for row in table.index:
    # click on the first field text
    pyautogui.click(x=2715, y=294)

    for col in information:
        data = table.loc[row, col]
        
        if not pd.isna(data):
            pyautogui.write(str(data))

        pyautogui.press("tab")
    
    pyautogui.press("enter")
    pyautogui.scroll(-5000)
    time.sleep(0.5)
    pyautogui.scroll(5000)
