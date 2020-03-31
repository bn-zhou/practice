from sys import argv

script,filename = argv

print ("We're going to erase ",filename, ".")
print ("If you don't want that, hit CTRL-C (^C).")
print ("If you do want that, hit RETURN")

input ("?")


print ("Opening the file ...")
target = open (filename, 'w')

print ("Truncating the file. Goodbye!")
target.truncate()

print ("Now, I'm going to ask you for three lines.")

line1 = input ("line1:")
line2 = input ("line2:")
line3 = input ("line3:")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)

target.close()
print ("And finally, we close it.")

