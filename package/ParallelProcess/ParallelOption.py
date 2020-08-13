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
        # Creating Object and Teamp Varaible
        call_stocks = GCPUtility.GCPStorage
        tw = TwilioUtility.TwilioProcess
        ws = WebScrap.WebScrap
        stock_updated_list = []
        Call_Flag = 0
        
        # Fetching Stock List from Google Storage
        stock_list = call_stocks.readCSV('stock-predictor-bucket',filename)
        
        for sl in stock_list:
            
            #Extracting current Price from Website
            fv = ws.getQuote(sl[1])
            msg = "Current Rate of " + str(sl[0]) + " is " + str(fv)
            # print(msg)
            stop_loss = float(sl[2])
            target = float(sl[3])
            
            #Check for Stop losss and Target Achieved
            if stop_loss >= fv:
                msg = "Alert ! Stop Loss for " + str(sl[0]) + " is " + str(fv)
                if sl[4] == 0:
                    Call_Flag = 1
                    tw.SendMessage(msg,phone_dtl)
                sl[4]=1
            elif target <= fv:                
                msg = "Alert ! Target Achieved for " + str(sl[0]) + " is " + str(fv)
                if sl[5] == 0:
                    tw.SendMessage(msg, phone_dtl)
                sl[5] = 1
            stock_updated_list.append(sl)
#         print(stock_updated_list)
        # Updating the stock list details in Google Cloud 
        call_stocks.writeCSV('stock-predictor-bucket',filename,stock_updated_list)
        if Call_Flag == 1:
            tw.CallUser(phone_dtl)




# call_users = GCPUtility.GCPStorage
# users = call_users.readCSV('stock-predictor-bucket',"register_user.csv")
# p=ParallelProcessing
# p.readUsers(users)
