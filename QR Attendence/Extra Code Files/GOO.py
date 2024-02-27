file1 = open(r"C:\Users\VK\Desktop\TETD.txt", "r")
var = file1.readlines()
count = 0

for i in var:

    count = 0
    for y in i:
        if y == "P":
            count = count + 1
            if count == 1:
                file2 = open(r"C:\Users\VK\Desktop\TOO.txt", "a")
                print(i)
                file2.write(i)
                file2.flush()




