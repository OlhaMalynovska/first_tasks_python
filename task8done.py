
original_String = " name=Amanda=sssss&age=32&&salary=1500&currency=euro "
print("The original string is ",original_String)
items = original_String.split('&')
dict = {}
for i in items:
    a = i.split('=')
    if len(a) > 1:
        key = a[0].strip()
        val = a[1].strip()
        dict[key] = val
print(dict)