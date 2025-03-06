import json

# записываем результат работы программы


def read_parameters_from_json(name_of_file):
    """
    Читает параметры из файла и возвращает словарь dict_of_params
    """
    f = open(name_of_file, 'r')
    dict_of_params = json.load(f)
    f.close()
    return dict_of_params


def write_parameters_to_json(name_of_file, price, balance, income, buy_price, is_order_open):
    """
    Перезаписывает весь json файл params.json
    """
    f = open(name_of_file, 'w')
    data = {"price": price, "balance": balance, "income": income, "buy_price": buy_price, "is_order_open": is_order_open}
    json.dump(data, f, indent=4)
    f.close()


def set_start_time_sys_json(name_of_file, start_t):
    """
    Записывает стартовые параметры в system.json
    """
    f = open(name_of_file, 'w')
    data = {"start_time": start_t, "current_time": start_t, "panic_sell": False}
    json.dump(data, f, indent=4)
    f.close()


def update_current_time(name_of_file, curr_t):
    """
    Обновляет текущее время в system.json
    """
    old_dict = read_parameters_from_json(name_of_file)
    f = open(name_of_file, 'w')
    data = {"start_time": old_dict.get('start_time'), "current_time": curr_t, "panic_sell": old_dict.get('panic_sell')}
    json.dump(data, f, indent=4)
    f.close()


def update_panic_sell_to_sys_json(name_of_file, panic_sell):
    """
    Обновляет паническую продажу в system.json
    """
    old_dict = read_parameters_from_json(name_of_file)
    f = open(name_of_file, 'w')
    data = {"start_time": old_dict.get('start_time'), "current_time": old_dict.get('current_time'), "panic_sell": panic_sell}
    json.dump(data, f, indent=4)
    f.close()


def write_parameters_to_sys_json(name_of_file, start_t, curr_t, panic_sell):
    """
    Перезаписывает все параметры в system.json
    """
    f = open(name_of_file, 'w')
    data = {"start_time": start_t, "current_time": curr_t, "panic_sell": panic_sell}
    json.dump(data, f, indent=4)
    f.close()