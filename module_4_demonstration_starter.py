try:
    file = open("module_4_data.txt", "r")
    data = file.readlines()
    1/0
    file.close()

    print("File Closed")

except FileNotFoundError as e:
    print("File does not exist", e)

except Exception as e:
    print("General exception", e)