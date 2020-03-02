# FiioM6PlaylistAdaptUpload
A simple Python script that converts Windows-like paths to Unix, then uploads via FTP.

## Usage
Set hostAddress, hostPort, username, password, original file name, processed file name (which will appear on your device), the directory where to upload the playlist file. 
You'll also need to adjust the Windows path to the Unix one that the Fiio accepts.
Fire up an FTP server on your device (I use MiXplorer), then run the script.
