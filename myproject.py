import zipfile
import pyminizip
import os
import hashlib
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from google_drive_downloader import GoogleDriveDownloader as gdd


#Configuring authentication with GoogleDrive
gauth = GoogleAuth()
drive = GoogleDrive(gauth)

#creating the file txt file
f = open("path", mode="w")
with open("hello.txt", "w") as f :
    f.write("A plane text file")
f.close()

#compress the txt file - create protected zipped file
password = "Aa123456"
inpt = "./hello.txt"
oupt = "./backup.zip"
com_lvl = 5
pyminizip.compress(inpt, None, oupt,password, com_lvl)

# upload_file_list = ['backup.zip']

# gfile = drive.CreateFile({'parents': [{
# #     'id': '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'
# # }]})
#upload the file into google drive
gfile = drive.CreateFile()
print (gfile)
gfile.SetContentFile('./backup.zip')
gfile.Upload()

#check if the folder already exists
if ('varonis-folder' not in os.listdir(os.curdir)):
    os.mkdir('./varonis-folder')



#change the os dir to be what i have chosed
os.chdir("varonis-folder")
gfile.GetContentFile('./backup.zip')
retval=os.getcwd()
print ("Directory is %s" % retval)

newinput="backup.zip"
my_dir="./"
password = "Aa123456"
newcom_lvl=0
pyminizip.uncompress(newinput,password,my_dir,newcom_lvl)

#get the hash of the file we unzipped
with open("./hello.txt","rb") as f:
    f_byte= f.read()
    result = hashlib.sha256(f_byte)
    print(result.hexdigest())

#enter the hash into a newfile
new_f = open("path", mode="w")
with open("the_hash.txt", "w") as new_f :
    new_f.write(result.hexdigest())
new_f.close()


#upload the new hash file into google drive
gfile = drive.CreateFile()
print (gfile)
gfile.SetContentFile('./the_hash.txt')
gfile.Upload()

