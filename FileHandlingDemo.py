# 🔹 FILE CREATE + WRITE
with open("student.txt", "w") as file:
    file.write("Name: Hanny\n")
    file.write("Course: BCA\n")

print("File created and data written successfully\n")


# 🔹 FILE APPEND (new data add karega)
with open("student.txt", "a") as file:
    file.write("City: Kashipur\n")

print("Data appended successfully\n")


# 🔹 FILE READ (full content)
with open("student.txt", "r") as file:
    content = file.read()
    print("Full File Content:\n")
    print(content)


# 🔹 FILE READ LINE BY LINE
print("Reading line by line:\n")

with open("student.txt", "r") as file:
    for line in file:
        print(line.strip())