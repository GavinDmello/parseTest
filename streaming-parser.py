#imports
import ijson
from data import Data
from utils import Utils

# instances
data = Data()
utilsInstance = Utils()

#constants
fileName = "./nvdcve-1.0-2018.json"
exploitDBRefSourceValue = "EXPLOIT-DB"

# process json file in streaming fashion
def processData():

	with open(fileName) as file:
		parser = ijson.parse(file)
		l = []
		refCount = 0
		exploitDBFlag =  0
		firstParse = True

		for prefix, event, value in parser: 

			if prefix == "CVE_Items.item.cve.CVE_data_meta.ID":
				if len(l) != 0:
					l.append(refCount)
					l.append(exploitDBFlag)
					data.addToDataFrame(l)
					print "processed CVE ID", l[0]
    		
				l = []
				refCount = 0
				exploitDBFlag = 0
				l.append(value)
				firstParse = False

			if prefix == "CVE_Items.item.publishedDate" or prefix == "CVE_Items.item.lastModifiedDate":
				value = utilsInstance.parseDate(value)
				l.append(value)
    	
			if prefix == "CVE_Items.item.impact.baseMetricV2.cvssV2.baseScore" or prefix == "CVE_Items.item.impact.baseMetricV2.exploitabilityScore" or prefix == "CVE_Items.item.impact.baseMetricV2.impactScore" or prefix == "CVE_Items.item.cve.description.description_data.item.value":
				l.append(value)

			if prefix == "CVE_Items.item.cve.references.reference_data.item.url":
				refCount = refCount + 1

			if prefix == "CVE_Items.item.cve.references.reference_data.item.refsource" and value == "EXPLOIT-DB":
				exploitDBFlag =  1

	return data.getDataFrame()

print processData()