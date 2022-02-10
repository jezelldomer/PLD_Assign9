# Assignment 9

# PDF Resume Creator
# 	- Create a python program that will create your personal resume in PDF format
# 	- All personal details are stored in a JSON file
# 	- Your program should read the JSON file and write the details in the PDF
# 	- The output file should be: LASTNAME_FIRSTNAME.pdf

# Note:
# 	- Search for available PDF library that you can use
# 	- Search how data is structured using JSON format
# 	- Search how to read JSON file
# 	- You will create the JSON file manually
# 	- Your code should be in github before Feb12

import os as access; from PyPDF2 import PdfFileReader; import json;

# Import OS as to interact with the Microsoft Windows default settings.
# I install and used the PyPDF2 (PDF File Reader - PyPDF2) imported on Python to generate my program to a PDF
# Import JSON Source File 
# I've updated my Python Version from 3.10 to 3.10.2
# And the PIP Install Package used for External Modules 

Header = 'RESUME' 
YrandSec = 'BSCOE 1-6' 
save = 'Domer_Jezell.pdf' 

title1 = 'Personal Information'
title2 = 'Contact Information'
title3 = 'Education'
title4 = 'Achievements'
title5 = 'Experiences'
title6 = 'Additional Skills'

jsonPD = "resume.json" 


resumepdf = PdfFileReader 
with open(jsonPD, 'r+') as obj: 
    charac = json.loads(obj.read()) 
resumepdf.add_page() 







