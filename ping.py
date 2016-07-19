import os
hostname = "goutamadwant.com"
response = os.system("ping -c 1 " + hostname)

if response == 0:
  print hostname, 'is up!'
else:
  print hostname, 'is down!'

hostname1 = "google.com"
response = os.system("ping -c 1 " + hostname1)

if response == 0:
  print hostname1, 'is up!'
else:
  print hostname1, 'is down!'


hostname2 = "adadasjkdhask.com"
response = os.system("ping -c 1 " + hostname2)

if response == 0:
  print hostname2, 'is up!'
else:
  print hostname2, 'is down!'