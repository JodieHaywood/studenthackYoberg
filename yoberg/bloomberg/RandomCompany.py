import csv
import random
from bloomberg import Bloomberg

def getRandomCompanyResponse():

        with open("bloomberg/companylist.csv") as csvfile:
                linereader = csv.reader(csvfile, delimiter=',')
                companies = []
                for row in linereader:
                        companies.append(row[0])

                result = Bloomberg.getFields(random.choice(companies))

                strResult = str(result['DS002']) + " last priced at: " + str(result['PX_LAST']) + " " + str(result['DS004'])
                return strResult
