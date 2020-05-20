#convert_to_text_file.py

f1 = open("temp1.txt", "r")

temp = f1.read()
temp = temp.split("\n")

f1.close()

f = open("man.txt", "a")

index = 0

for name in temp:
    f.write("%05d,%s\n" %(index, name))
    index += 1

f.close()

print("Task's done!")
