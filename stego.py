import cv2
import os
import string

#Encryption

img = cv2.imread("C:/Users/POOJASHREE/Desktop/PYTHON/IBM_project/img.jpg") #filepatgh

msg = input("Enter your secret message:")

password = input("Enter a password:")

d={}      #two dict to store the ascii value of the characters and initialize the pixcel value of the image
c={}

for i in range(255):          #for loop for iterate the ascii valueof the characters
    d[chr(i)]=i
    c[i]=chr(i)

m=0        # 3 variables for RGB
n=0
z=0

for i in range(len(msg)):
    img[n,m,z]=d[msg[i]]
    n=n+1
    m=m+1
    z=(z+1)%3

cv2.imwrite("Encryptedmsg.jpg",img)

os.system("start Encryptedmsg.jpg")


#Decryption

message=""      #to store the decrypted message

n=0
m=0
z=0

pas = input("Enter password for Decryption:")
if password == pas :
    for i in range(len(msg)):
        message = message + c[img[n,m,z]]
        n=n+1
        m=m+1
        z=(z+1)%3
    print("Decryptedmsg",message)
else:
    print("password not valid")

