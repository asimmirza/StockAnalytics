from google.cloud import storage
import csv
import os

class GCPStorage:
    def readCSV(Bucket_Name,FileName):
        #Authenticating to GCP
        storage_client = storage.Client.from_service_account_json('package/GCPService/clear-region-285807-dc6770a9ef87.json')
        bucket = storage_client.get_bucket(Bucket_Name)

        # Download the file from Google Cloud
        blop = bucket.blob(FileName)
        data = blop.download_as_string().decode("utf-8")

        # Spliting Data
        read_row = data.replace(u'\ufeff', '')
        read_row = read_row.replace(u'\r', '')
        read_row = read_row.split('\n')
        file_content = []
        for row in read_row:
            column = []
            if row != '':
                read_column = row.split(",")
                for col in read_column:
                    column.append(col)
                file_content.append(column)
        return file_content

    def writeCSV(Bucket_Name,filename,data):
        with open(filename, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(data)
            print("New File Created")
        storage_client = storage.Client.from_service_account_json('package/GCPService/clear-region-285807-dc6770a9ef87.json')
        bucket = storage_client.get_bucket(Bucket_Name)
        blop = bucket.blob(filename)
        blop.upload_from_filename(filename=filename)
        print("New File Uploaded")
        os.remove(filename)
        print("New File Removed")


# cs = GCPStorage
# fc = cs.readUserCSV('stock-predictor-bucket',"register_user.csv")
# print(fc)