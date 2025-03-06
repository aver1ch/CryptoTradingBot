import trading_processes
import io_json

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

import time

curl = "https://ru.tradingview.com/chart/?symbol=BINANCE%3ABTCUSDT"
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

dict_of_params = io_json.read_parameters_from_json("params.json")

balance = dict_of_params.get('balance')
income = dict_of_params.get('income')
is_order_open = dict_of_params.get('is_order_open')
buy_price = dict_of_params.get('buy_price')

#
start_time = time.time()
io_json.set_start_time_sys_json("system.json", start_time)
#
try:
    trading_processes.dual_sma_trading(driver, curl, balance, income, is_order_open, buy_price)
except Exception as error:
    print("Error")
    trading_processes.dual_sma_trading(driver, curl, balance, income, is_order_open, buy_price)

driver.quit()