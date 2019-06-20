import requests
import json
import smtplib
from datetime import datetime
from datetime import timedelta  
mail_list = ["[RECIPIENT]", "[RECIPIENT]"] 
my_date = datetime.today()
my_total = 0
for i in range(1, 20):
    r = requests.get('https://www.doctolib.fr/availabilities.json?start_date='+ my_date.strftime('%Y-%m-%d') + '{RESTE DU LIEN API}')
    my_total = r.json()['total'] + my_total
    if my_total > 0:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.login("[EMAIL]@gmail.com", "[PASSWORD]")
        server.sendmail(
          "[EMAIL]@gmail.com", 
          mail_list, 
          "Il y a des RDV dispos")
        server.quit()
        break
    my_date = my_date + timedelta(weeks=1) 
