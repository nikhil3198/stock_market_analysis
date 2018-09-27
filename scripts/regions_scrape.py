from time import sleep
import re
import csv
from selenium import webdriver
from selenium.webdriver.support.ui import Select 


d = webdriver.Chrome()
base_url="https://trendogate.com/"
d.get(base_url)

select = Select(d.find_element_by_name('place'))
places=[o.text for o in select.options]
myString='United States'
pattern = r'\b' + re.escape(myString) + r'\b'
values = [x for i, x in enumerate(places) if re.search(pattern, x)]
print(values)

with open("regions.csv", "w") as output:
    writer = csv.writer(output, lineterminator='\n')
    for val in values:
        writer.writerow([val])   
