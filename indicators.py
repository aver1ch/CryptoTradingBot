def calculate_avg(curr_list):
    return sum(curr_list)/len(curr_list)

def sma_by_user_timeframe(list_of_avg, new_price, nmax_len):

    max_len = nmax_len

    if len(list_of_avg) < max_len:
        list_of_avg.append(new_price)
    elif len(list_of_avg) == max_len:
        list_of_avg = list_of_avg[1:]
        list_of_avg.append(new_price)
    else:
        list_of_avg = list_of_avg[len(list_of_avg) - max_len + 1:]
        list_of_avg.append(new_price)

    return list_of_avg, calculate_avg(list_of_avg)

def split_balance(balance, max_amount_of_orders):

    balance /= max_amount_of_orders

    dict_of_money = []

    for i in range(max_amount_of_orders - 1):
        dict_of_money.append(balance)

    return dict_of_money