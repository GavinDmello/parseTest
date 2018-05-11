# imports
import json
from data import Data
from utils import Utils

# instances
data = Data()
utilsInstance = Utils()

# constants
fileName = "./nvdcve-1.0-2018.json"
exploitDBRefSourceValue = "EXPLOIT-DB"

# process the json value 
def processData():
	with open(fileName) as file:
		contents = json.load(file)
    	cveItems = contents["CVE_Items"]

    	for individualCveItem in cveItems:
    		try :
    			cveId = individualCveItem["cve"]["CVE_data_meta"]["ID"]
    			description = individualCveItem["cve"]["description"]["description_data"][0]["value"]
    			baseScore = individualCveItem["impact"]["baseMetricV2"]["cvssV2"]["baseScore"]
    			exploitabilityScore = individualCveItem["impact"]["baseMetricV2"]["exploitabilityScore"]
    			impactScore = individualCveItem["impact"]["baseMetricV2"]["impactScore"]
    			publishedDate = utilsInstance.parseDate(individualCveItem["publishedDate"])
    			lastModifiedDate = utilsInstance.parseDate(individualCveItem["lastModifiedDate"])
    			refCount = len(individualCveItem["cve"]["references"]["reference_data"])
    			exploitDBFlag = isExploitDBRefPresent(individualCveItem["cve"]["references"]["reference_data"])
    			row = [
    				cveId, 
    				description, 
    				baseScore, 
    				exploitabilityScore, 
    				impactScore, 
    				publishedDate,
    				lastModifiedDate,
    				refCount,
    				exploitDBFlag
    			]
    			data.addToDataFrame(row)
    			print "Processing CVE ID", cveId

    		except :
    			# print "Key error, some properties are missing. Skipping row"
    			pass
    	
    	return data.getDataFrame()

# checks if a exploit db reference is present in the references
def isExploitDBRefPresent(references):
	exploitDBFlag = 0
	for reference in  references:
		if reference["refsource"] == exploitDBRefSourceValue:
			exploitDBFlag = 1
    		break
	return exploitDBFlag



print processData()