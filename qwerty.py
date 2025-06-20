file1=open("sample.txt", "w")
w=file1.write("It is a sample text file. \nIt consist of multiple lines.")
print(w)
file1.close()

try:
    with open("sample.txt", 'r') as file:
        print("Reading file content:")
        for index, line in enumerate(file, start=1):
            print(f"Line {index}: {line.strip()}")
except FileNotFoundError:
    print(f"Error: The file '{"sample.txt"}' was not found.")


#----------------------------------------------------------------------

w2 = input("Enter text to write to the file: ")
with open("output.txt", "w") as file:
    file.write(w2 + "\n")
print("Data successfully written to output.txt.")

a = input("\nEnter additional text to append: ")
with open("output.txt", "a") as file:
    file.write(a + "\n")
print("Data successfully appended.")

print("\nFinal content of output.txt:")
with open("output.txt", "r") as file:
    r = file.read()
    print(r)












