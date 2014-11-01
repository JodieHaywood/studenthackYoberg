import blpapi

def getFieldValues(company, fields):

        host = "10.8.8.1"
        port = 8194
        REFDATA_SVC = "//blp/refdata"

        sessionOptions = blpapi.SessionOptions()
        sessionOptions.setServerHost(host)
        sessionOptions.setServerPort(port)

        print "Connecting to %s:%d" % (host, port)

        # Create a Session
        session = blpapi.Session(sessionOptions)

        # Start a Session
        if not session.start():
                print "Failed to start session."

        if not session.openService(REFDATA_SVC):
                print "Failed to open //blp/refdata"

        refDataService = session.getService(REFDATA_SVC)
        request = refDataService.createRequest("ReferenceDataRequest")

        # append security to request
        request.append("securities", company + " US Equity")

        # append fields to request
        for field in fields:
                request.append("fields", field)

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


def getFields(text):
        host = "10.8.8.1"
        port = 8194
        APIFLDS_SVC = "//blp/apiflds"
        FIELD_ID = blpapi.Name("id")
        FIELD_MNEMONIC = blpapi.Name("mnemonic")
        FIELD_DATA = blpapi.Name("fieldData")
        FIELD_DESC = blpapi.Name("description")
        FIELD_INFO = blpapi.Name("fieldInfo")
        FIELD_ERROR = blpapi.Name("fieldError")
        FIELD_MSG = blpapi.Name("message")

        # Fill SessionOptions
        sessionOptions = blpapi.SessionOptions()
        sessionOptions.setServerHost(host)
        sessionOptions.setServerPort(port)

        print "Connecting to %s:%d" % (host, port)

        # Create a Session
        session = blpapi.Session(sessionOptions)

        # Start a Session
        if not session.start():
                print "Failed to start session."
                return

        if not session.openService(APIFLDS_SVC):
                print "Failed to open", APIFLDS_SVC
                return

        fieldInfoService = session.getService(APIFLDS_SVC)
        request = fieldInfoService.createRequest("FieldSearchRequest")
        request.set("searchSpec", text)
        exclude = request.getElement("exclude")
        exclude.setElement("fieldType", "Static")
        request.set("returnFieldDocumentation", False)

        print "Sending Request:", request
        session.sendRequest(request)

        try:
                # Process received events
                while(True):
                        # We provide timeout to give the chance to Ctrl+C handling:
                        ev = session.nextEvent(500)
                        data = []
                        if ev.eventType() != blpapi.Event.RESPONSE and \
                                ev.eventType() != blpapi.Event.PARTIAL_RESPONSE:
                                continue
                        for msg in ev:
                                for field in msg.getElement("fieldData").values():
                                        fldInfo = field.getElement(FIELD_INFO)
                                        data.append([field.getElementAsString(FIELD_ID), fldInfo.getElementAsString(FIELD_MNEMONIC), fldInfo.getElementAsString(FIELD_DESC)])

                        # Response completly received, so we could exit
                        if ev.eventType() == blpapi.Event.RESPONSE:
                                return data
        finally:
                # Stop the session
                session.stop()