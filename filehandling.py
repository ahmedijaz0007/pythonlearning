# import os
# os.remove("sample.txt")
f = open("sample.txt","r+")
data = f.read()
print(data)

newdata = data.replace("Java","Python")

print(newdata)


f.write(newdata)

index =  data.find("learning")

print("learning was found") if index != -1 else print("learning wasn't found")

f.close()




