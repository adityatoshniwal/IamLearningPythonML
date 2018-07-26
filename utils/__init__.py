from datetime import datetime


def date_to_string(dateObj):
    if dateObj:
        return dateObj.strftime("%Y-%m-%d")
    else:
        return None


def string_end_date(dateStr):
    if dateStr:
        return datetime.strptime(dateStr, "%Y-%m-%d")
    else:
        return None


def date_today():
    return datetime.today()


def date_today_string():
    return date_to_string(datetime.today())


def check_required_args(inp_args, req_args):
    missing = []
    for arg in req_args:
        if arg in inp_args and inp_args[arg] is not None:
            pass
        else:
            missing.append(arg)

    if len(missing) > 0:
        raise ValueError("Arguments " + ", ".join(missing) + " required.")