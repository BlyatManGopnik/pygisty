import json
import sys
import requests

def post(authtoken, content, filename):
    print("Uploading " + filename)
    jsondata = "{\"files\": {\""+filename.strip("\n")+"\": {\"content\": \""+content+"\"}}}"
    header = {'User-Agent': "pygisty", "Authorization": "token "+authtoken, "Accept": "application/json"}
    r = requests.Session()
    r.headers.update(header)
    request = r.post("https://api.github.com/gists", data=jsondata)
    dat = json.loads(request.text)
    try:
        error = dat["message"]
        print("Error: " + error)
        sys.exit(1)
    except KeyError:
        test = ""
    html = dat["html_url"]
    return html