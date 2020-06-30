from yahoo_fin import stock_info as si
from datetime import datetime
from pytz import timezone
import psycopg2


def stock_time_vals(tz='America/New_York', ticker='SPY'):
    spy_price = si.get_live_price(ticker)
    ny_tz = timezone(tz)
    ny_time = datetime.now(ny_tz)
    return (spy_price, ny_time)



def intervals_data_insert(stock_time):
    try:
        conn = psycopg2.connect(user="",
                                       password="",
                                       host="",
                                       port="",
                                       database="")
        cursor = conn.cursor()
        query = """INSERT INTO stock_test (price, time_stamp) VALUES (%s, %s)"""
        cursor.execute(query, stock_time)
        conn.commit()  # <- We MUST commit to reflect the inserted data
        cursor.close()
        conn.close()
    except (Exception, psycopg2.Error) as error:
        print(error)


intervals_data_insert(stock_time_vals())
