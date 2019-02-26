with open('RECORDS', 'r') as myfile:
    records = myfile.readlines()

print("cd ../raw") # adjust paths to fit your needs

for record in records:
    print("rdsamp -r {} > ../data/{}.data".format(record.strip(), record.strip()))
    print("rdann -r {} -a qrs > ../data/{}.ann".format(record.strip(), record.strip()))
