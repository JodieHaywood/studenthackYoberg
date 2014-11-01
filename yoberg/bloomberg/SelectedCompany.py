from bloomberg import Bloomberg

def getSelectedCompanyResponse(company):
        result = Bloomberg.getFields(company)

        strResult = result['DS002'] + " last priced at: " + result['PX_LAST'] + " " + result['DS004']
        return strResult
