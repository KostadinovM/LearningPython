#Writing to File

text = 'Sample Text to Save\nNew line!'
saveFile = open('exampleFile.txt', 'w')     #which file to open and what to do(write)
                                            #if the file doesnt exist it wll be created
                                            #also clears whatever it has inside
saveFile.write(text)
saveFile.close()                            #always want to close to avoid trouble


