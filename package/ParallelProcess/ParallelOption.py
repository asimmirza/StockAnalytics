import multiprocessing
from package.GCPService import GCPUtility
from package.WebScrapping import WebScrap
from package.Communication import TwilioUtility


class ParallelProcessing:
    def readUsers(userlist):
        for row in userlist:
            file_name = row[3]
            phone_dtl = row[2]
            p = multiprocessing.Process(target=ParallelProcessing.readStockFile,args=[file_name,phone_dtl])
            p.start()


    def readStockFile(filename,phone_dtl):
        # print(filename)
        # print(phone_dtl)
        call_stocks = GCPUtility.GCPStorage
        tw = TwilioUtility.TwilioProcess
        stock_list = call_stocks.readCSV('stock-predictor-bucket',filename)
        ws = WebScrap.WebScrap
        stock_updated_list = []
        # print(stock_list)
        for sl in stock_list:
            # print(sl[1])
            fv = ws.getQuote(sl[1])
            msg = "Current Rate of " + str(sl[0]) + " is " + str(fv)
            # print(msg)
            stop_loss = float(sl[2])
            target = float(sl[3])
            if stop_loss >= fv:
                msg = "Alert ! Stop Loss for " + str(sl[0]) + " is " + str(fv)
                sl[4]=1
                tw.CallUser(phone_dtl)
                tw.SendMessage(msg,phone_dtl)
            elif target <= fv:
                sl[5] = 1
                msg = "Alert ! Target Achieved for " + str(sl[0]) + " is " + str(fv)
                tw.SendMessage(msg, phone_dtl)
            stock_updated_list.append(sl)
        print(stock_updated_list)
        call_stocks.writeCSV('stock-predictor-bucket',filename,stock_updated_list)




# call_users = GCPUtility.GCPStorage
# users = call_users.readCSV('stock-predictor-bucket',"register_user.csv")
# p=ParallelProcessing
# p.readUsers(users)