import csv
import random
from bloomberg import Bloomberg

def getRandomCompanyResponse():

        with open("bloomberg/companylist.csv") as csvfile:
                linereader = csv.reader(csvfile, delimiter=',')
                companies = []
                for row in linereader:
                        companies.append(row[0])

                return Bloomberg.getFields(random.choice(companies))