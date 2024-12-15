from datetime import datetime

from sqlalchemy.inspection import inspect


def to_dict(obj):
    return {c.key: getattr(obj, c.key) for c in inspect(obj).mapper.column_attrs}


def get_datetime_now_db_format():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
