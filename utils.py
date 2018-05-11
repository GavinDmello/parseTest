from dateutil.parser import parse

class Utils:
	# constructor
    def __init__(self):
    	self.dateFormat = "%d/%m/%Y"
    	pass


    # parses Date to new format
    def parseDate(self, date):
    	datetime = parse(date)
    	return datetime.strftime(self.dateFormat)