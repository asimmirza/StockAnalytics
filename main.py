from package.time.check_time import TimeIndia
from package.GCPService import GCPUtility
from package.ParallelProcess.ParallelOption import ParallelProcessing as pp
import time


if __name__ == '__main__':

    flag_mkt_open = True
    temp_time = TimeIndia.getCurrentTime()
    market_close_time = temp_time.replace(hour=15, minute=30, second=0, microsecond=0)
    print(market_close_time)
    while flag_mkt_open:
        ct = TimeIndia.getCurrentTime()
        call_users = GCPUtility.GCPStorage
        users = call_users.readCSV('stock-predictor-bucket',"register_user.csv")
        pp.readUsers(users)

        print("Check Time")
        # Checking the Market Close Time
        if ct >= market_close_time :
            print("Market Closed")
            flag_mkt_open = False
            break
        time.sleep(60)

