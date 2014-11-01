import csv
import random
import blpapi

def getRandomCompanyResponse():

        host = "10.8.8.1"
        port = 8194

        with open("companylist.csv") as csvfile:
                linereader = csv.reader(csvfile, delimiter=',')
                companies = []
                for row in linereader:
                        companies.append(row[0])

                sessionOptions = blpapi.SessionOptions()
                sessionOptions.setServerHost(host)
                sessionOptions.setServerPort(port)

                print "Connecting to %s:%d" % (host, port)

                # Create a Session
                session = blpapi.Session(sessionOptions)

                # Start a Session
                if not session.start():
                        print "Failed to start session."

                if not session.openService("//blp/refdata"):
                        print "Failed to open //blp/refdata"

                refDataService = session.getService("//blp/refdata")
                request = refDataService.createRequest("ReferenceDataRequest")

                # append security to request
                request.append("securities", random.choice(companies) + " US Equity")

                # append fields to request
                request.append("fields", "PX_LAST")
                request.append("fields", "DS002")
                request.append("fields", "DS003")
                request.append("fields", "DS004")
                request.append("fields", "DS005")

                print "Sending Request:", request
                session.sendRequest(request)

                try:
                        # Process received events
                        while(True):
                                # We provide timeout to give the chance to Ctrl+C handling:
                                ev = session.nextEvent(500)
                                for msg in ev:
                                        pass
                                        # print msg
                                        # Response completly received, so we could exit
                                if ev.eventType() == blpapi.Event.RESPONSE:
                                        data = dict()
                                        for msg in ev:
                                                for element in msg.asElement().getElement("securityData").getValue().getElement("fieldData").elements():
                                                        data[element.name().__str__()] = element.getValue()
                                        return data
                finally:
                        # Stop the session
                        session.stop()