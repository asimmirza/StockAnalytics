from package.time.check_time import TimeIndia
from package.GCPService import GCPUtility
from package.ParallelProcess.ParallelOption import ParallelProcessing as pp
import time


if __name__ == '__main__':

    flag_mkt_open = True
    while flag_mkt_open:
        ct = TimeIndia.getCurrentTime()
        call_users = GCPUtility.GCPStorage
        users = call_users.readCSV('stock-predictor-bucket',"register_user.csv")
        pp.readUsers(users)


        # Checking the Market Close Time
        if ct.hour>=15 and ct.minute >=30 :
            print("Market Closed")
            flag_mkt_open = False

        time.sleep(300)

