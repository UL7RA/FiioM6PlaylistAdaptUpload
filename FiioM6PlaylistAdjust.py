from ftplib import FTP
from os import remove
from sys import exc_info

hostAddress = "192.168.1.115"
hostPort = 2121
username = "UL7RA"
password = ""
original = "Trippy.m3u8"
directory = "Playlists"

processed = "Processed.m3u8"
originalPlaylist = open(original,"r")
processedPlaylist = open(processed,"w")

for line in originalPlaylist:
    proc = str(line)
    proc = proc.replace("Z:\Torrents\\","/storage/external_sd/")
    proc = proc.replace("\\","/")
    processedPlaylist.write(proc)

originalPlaylist.close()
processedPlaylist.close()

try:
    playlistBinary = open(processed,"rb")
    connection = FTP()
    connection.connect(hostAddress,hostPort)
    if username:
        connection.login(username,password)
        print("Logged in succesfully!")
    if directory:
        connection.cwd(directory)
        print("Changed directory to %s"%(directory))
    connection.storbinary("STOR %s" %(original),playlistBinary,1024)
    connection.close()
    playlistBinary.close()
    print("Success!")
except:
    exc = exc_info()[0]
    print("Error: {}".format(exc))

try:
    remove(processed)
except:
    exc = exc_info()[0]
    print("Could not delete file! Error: %s"%(exc))
