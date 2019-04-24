from pathlib import Path
import requests
#Create folders for the pdfs
import pathlib
for year in range (1998,2013): 
    pathlib.Path("/Users/erica/Documents/VS Code Projects/Download PDF/"+str(year)+"SAT").mkdir(parents=True, exist_ok=True)

states = ["Alabama","Alaska","Arizona","Arkansas","California","Colorado",
  "Connecticut","Delaware","Florida","Georgia","Hawaii","Idaho","Illinois",
  "Indiana","Iowa","Kansas","Kentucky","Louisiana","Maine","Maryland",
  "Massachusetts","Michigan","Minnesota","Mississippi","Missouri","Montana",
  "Nebraska","Nevada","New-Hampshire","New-Jersey","New-Mexico","New-York",
  "North-Carolina","North-Dakota","Ohio","Oklahoma","Oregon","Pennsylvania",
  "Rhode-Island","South-Carolina","South-Dakota","Tennessee","Texas","Utah",
  "Vermont","Virginia","Washington","West-Virginia","Wisconsin","Wyoming"]

states2 = ["Alabama","Alaska","Arizona","Arkansas","California","Colorado",
  "Connecticut","Delaware","Florida","Georgia","Hawaii","Idaho","Illinois",
  "Indiana","Iowa","Kansas","Kentucky","Louisiana","Maine","Maryland",
  "Massachusetts","Michigan","Minnesota","Mississippi","Missouri","Montana",
  "Nebraska","Nevada","New_Hampshire","New_Jersey","New_Mexico","New_York",
  "North_Carolina","North_Dakota","Ohio","Oklahoma","Oregon","Pennsylvania",
  "Rhode_Island","South_Carolina","South_Dakota","Tennessee","Texas","Utah",
  "Vermont","Virginia","Washington","West_Virginia","Wisconsin","Wyoming"]

abrstates = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL", "GA", 
            "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", 
            "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", 
            "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", 
            "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]
#1998-2000
for year in range(1998,2001):
    for y in states:
        for x in abrstates:
            url = "http://secure-media.collegeboard.org/digitalServices/pdf/research/cb-seniors-"+str(year)+"-"+x+".PDF"
            filename = Path("/Users/erica/Documents/VS Code Projects/Download PDF/"+str(year)+"SAT/"+str(year)+y+".pdf")
            response = requests.get(url)
            filename.write_bytes(response.content)
#2001
for y in states:
        for x in abrstates:
            url = "http://secure-media.collegeboard.org/digitalServices/pdf/research/cb-seniors-2001-"+x+".pdf"
            filename = Path("/Users/erica/Documents/VS Code Projects/Download PDF/2001SAT/2001"+y+".pdf")
            response = requests.get(url)
            filename.write_bytes(response.content)
#2002-2003
for year in range(2002,2004):
    for y in states:
        for z in states2:
                url = "http://secure-media.collegeboard.org/digitalServices/pdf/research/cb-seniors-"+str(year)+"-"+z.upper()+".pdf"
                filename = Path("/Users/erica/Documents/VS Code Projects/Download PDF/"+str(year)+"SAT/"+str(year)+y+".pdf")
                response = requests.get(url)
                filename.write_bytes(response.content)
#2004, 2007
for year in range(2004,2008,3):
    for y in states:
        for x in abrstates:
            url = "http://secure-media.collegeboard.org/digitalServices/pdf/research/cb-seniors-"+str(year)+"-"+x+".pdf"
            filename = Path("/Users/erica/Documents/VS Code Projects/Download PDF/"+str(year)+"SAT/"+str(year)+y+".pdf")
            response = requests.get(url)
            filename.write_bytes(response.content)
#2005-2006
for year in range(2005,2007):
    for y in states:
        url = "http://secure-media.collegeboard.org/digitalServices/pdf/research/cb-seniors-"+str(year)+"-"+y.lower()+".pdf"
        filename = Path("/Users/erica/Documents/VS Code Projects/Download PDF/"+str(year)+"SAT/"+str(year)+y+".pdf")
        response = requests.get(url)
        filename.write_bytes(response.content)
#2008
for y in states:
    url: "http://secure-media.collegeboard.org/digitalServices/pdf/research/"+y+"_CBS_08.pdf"
    filename = Path("/Users/erica/Documents/VS Code Projects/Download PDF/2008SAT/2008"+y+".pdf")
    response = requests.get(url)
    filename.write_bytes(response.content)
#2009
for y in states:
    for x in abrstates:
        url = "http://secure-media.collegeboard.org/digitalServices/pdf/research/"+x+"_09_03_03_01.pdf"
        filename = Path("/Users/erica/Documents/VS Code Projects/Download PDF/2009SAT/2009"+y+".pdf")
        response = requests.get(url)
        filename.write_bytes(response.content)
#2010-2012
for year in range(10,13):
    for y in states:
        for x in abrstates:
            url = "http://secure-media.collegeboard.org/digitalServices/pdf/research/"+x+"_"+str(year)+"_03_03_01.pdf"
            filename = Path("/Users/erica/Documents/VS Code Projects/Download PDF/20"+str(year)+"SAT/20"+str(year)+y+".pdf")
            response = requests.get(url)
            filename.write_bytes(response.content)
#2013
for y in states:
    for x in abrstates:
        url = "http://secure-media.collegeboard.org/digitalServices/pdf/research/2013/"+x+"_13_03_03_01.pdf"
        filename = Path("/Users/erica/Documents/VS Code Projects/Download PDF/2013SAT/2013"+y+".pdf")
        response = requests.get(url)
        filename.write_bytes(response.content)
#2014-2016
for year in range(14,17):
    for y in states:
        for x in abrstates:
            url = "https://secure-media.collegeboard.org/digitalServices/pdf/sat/"+x+"_"+str(year)+"_03_03_01.pdf"
            filename = Path("/Users/erica/Documents/VS Code Projects/Download PDF/20"+str(year)+"SAT/20"+str(year)+y+".pdf")
            response = requests.get(url)
            filename.write_bytes(response.content)
#2017-2018
for year in range(2017,2019):
    for y in states:
        url = "https://reports.collegeboard.org/pdf/"+str(year)+"-"+y+"-sat-suite-assessments-annual-report.pdf"
        filename = Path("/Users/erica/Documents/VS Code Projects/Download PDF/"+str(year)+"SAT/"+str(year)+y+".pdf")
        response = requests.get(url)
        filename.write_bytes(response.content)
