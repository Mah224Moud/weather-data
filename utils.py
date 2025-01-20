def convert_date_to_datetime(dict_data, datetime):
    """
    Convert the date column of a list of dictionaries to datetime format.

    Parameters:
    dict_data (list): a list of dictionaries containing a "date" key
    datetime (module): the datetime module

    Returns:
    None
    """
    for i in dict_data:
        i["date"] = datetime.strptime(i["date"], "%Y-%m-%d %H:%M:%S")