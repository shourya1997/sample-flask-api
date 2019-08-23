import requests
from datetime import datetime
date = str(datetime.today().date())
time = str(datetime.today().time())
clid = 'Hi'
number = 1000
r = requests.post("http://localhost:5000/params", data={'uid': 1, 'node_id':2, 'date':date, 'time':time, 'clid':clid, 'input':number})
# And done.
# print(r.text) # displays the result body.