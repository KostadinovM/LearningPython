#Appending Files
appendMe = '\nNew bit of information'

appendFile = open('exampleFile.txt', 'a')       #'a' refers to append                         #for a new line
appendFile.write(appendMe)
