#pytube library

#syntax:
        #con=pytube.Youtube("url")

import pytube
con=pytube.YouTube("hhttps://www.youtube.com/shorts/paRXS3IxX0U")
print(con.streams)#list all available formats of gievn url
con.streams[0].download()
print('downloaded')
