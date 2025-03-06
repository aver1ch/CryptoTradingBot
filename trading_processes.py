from get_price import get_price
import indicators
import io_json

from datetime import datetime
import time

#разбиениие капитала

def dual_sma_trading(driver, curl, balance, income, is_order_open, buy_price):
    sma_300 = []
    sma_900 = []

    commission = 0.0003

    potential_income = 0

    if not is_order_open:
        buy_price = 0

    while True:
        price = float(get_price(driver, curl))

        sma_300, sma300 = indicators.sma_by_user_timeframe(sma_300, price, 300)
        sma_900, sma900 = indicators.sma_by_user_timeframe(sma_900, price, 900)

        current_time = time.time()
        io_json.update_current_time("system.json", current_time)
        io_json.write_parameters_to_json("params.json", price, balance, income, buy_price, is_order_open)

        # условие начала торгов
        if len(sma_900) == 900 and len(sma_300) == 300:
            # условие покупки
            if not is_order_open and sma300 > sma900:
                buy_price = price
                balance -= balance * commission
                is_order_open = True
                io_json.write_parameters_to_json("params.json", price, balance, income, buy_price, is_order_open)
                print(" ".join(map(str, ['buy', str(round(price, 2)), str(round(sma300, 2)), str(round(sma900, 2)), str(round(balance, 2)), str(round(income, 2)), str(datetime.now().date()), str(datetime.now().time()), '\n'])))

            # условие продажи
            if is_order_open and (((balance * commission + (potential_income * commission)) < potential_income)): # sma300 < sma900 or
                is_order_open = False
                income = balance * ((price / buy_price) - 1)
                balance += income - (income * commission)
                io_json.write_parameters_to_json("params.json", price, balance, income, buy_price, is_order_open)
                print(" ".join(map(str, ['sell', str(round(price, 2)), str(round(sma300, 2)), str(round(sma900, 2)), str(round(balance, 2)), str(round(income, 2)), str(datetime.now().date()), str(datetime.now().time()), '\n'])))
        
        if(is_order_open == True):
            potential_income = balance * ((price / buy_price) - 1)
