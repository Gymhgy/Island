import random
import csv
import sys
sys.path.append("/")
from approaches import *

random.seed(78126312)
N=0
with open("islanddata.csv", 'r') as data, open("output.csv", 'w') as output:
    datareader = csv.reader(data)
    outputwriter = csv.writer(output)
    outputwriter.writerow(["Approach1", "Approach2"])
    next(datareader)
    for row in datareader:
        n = [float(s) for s in row]
        applicants = [
            (n[0],n[1]),
            (n[2],n[3]),
            (n[4],n[5]),
            (n[6],n[7])
        ]
        treasure = (n[8],n[9])
        results = [
            approach1(applicants,treasure)["time"],
            approach2(applicants,treasure)["time"],
        ]
        if len(results) !=len( set(results)):
            N+=1
        outputwriter.writerow(results)

print(N)