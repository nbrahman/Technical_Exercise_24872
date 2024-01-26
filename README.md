# Technical_Exercise_24872
This repository includes files for technical assessment. The file details are as below.

1. **Part1.py:** This file incldues the code to extract data, and generate visualization for the technical assessment Part 1.
	- The code uses libraries like 
		- **WBGAPI:** to extract the data from World Bank Databank. The data is extracted for series code SH.STA.BASS.ZS.
		- **PANDAS:** to extract, wrangle, and transform the data.
		- **PLOTLY:** to plot final visualization
		- **TRACEBACK:** for exception handling
	- The functions in the code are detailed below
		- **__addErrors:** Function for exception handling, to add the errors encountered.
		- **__displayErrors:** Function to display encountered and handled exceptions and errors.
		- **__readWBGData:** Function to extract the data from Databank using WBGAPI library. This function also displays the visualization in browser.

2. **Part 1 Report.pdf:** This file includes some details about the code used to extract the data and generate the chart. It also incldues the chart and some analysis based on the data.

3. **Part 2 Report.pdf:** This file includes detailed steps to create data pipeline, some of my preferences/choices to create the data pipeline concept diagram, and actual concept diagram for the data pipeline.
