from google.colab import auth
auth.authenticate_user()
import requests
import gspread
from oauth2client.client import GoogleCredentials
import pandas as pd

gc = gspread.authorize(GoogleCredentials.get_application_default())

sheetname="enrollment" # Enter Sheet name without using extention
sh = gc.open(sheetname)
worksheet = sh.sheet1
values_list = worksheet.get_all_values()
df = pd.DataFrame(values_list)
df.head()