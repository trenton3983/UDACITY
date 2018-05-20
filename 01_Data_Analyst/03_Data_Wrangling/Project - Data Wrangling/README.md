# Project - Data Wrangling for UDACITY Nanodegree - Trenton J. McKinney
# All code requires python version 3.6...this code will not work in 2.7
## This is an ETL (Extract, Transform & Load) Project using python and SQL
#### For the best viewing experience, use Project_Data_Wrangling.ipynb or Project_Data_Wrangling.html
#### Project_Data_Wrangling.pdf: Internal navigation links do not work
## File Description

* **<a href="https://github.com/trenton3983/UDACITY/blob/master/01_Data_Analyst/03_Data_Wrangling/Project%20-%20Dat
a%20Wrangling/Project_Data_Wrangling.pdf">Project_Data_Wrangling.pdf</a>** - This is the main write up for the project in pdf
* **<a href="https://github.com/trenton3983/UDACITY/blob/master/01_Data_Analyst/03_Data_Wrangling/Project%20-%20Dat
a%20Wrangling/Project_Data_Wrangling.html">Project_Data_Wrangling.html</a>** - This is the main write up for the project in html
* **<a href="https://github.com/trenton3983/UDACITY/blob/master/01_Data_Analyst/03_Data_Wrangling/Project%20-%20Dat
a%20Wrangling/Project_Data_Wrangling.ipynb">Project_Data_Wrangling.ipynb</a>** - This is the main write up for the project as an ipynb
* **<a href="https://github.com/trenton3983/UDACITY/blob/master/01_Data_Analyst/03_Data_Wrangling/Project%20-%20Dat
a%20Wrangling/audit_street_names.py">audit_street_names.py</a>** - a script for reviewing street names
* **<a href="https://github.com/trenton3983/UDACITY/blob/master/01_Data_Analyst/03_Data_Wrangling/Project%20-%20Dat
a%20Wrangling/audited_street_names_full.txt">audited_street_names_full.txt</a>** - this is a full list of the fixed street names
* **<a href="https://github.com/trenton3983/UDACITY/blob/master/01_Data_Analyst/03_Data_Wrangling/Project%20-%20Dat
a%20Wrangling/portland_oregon_95_sample.7z">portland_oregon_95_sample.7z</a>** - this is a small sample of the osm file
* **<a href="https://github.com/trenton3983/UDACITY/blob/master/01_Data_Analyst/03_Data_Wrangling/Project%20-%20Dat
a%20Wrangling/portland_osm_map.ipynb">portland_osm_map.ipynb</a>** - used to create the map in the project write up
* **<a href="https://github.com/trenton3983/UDACITY/blob/master/01_Data_Analyst/03_Data_Wrangling/Project%20-%20Dat
a%20Wrangling/project_abbreviated_street_names.py">project_abbreviated_street_names.py</a>** - this is a nested dict output by audit_street_names.py; it contains the full list
of streets that aren't excluded by being in the EXPECTED list.
* **<a href="https://github.com/trenton3983/UDACITY/blob/master/01_Data_Analyst/03_Data_Wrangling/Project%20-%20Dat
a%20Wrangling/project_fix_city_name.py">project_fix_city_name.py</a>** - method for fixing city names
* **<a href="https://github.com/trenton3983/UDACITY/blob/master/01_Data_Analyst/03_Data_Wrangling/Project%20-%20Dat
a%20Wrangling/project_fix_street_name.py">project_fix_street_name.py</a>** - method for fixing street names
* **<a href="https://github.com/trenton3983/UDACITY/blob/master/01_Data_Analyst/03_Data_Wrangling/Project%20-%20Dat
a%20Wrangling/project_fix_zip_code.py">project_fix_zip_code.py</a>** - method for fixing zip codes
* **<a href="https://github.com/trenton3983/UDACITY/blob/master/01_Data_Analyst/03_Data_Wrangling/Project%20-%20Dat
a%20Wrangling/project_to_csv.py">project_to_csv.py</a>** - main program for converting osm file into a csv; this script calls the project_fix scripts to
repair the data prior to writing it into the csv.