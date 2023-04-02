dict1 = {"NFLX": 4950, "TREX": 2400, "FIZZ": 1800, "XPO": 1700}
dict2 = {}

for k in dict1.keys():
    if dict1[k] > 2000:
        dict2[k] = dict1[k]
    else:
        continue
print(dict2)