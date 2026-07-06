# creating files -> use with method beacuse this closes file automatically.
with open("file.txt", "r") as file: # can give full location or only file name
    print(file.read())

#                                               Read Methods

# 1) Read entire file -> file.read()
# 2) Read first n characters -> file.read(10)
# 3) Read one line -> file.readline()
# 4) Read all lines into a list -> file.readlines()
# 5) Read file using a loop -> for line in file:print(line)

#                                              Write Methods

# 1) Write text -> file.write("Hello")
# 2) Write multiple lines
    # lines = ["Ali\n", "Sara\n"]
    # file.writelines(lines)

#                                          File Positioning Methods

# 1) Current position ->file.tell()
# 2) Move cursor -> file.seek(0) , file.seek(10)

#                                            Check File Properties

# 1) Is file closed? -> file.closed
# 2) File mode -> file.mode
# 3) File name -> file.name


#                                               File Modes

# Mode	Meaning
# "r"	Read
# "w"	Write (overwrite/create)
# "a"	Append
# "x"	Create (error if exists)
# "r+"	Read & Write
# "w+"	Write & Read (overwrite)
# "a+"	Append & Read
# "rb"	Read binary
# "wb"	Write binary
# "ab"	Append binary
# "rb+"	Read & Write binary

#                                           OS Methods

# 1) Check existence -> os.path.exists("file.txt")
# 2) Delete file -> os.remove("file.txt")
# 3) Rename file -> os.rename("old.txt", "new.txt")

