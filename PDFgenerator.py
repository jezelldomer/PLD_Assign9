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

def design(resumepdf):
    resumepdf.set_font('castellar', 'B', 27) 
    resumepdf.set_text_color(0, 0, 200) 
    resumepdf.cell(180, 35, Header, ln = 1, align = 'C'); 
    resumepdf.set_font('arial', 'B', 27)
    resumepdf.set_text_color(255, 165, 0)
    resumepdf.cell(180, -10, YrandSec, ln = 0, align = 'C')
    resumepdf.set_text_color(0, 0, 0) 


def body1(resumepdf): 
    resumepdf.ln(10) 
    resumepdf.cell(90, 10, title1) 
    resumepdf.ln(10) 
    resumepdf.set_font("times", "B", 12) 
    resumepdf.cell(40, 6, "   Name          :  " + str(charac["primaryElements"][0]["Full Name"]), ln = 10)
    resumepdf.cell(40, 6, "Sex / Gender      :  " + str(charac["primaryElements"][0]["Sex / Gender"]), ln = 10)
    resumepdf.cell(40, 6, "Age                     :  " + str(charac["primaryElements"][0]["Age"]), ln = 10)
    resumepdf.cell(40, 6, "Address   :  " + str(charac["primaryElements"][0]["Address"]), ln = 10)
    resumepdf.cell(40, 6, "Height                :  " + str(charac["primaryElements"][0]["Height"]), ln = 10)
    resumepdf.cell(40, 6, "Weight               :  " + str(charac["primaryElements"][0]["Weight"]), ln = 10)
    resumepdf.ln(15) 







