# parseTest

- streaming-parser.py 
	This streams the json file. It will be more memory efficient if the JSON size 
	grows in the future

- simple-parser.py
	This loads the json file directly. Works well for small json files. It will be 
	a memory hog if the file size grows.

- utils.py
	contains the data formating function

- data.py
	contains the functions to add, display are return the dataframe