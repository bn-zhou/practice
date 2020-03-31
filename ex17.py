from sys import argv
from os.path import exists

script, form_file, to_file = argv

print ("Copying from", form_file,"to",to_file)

#we could do these two on one line too, how?
input = open (form_file)
indate = input.read()

print ("The input file is",len(indate),"bytes long")

print ("Does the output file exists?", exists(to_file))
print ("Read, hit RETURN to continue, CTRL-C to abort.")


output = open (to_file, "w")
output.write(indate)

print ("Alright, all done.")
output.close()
input.close()
