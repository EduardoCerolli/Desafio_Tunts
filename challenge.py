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

def Situation (average, absences):                      # returns the situation of the students
    if absences > 15:
        return "Reprovado por Falta"

    if average >= 70:
        return "Aprovado"

    if average >= 50:
        return "Exame Final"

    return "Reprovado por Nota"

def NAF (average):                                      # returns grade for final approval
    naf = 100 - average
    return naf

def Logs (Student, absences, average, situation, naf):  # prints the log lines
    name = Student["Name"]
    p1 = Student["P1"]
    p2 = Student["P2"]
    p3 = Student["P3"]
    print ("(log)")
    print ("Name:", name)
    print ("P1 =", p1)
    print ("P2 =", p2)
    print ("P3 =", p3)
    print ("Absences =", absences)
    print ("Average =", average)
    print ("Situation:", situation)
    print ("NAF =", naf)
    print ("\n")





Student = {}                                            # object where the data will be stored

row = 4                                                 # row that starts the necessary data
spreadsheet = worksheet.get_all_values()                # get the entire spreadsheet
max_row = len (spreadsheet)                             # finds out how many lines there are

for x in range (3, max_row):
    current_row = spreadsheet[x]

    name = current_row[1]

    p1 = int (current_row[3])                           # get the test notes
    p2 = int (current_row[4])
    p3 = int (current_row[5])

    Student ["Name"] = name                             # updates the student object with current data
    Student ["P1"] = p1
    Student ["P2"] = p2
    Student ["P3"] = p3

    average = Average (Student)
    
    absences = int (current_row[2])                     # get the number of absences

    situation = Situation (average, absences)

    if situation == "Exame Final":
        naf = NAF (average)
    else:
        naf = 0

    worksheet.update_cell (row, 7, situation)           # updates the cell with the situation
    worksheet.update_cell (row, 8, naf)                 # updates the cell with the grade for final approval

    Logs (Student, absences, average, situation, naf)   

    row = row + 1                                       # increment the row to calculate the next student


print ("End")