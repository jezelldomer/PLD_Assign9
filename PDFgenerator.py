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

# Import OS as to interact with the Microsoft Windows default settings.
# I install and used the FPDF imported on Python to generate my program to a PDF
# I Import JSON Source File 
# I've updated my Python Version from 3.10 to 3.10.2
# And the PIP Install Package used for External Modules 

import os as access; from fpdf import FPDF; import json

Header = 'My RESUME' 
YrandSec = 'BSCOE 1-6, Student' 
save = 'DOMER_JEZELL.pdf' 

title1 = 'Personal Information'
title2 = 'Contact Information'
title3 = 'Education'
title4 = 'Experiences'
title5 = 'Additional Skills'
title6 = 'Achievements'

jsonPD = "resume.json" 

resumepdf = FPDF('P', 'mm', 'Legal')
with open(jsonPD, 'r') as obj: 
    charac = json.loads(obj.read()) 
resumepdf.add_page() 

def design(resumepdf):
    resumepdf.set_font('arial', 'B', 25) 
    resumepdf.set_text_color(0, 0, 200)    
    resumepdf.cell(180, 35, Header, ln = 1, align = 'C');  
    resumepdf.image('header.png', 7, 0, 200, 0)
    resumepdf.image('idpic.png', 167, 20, 40, 0)
    resumepdf.set_font('arial', 'B', 20)
    resumepdf.set_text_color(0, 0, 0)
    resumepdf.cell(180, -10, YrandSec, ln = 0, align = 'C')
    resumepdf.set_text_color(0, 0, 0) 
    
    
def body1(resumepdf): 
    resumepdf.ln(10) 
    resumepdf.cell(90, 0, title1) 
    resumepdf.ln(10) 
    resumepdf.set_font("times", "B", 12) 
    resumepdf.cell(40, 6, "Name                  :  " + str(charac["primaryElements"][0]["Name"]), ln = 10)
    resumepdf.cell(40, 6, "Sex / Gender      :  " + str(charac["primaryElements"][0]["Sex / Gender"]), ln = 10)
    resumepdf.cell(40, 6, "Address              :  " + str(charac["primaryElements"][0]["Home Address"]), ln = 10)
    resumepdf.cell(40, 6, "Age                     :  " + str(charac["primaryElements"][0]["Age"]), ln = 10)
    resumepdf.cell(40, 6, "Height                :  " + str(charac["primaryElements"][0]["Height"]), ln = 10)
    resumepdf.cell(40, 6, "Weight               :  " + str(charac["primaryElements"][0]["Weight"]), ln = 10)
    resumepdf.ln(15) 

def body2(resumepdf): 
    resumepdf.set_font("arial", "B", 20)
    resumepdf.cell(90, 0, title2) 
    resumepdf.ln(5) 
    resumepdf.set_font("times", "B", 11) 
    resumepdf.cell(40, 6, "E-Mail                :  " + str(charac["contactInformation"][0]["E-Mail"]), ln = 10)
    resumepdf.cell(40, 6, "Mobile Number :           " + str(charac["contactInformation"][0]["Mobile Number"]), ln = 10)
    resumepdf.cell(40, 6, "Landline Number       :  " + str(charac["contactInformation"][0]["Landline Number"]), ln = 10)
    resumepdf.ln(15) 

def body3(resumepdf): 
    resumepdf.set_font("arial", "B", 20) 
    resumepdf.cell(90, 0, title3) 
    resumepdf.ln(5) 
    resumepdf.set_font("times", "B", 11) 
    resumepdf.cell(40, 6, "Elementary                   :  " + str(charac["academicBackground/Education"][0]["Elementary"]), ln = 10)
    resumepdf.cell(40, 6, "Middle School                 :  " + str(charac["academicBackground/Education"][0]["Middle School"]), ln = 10)
    resumepdf.cell(40, 6, "Senior High School           :  " + str(charac["academicBackground/Education"][0]["Senior High School"]), ln = 10)
    resumepdf.cell(40, 6, "University or College             :  " + str(charac["academicBackground/Education"][0]["College"]), ln = 10)
    resumepdf.ln(15) 

def body4(resumepdf): 
    resumepdf.set_font("arial", "B", 20) 
    resumepdf.cell(90, 0, title4) 
    resumepdf.ln(5) 
    resumepdf.set_font("arial", "B", 12) 
    resumepdf.cell(40, 6, " Music                                   :  " + str(charac["Experiences"][0]["Music"]), ln = 10)
    resumepdf.cell(40, 6, " Church Ministry                 :  " + str(charac["Experiences"][0]["Church Ministry"]), ln = 10)
    resumepdf.ln(15) 

def body5(resumepdf): 
    resumepdf.set_font("arial", "B", 20)
    resumepdf.cell(90, 0, title5) 
    resumepdf.ln(5) 
    resumepdf.set_font("times", "B", 12) 
    resumepdf.cell(40, 6, "" + str(charac["Additional Skills"][0]), ln = 10)
    resumepdf.ln(5) 
    resumepdf.set_font("times", "B", 12) 
    resumepdf.cell(40, 6, "" + str(charac["Additional Skills"][1]), ln = 10)
    resumepdf.ln(5) 
    resumepdf.set_font("times", "B", 12) 
    resumepdf.cell(40, 6, "" + str(charac["Additional Skills"][2]), ln = 10)
    resumepdf.ln(5) 
    resumepdf.set_font("times", "B", 12) 
    resumepdf.cell(40, 6, "" + str(charac["Additional Skills"][3]), ln = 10)
    resumepdf.ln(15) 

def body6(resumepdf):
    resumepdf.set_font("arial", "B", 20) 
    resumepdf.cell(90, 0, title6) 
    resumepdf.ln(5) 
    resumepdf.set_font("times", "B", 11) 
    resumepdf.cell(40, 6, "A.  " + str(charac["Achievement/s"][0]), align = '')
    resumepdf.cell(120, 6,      "B.    " + str(charac["Achievement/s"][1]), ln = 10, align = 'C')
    resumepdf.ln(0) 
    resumepdf.cell(40, 6, "C.  " + str(charac["Achievement/s"][2]), align = '')
    resumepdf.cell(150, 6, "D.  " + str(charac["Achievement/s"][3]), ln = 10, align = 'C')
    resumepdf.ln(15)

def generatePDF():
    design(resumepdf) 
    body1(resumepdf)
    body2(resumepdf)
    body3(resumepdf) 
    body4(resumepdf) 
    body5(resumepdf) 
    body6(resumepdf) 
    footer(resumepdf)

def footer(resumepdf):
    resumepdf.set_y(-9) 
    resumepdf.image('footer.png', 10, 340, 200, 0) 

generatePDF()

resumepdf.set_auto_page_break(margin = 0.5, auto = True) 
resumepdf.output(save)
access.startfile(save)