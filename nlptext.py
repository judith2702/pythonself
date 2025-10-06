import requests
print "Hello World!"

r = requests.get("http://www.bing.com")
print "status code: ",r.status_code
