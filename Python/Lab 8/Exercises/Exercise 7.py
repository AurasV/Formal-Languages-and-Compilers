from datetime import datetime


def change_format(date_init):
    date_init = datetime.strptime(date_init, '%y-%m-%d')
    day = date_init.day
    month = date_init.strftime('%B')
    year = date_init.strftime('%y')
    result = f"{day}-{month}-{year}"

    return result


init_date = "03-07-17"
result_date = change_format(init_date)
print(result_date)
