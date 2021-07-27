import gspread          # library to use the sheets API 
import math             # library to use the function ceil


gc = gspread.service_account (filename = 'service_account.json')                                                            # setting the credentials file
sh = gc.open_by_url ('https://docs.google.com/spreadsheets/d/1HLNVnAsUohEVQUas9SLWDQuE_N_mZWVg0JqBhbuqAsc/edit#gid=0')      # setting the spreadsheet link
worksheet = sh.sheet1                                                                                                       # setting the spreadsheet page




def Average (Student):                                  # returns the average of the grades 
    p1 = Student ["P1"]
    p2 = Student ["P2"]
    p3 = Student ["P3"]

    average = math.ceil ((p1 + p2 + p3) / 3)            # "math.ceil" rounds the result up
    return average

def Situation (Student):                                # returns the situation of the students
    if Student["Absences"] > 15:
        return "Reprovado por Falta"

    if Student["Average"] >= 70:
        return "Aprovado"

    if Student["Average"] >= 50:
        return "Exame Final"

    return "Reprovado por Nota"

def NAF (Student):                                      # returns grade for final approval
    naf = 100 - Student["Average"]
    if naf <= 50:
        return naf

    return 0

def Logs (Student):                                     # prints the log lines
    print ("(log)")
    print ("Name:", Student["Name"])
    print ("P1 =", Student["P1"])
    print ("P2 =", Student["P2"])
    print ("P3 =", Student["P3"])
    print ("Absences =", Student["Absences"])
    print ("Average =", Student["Average"])
    print ("Situation:", Student["Situation"])
    print ("NAF =", Student["NAF"])
    print ("\n")

def Update_spreadsheet (Student, row):
    worksheet.update_cell (row+1, 7, Student["Situation"])           # updates the cell with the situation
    worksheet.update_cell (row+1, 8, Student["NAF"])                 # updates the cell with the grade for final approval





Student = {}                                                         # object where the data will be stored

spreadsheet = worksheet.get_all_values()                             # get the entire spreadsheet
max_row = len (spreadsheet)                                          # finds out how many lines there are

for row in range (3, max_row):
    row_data = spreadsheet[row]

    Student ["Name"] = row_data[1]                                   # updates the student object with current data
    Student ["P1"] = int (row_data[3])
    Student ["P2"] = int (row_data[4])
    Student ["P3"] = int (row_data[5])
    Student ["Average"] = Average (Student)
    Student ["Absences"] = int (row_data[2])         
    Student ["Situation"] = Situation (Student)
    Student ["NAF"] = NAF (Student)

    Update_spreadsheet (Student, row)

    Logs (Student)   

    row = row + 1                                                   # increment the row to calculate the next student



print ("End")