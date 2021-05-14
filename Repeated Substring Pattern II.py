#14/05/2021
#same as Repeated Substring Pattern just gets no input substring to test against.
string = input("input string: ")
inside = "false"
for i in range(1,len(string)):
    substring =  string[0:i]
    _ = ""
    while len(_) < len(string) and len(_) != len(string):
        _ += substring
    if _ == string:
        inside = "true"
        break
if inside == "true":
    print(f"{inside}, substring is {substring}")
if inside == "false":
    print("false")
