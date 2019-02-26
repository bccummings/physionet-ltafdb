with open('RECORDS', 'r') as myfile:
    records = myfile.readlines()

print("cd data/") # your directory here
for iPt in records:
    print("wget https://physionet.org/physiobank/database/ltafdb/{}.atr".format(iPt.strip()))
    print("wget https://physionet.org/physiobank/database/ltafdb/{}.dat".format(iPt.strip()))
    print("wget https://physionet.org/physiobank/database/ltafdb/{}.hea".format(iPt.strip()))
    print("wget https://physionet.org/physiobank/database/ltafdb/{}.qrs".format(iPt.strip()))
