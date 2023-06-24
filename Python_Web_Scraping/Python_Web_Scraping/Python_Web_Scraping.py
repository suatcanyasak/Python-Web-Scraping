import requests
from bs4 import BeautifulSoup
import xlsxwriter

url = "https://www.example-site.com/data" #The address of the website from which data will be extracted is assigned to a variable.

response = requests.get(url) #The website is called with the get command.
html_content = response.content #With the content command, all the content of the website is read.
soup = BeautifulSoup(html_content,"html.parser") #Separates the entire content of the website.
data_example = soup.find_all("div",{"class":"class data 1"}) #The class expressions are the expressions assigned to the received data in the open source code (ctrl+u or ctrl+shift+c) of the data source site.
data_example2 =soup.find_all("a",{"class":"class data 2"}) #With the find_all command, all data with that class are retrieved.
data_example3 = soup.find_all("a",{"class":"class data 3"}) 
data_example4 = soup.find_all("a",{"class":"class data 4"}) 

for i in range(len(data_example)): #All data are listed separately according to their class.
    data_example[i] = (data_example[i].text).strip("\n").strip()
    data_example2[i] = (data_example2[i].text).strip("\n").strip()
    data_example3[i] = (data_example3[i].text).strip("\n").strip()
    data_example4[i] = (data_example4[i].text).strip("\n").replace("\nTL"," TL").strip()    

workbook = xlsxwriter.Workbook('my_list.xlsx') #Turns on data entry for Excel file.
worksheet = workbook.add_worksheet() #excel file is created and add_worksheet is used to add.

for row,datas in enumerate(data_example): #Prints data starting from first row for first column (zeroth index)
    worksheet.write(row,0,datas)

for row,datas in enumerate(data_example2): #Prints data starting from first row for second column (first index)
    worksheet.write(row,1,datas)

for row,datas in enumerate(data_example3): #Prints data starting from first row for third column (second index)
    worksheet.write(row,2,datas)

for row,datas in enumerate(data_example4): #Prints data starting from first row for fourth column (third index)
    worksheet.write(row,3,datas)

workbook.close() #Turns off data entry to Excel file and saves the changes.







