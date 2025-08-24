from datetime import datetime

filename = input("Enter the name of the file: ")
try:
    with open(filename, 'r') as f:
        content = f.read()
    print("File exists!")
except FileNotFoundError:
    print("Error: File not found. \nCreating File Instead")
finally:
    with open(filename, 'a') as f:
            f.write(f"Modified at {datetime.now()}")
