#AUTHOR: S SHABHITH KRISHNA | H4ckr0pZ
import time
from datetime import datetime
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import numpy as np
from os import system
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome()
col = "color 0a"
system("cls")
system(col)
price_history = []
x_org = datetime.timestamp
notShowing = True
tdata = 60
while notShowing:
    url =  "https://www.tradingview.com/dailyfx/widgetembed/?hideideas=1&overrides=%7B%7D&enabled_features=%5B%5D&disabled_features=%5B%5D&locale=en#%7B%22symbol%22%3A%22MEXC%3AHAMUSDT%22%2C%22frameElementId%22%3A%22tradingview_e0c07%22%2C%22interval%22%3A%221M%22%2C%22hide_side_toolbar%22%3A%220%22%2C%22allow_symbol_change%22%3A%221%22%2C%22save_image%22%3A%221%22%2C%22studies%22%3A%22%5B%5D%22%2C%22theme%22%3A%22Light%22%2C%22timezone%22%3A%22exchange%22%2C%22studies_overrides%22%3A%22%7B%7D%22%2C%22utm_source%22%3A%22www.dailyfx.com%22%2C%22utm_medium%22%3A%22widget%22%2C%22utm_campaign%22%3A%22chart%22%2C%22utm_term%22%3A%22MEXC%3AHAMUSDT%22%2C%22page-uri%22%3A%22www.dailyfx.com%2Fcharts%22%7D"
    driver.get(url)
    amt = driver.find_element(By.XPATH,"/html/body/div[2]/div[3]/div/div[1]/div/div[2]/div[1]/div[2]/div/div[2]/div[1]/div/div[2]")
#    print(amt.text[86:92])
    print(f"{amt.text[86:92]} {datetime.now()}")
    p = amt.text[86:91]
    price = float(p)
    price_history.append(price)
    style.use('fivethirtyeight')
    fig = plt.figure()
#    plt.plot(np.array(price_history))
    plt.title(f"HAMSTER {price} @H4CKR0PZ")
    plt.ylabel("Price of HAMSTER")
    plt.plot(price_history,color="green",linewidth = 1)
    plt.draw()
    plt.waitforbuttonpress(timeout=10)
    plt.close(fig)