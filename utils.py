def convert_date_to_datetime(dict_data, datetime):
    for i in dict_data:
        i["date"] = datetime.strptime(i["date"], "%Y-%m-%d %H:%M:%S")