from package.time.check_time import TimeIndia

if __name__ == '__main__':

    flag_mkt_open = True
    while flag_mkt_open:
        ct = TimeIndia.getCurrentTime()

        if ct.hour>=15 and ct.minute >=30 :
            print("Market Closing")
            flag_mkt_open = False

