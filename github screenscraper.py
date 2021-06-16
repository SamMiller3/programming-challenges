import urllib.request
print(len('h2 class="f4 text-normal mb-2">'))
website = urllib.request.urlopen('https://github.com/IronHead43')
website = website.read()
i=0
website = str(website)
while True:
    if website[i:i+32] == '<h2 class="f4 text-normal mb-2">':
        print("t")
        i+=40
        _ = ""
        while True:
            if website[i] != "\\":
                _ = _ + website[i]
            else:
                i+=1
            i+=1
            if str(website[i]) == "<":
                break
        website = _
        break
            
    i+=1
print(website)
