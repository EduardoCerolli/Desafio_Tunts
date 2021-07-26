import gspread          # library to use the sheets API 
import math             # library to use the function ceil


gc = gspread.service_account (filename = 'service_account.json')        # setting the credentials file
sh = gc.open_by_url ('https://docs.google.com/spreadsheets/d/1HLNVnAsUohEVQUas9SLWDQuE_N_mZWVg0JqBhbuqAsc/edit#gid=0')      # setting the spreadsheet link
worksheet = sh.sheet1           # setting the spreadsheet page
