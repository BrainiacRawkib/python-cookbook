# rank zipcodes by the number of pothole reports
from xml.etree.ElementTree import parse
from collections import Counter
from ch_06.ex_04 import parse_and_remove

potholes_by_zip = Counter()

doc = parse('potholes.xml')

for pothole in doc.iterfind('row/row'):
    potholes_by_zip[pothole.findtext('zip')] += 1

for zipcode, num in potholes_by_zip.most_common():
    print(zipcode, num)

# or

data = parse_and_remove('potholes.xml', 'row.row')

for pothole in data:
    potholes_by_zip[pothole.findtext('zip')] += 1

for zipcode, num in potholes_by_zip.most_common():
    print(zipcode, num)

if __name__ == '__main__':
    pass
