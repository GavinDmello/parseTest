import pandas as pd

class Data:
	# constructor
    def __init__(self):
    	self.cols = [
    		'ID', 
    		'description', 
    		'cvssV2_baseScore',
    		'exploitabilityScore',
    		'impactScore',
    		'publishedDate', 
    		'lastModifiedDate', 
    		'ref_count',
    		'exploit_db'
    	]
        self.df = pd.DataFrame(columns = self.cols)


    # add rows to the data frame 
    def addToDataFrame(self, new_df):

    	# some records don't have an impact
    	if len(new_df) != len(self.cols):
    		return

    	self.df.loc[len(self.df)] = new_df

    # Prints the data frame to the console
    def displayDataFrame(self):
    	print self.df

    # returns the dataframe
    def getDataFrame(self):
        return self.df

