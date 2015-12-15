__author__ = 'kzkv'

import uuid, csv

keys = list()
key = ""

while len(keys) < 30000:
    key = str(uuid.uuid4().get_hex().upper()[0:6])

    if key not in keys:
        keys.append(key)

#print keys

with open('tickets.csv', 'wb') as myfile:
    wr = csv.writer(myfile, lineterminator='\n')
    wr.writerows([[x] for x in keys])





