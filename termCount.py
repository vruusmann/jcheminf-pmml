import urllib
import xml.etree.ElementTree as ET

u = "http://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?term=%s&mindate=%d/01/01&maxdate=%d/12/31"
term = "QSAR or QSPR"
startYear = 1980
endYear = 2013
for year in range(startYear, endYear+1):
    url = u % (term.replace(" ", "+"), year, year)
    page = urllib.urlopen(url).read()
    doc = ET.XML(page)
    count = doc.find("Count").text
    print year, count
