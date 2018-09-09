#!/usr/bin/env python3

import re

from selenium import webdriver

# create a Chome robot
driver = webdriver.Chrome()
driver.get("http://www.hkcib.org/hkcib/common/register/MemberSummary.faces")

# find the total number of pages
total_page = driver.find_element_by_xpath("//*[contains(text(), '總共 ')]").text
total_page = int(re.search(r'\d+',total_page).group(0))

# the javascript the clicks the next page, copied from the website itself
next_page_script = "document.forms['form1']['form1:_idcl'].value='form1:_id13next';document.forms['form1']['form1:_id13'].value='next'; document.forms['form1'].submit();"
for p in range(1,total_page):
    # try to download the webpage as .html file
    # and give it a page number
    try:
        filename = "MemberDetails\page" + str(p) + ".html"
        with open(filename, 'w') as f:
            f.write(driver.page_source)
    # if the command fails, output an error message to the cmd
    except:
        print("Error with saving page %s to " % filename)

    # execute the javascript that clicks the next page
    driver.execute_script(next_page_script)
    print(p)
