from twilio.rest import Client as Call
import time
class TwilioProcess:
    def CallUser(ph_number):
        while True:
            try:
                client = Call("<>","<>")
                From_number = "<>"
                To_number = "+91"+str(ph_number)
                Src_path = "http://demo.twilio.com/docs/voice.xml"
                print("Call Intiated")
                client.calls.create(to=To_number,from_=From_number,url= Src_path,method = 'GET')
            except:
                print("Call - Resource Busy")
                time.sleep(30)
                continue
            else:
                print("Call Completed")
                break
            finally:
                pass
    def SendMessage(msg,ph_number):
        while True:
            try:
                print("Message Intiated")
                client = Call("ACe6debefea0793a37c388b807abd01a9f","db372182e8ac8ec648196583c8c1d209")
                From_number = "+18316121429"
                To_number = "+91"+str(ph_number)
                client.messages.create(to=To_number,from_=From_number,body=str(msg))
            except:
                print("Message -Resource Busy")
                time.sleep(30)
                continue
            else:
                break
            finally:
                print("Message Sent Completed")
