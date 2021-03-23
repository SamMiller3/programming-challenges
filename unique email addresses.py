#unique email addresses, 23/03/2021
while True:
    emails = input("emails: ")
    emails = emails.split()
    duplicates = list()
    i = 0
    while i < len(emails):
        if emails[i] in duplicates:
            emails.pop(i)
            i-=1
        else:
            duplicates.append(emails[i])
        i+=1
    print(len(emails))
