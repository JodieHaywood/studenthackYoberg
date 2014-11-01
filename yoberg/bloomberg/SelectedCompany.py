from bloomberg import Bloomberg

def getSelectedCompanyResponse(company):
        result = Bloomberg.getFields(company)

        strResult = str(result['DS002']) + " last priced at: " + str(result['PX_LAST']) + " " + str(result['DS004'])
        return strResult
