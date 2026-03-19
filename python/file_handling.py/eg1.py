print("write function")                #if file does not exixt writefile creates it , always mention the file type
f=open("newfile.txt", "w")
content= f.write("ONION\nTOMATO\nPOTATO")
  #print(content)
f.close()

#write() does NOT return text

#👉 It returns number of characters written

print("read function")
f=open("newfile.txt", "r")
content= f.read()
print(content)
f.close()

print("append function")
f=open("newfile.txt", "a")
f.write("\nCUCUMBER")
f.close()


f=open("newfile.txt", "r+")  #read and write mode but it clears the content of the file then write
content=f.read()
print(content)
f.close()