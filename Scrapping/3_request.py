import requests
res = requests.get("https://www.google.com")
res.raise_for_status()
print(len(res.text))

with open('mygoogle.html',"w",encoding="utf8") as f:
    f.write(res.text)
