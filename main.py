
# Programme simple pour afficher la date et l'heure actuelles en Python

import datetime
now = datetime.datetime.now()
print ("Today is "+now.strftime("%Y-%m-%d and it is %H:%M:%S."))