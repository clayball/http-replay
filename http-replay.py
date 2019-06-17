#!/usr/bin/env python3

import sys
import shutil
import tempfile
import urllib.request
from urllib.error import URLError, HTTPError

""" 
Example usage:
"""

#hphost = "https://www.bing.com"
hphost = sys.argv[1]
#hpport = 80
hpurlpath = "/"
hpfilepath = ""
hpreq = hphost + hpurlpath + hpfilepath

user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) Black Mirage'
origin = 'blackmirage.sh'

#values = {'name': 'Fred',
#          'location': 'Europe',
#          'language': 'Python' }

#data = urllib.parse.urlencode(values)
#data = data.encode('ascii')

headers = {'User-Agent': user_agent,
           'Origin': origin}

print('[*] Sending request.. ')
print('[*]     host: ', hphost)
print('[*]     request: ', hpreq)

req = urllib.request.Request(hpreq, None, headers)

try:
    with urllib.request.urlopen(req) as response:
        the_page = response.read()
        # We may want the ability to save the page to a temporary file.
        #with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
        #    shutil.copyfileobj(response, tmp_file)
except HTTPError as e:
    print('[-] The server couldn\'t fulfill the request.')
    print('[-] Error code: ', e.code)
except URLError as e:
    print('[-] We failed to reach a server.')
    print('[-] Reason: ', e.reason)
else:
    # everything is fine
    print('[*] Success')
    response_headers = response.getheaders()
    response_status = response.status

if response_status == 200:
    print('[*] STATUS: 200')
    print('[*] Response Headers:', response_headers)

#with open(tmp_file.name) as html:
#    pass
