from datetime import datetime, timedelta

def get_date_list(from_date: str, to_date: str) -> list[str]:
    date_format = "%Y-%m-%d"
    start_date = datetime.strptime(from_date, date_format)
    end_date = datetime.strptime(to_date, date_format)

    if start_date <= end_date:
        delta = timedelta(days=1)
        date_list = []
        current_date = start_date
        while current_date <= end_date:
            date_list.append(current_date.strftime(date_format))
            current_date += delta
        return date_list
    else:
        delta = timedelta(days=-1)
        date_list = []
        current_date = start_date
        while current_date >= end_date:
            date_list.append(current_date.strftime(date_format))
            current_date += delta
        return date_list

print(get_date_list("2023-04-08", "2023-06-06"))
print(get_date_list("2023-06-06", "2023-06-06"))