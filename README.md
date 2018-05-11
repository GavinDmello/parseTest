# parseTest

- streaming-parser.py 
	This streams the json file. It will be more memory efficient if the JSON size 
	grows in the future

- simple-parser.py
	This loads the json file directly. Works well for small json files. It will be 
	a memory hog if the file size grows.

- utils.py
	contains the date formating function

- data.py
	contains the functions to add, display are return the dataframe

## requirements
pip install ijson


## For processing with streams 
```
	python streaming-parser.py
```

## For processing without streams
```
	python simple-parser.py
```

