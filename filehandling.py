# import os
# os.remove("sample.txt")
# f = open("sample.txt","r+")
# data = f.read()
# print(data)

# newdata = data.replace("Java","Python")

# print(newdata)


# f.write(newdata)

# index =  data.find("learning")

# print("learning was found") if index != -1 else print("learning wasn't found")

# f.close()



def check_lines():
    word = "learning"
    with open("sample.txt","r") as f:
        count = 0
        for line in f:
            index = line.find(word)
            if index != -1:
                print(count)
                return
            count += 1
        print("not found")




check_lines()




            
