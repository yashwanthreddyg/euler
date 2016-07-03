from urllib.error import HTTPError, URLError

__author__ = 'Yashwanth Reddy'
import hashlib
import os
import urllib.request
import sys

def downloadSub(vidfullpath):
    #vidfullpath = "C:/Users/Yashwanth Reddy/Downloads/Drive (2011)/Drive.2011.720p.BrRip.x264.YIFY.mp4"
    if not isFileVid(vidfullpath) :
        print("File isn't a video");
        return
    hash = get_hash(vidfullpath)
    try:
        raw_file = get_file(hash)
    except HTTPError as h:
        if(h.code == 404):
            print("Subtitle not found :(")
        elif(h.code == 400):
            print("Something ain't right :(")
    except URLError as u:
        print("There's some problem with your internet...")
    except Exception as e:
        print("OOPS... something isn't right")
    else:
        savefile(raw_file,vidfullpath)

def savefile(file,path):
    print(path[:path.rfind('/')+1])
    outputfile = open(path[:path.rfind('.')]+'.srt','wb')
    outputfile.write(file)
    outputfile.close()

def get_file(hash):
    #response = urllib2.urlopen('http://www.example.com/')
    #html = response.read()
    header = dict()
    header["User-Agent"] = "SubDB/1.0"
    req = urllib.request.Request("http://api.thesubdb.com/?action=download&hash="+hash+"&language=en",None,header)
    response = urllib.request.urlopen(req)
    raw_file = response.read()
    return raw_file

def isFileVid(filepath):
    format = filepath[filepath.rfind('.'):]
    print('format: '+format)
    if format in [".avi", ".mp4", ".mkv", ".mpg", ".mpeg", ".mov", ".rm", ".vob", ".wmv", ".flv", ".3gp"] :
        return True
    return False;

def get_hash(name):
    readsize = 64 * 1024
    with open(name, 'rb') as f:
        size = os.path.getsize(name)
        data = f.read(readsize)
        f.seek(-readsize, os.SEEK_END)
        data += f.read(readsize)
    return hashlib.md5(data).hexdigest()

if __name__ == "__main__":
    vidfullpath = "F:/movie/matchstick men 2003 1080p brrip x264 yify/Matchstick.Men.2003.1080p.BluRay.x264.YIFY.mp4"
    if(len(sys.argv)<2):
        print("Too few argumetns")
    elif(len(sys.argv)>2):
        print("Too many arguments")
    else:
        try:
            downloadSub(vidfullpath)
        except Exception as e:
            print("OOPS... something isn't right")

    """print("args:")
    for arg in sys.argv:
        print(arg)"""
