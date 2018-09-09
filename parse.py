#!/usr/bin/env python3

import csv
import os
import glob
import re

from bs4 import BeautifulSoup as bs

# obtain the absolute path of the downloaded .html files
PATH = os.getcwd() + '\MemberDetails'

# Main

# first create an empty .csv file
# open it in write mode 'w'
# give it an alias -> csvfile
# newline='' means that the ending character of each line
# is configured to the default newline character according to your OS
# e.g. for Windows a newline character is \r\n
# e.g. for Linux a newline character is \n
# the default encoding for Chinese character on Windows is Big5
# you may specify it as -> encoding='utf-8'
with open("hkcib_results.csv", 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)

    # write headers for the data
    writer.writerow([
        "Membership No.",
        "Name of Company(E)",
        "Name of Company(C)",
        "CE Name(E)",
        "CE Name(C)",
        "Status"
    ])

    # create a loop that process each .html file
    # filename -> each file in MemberDetails ending with .html extension
    for filename in glob.glob(os.path.join(PATH, '*.html')):
        print("processing ", filename)

        soup = bs(open(filename), 'html.parser')

        # find all rows and put them into a list called contentrows
        # \ is a sepeartor for code lines that are too long
        contentrows = soup.find_all('tr', attrs={"class": "summaryRow"}) \
                    + soup.find_all('tr', attrs={"class": "summaryRow2"})

        # extract data from each company
        for row in contentrows:
            company_name = row.find_all('td', attrs={"class": "MemSearch_Company_Name"})
            company_name_en = company_name[0].text
            company_name_zh = company_name[1].text

            CE_name = row.find_all('td', attrs={"class": "MemSearch_CE_Name"})
            CE_name_en = CE_name[0].text
            CE_name_zh = CE_name[1].text

            others = row.find_all('td', attrs={"class":"MemSearch_Member_No"})
            membership_no = others[0].text
            status = others[1].text

            # finally output the data to the .csv file
            writer.writerow([membership_no, company_name_en, company_name_zh, CE_name_en, CE_name_zh, status])
            


