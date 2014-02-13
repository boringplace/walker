import urllib.request
import ftplib

responses_ok = {
    200: ('OK', 'Request fulfilled, document follows'),
    201: ('Created', 'Document created, URL follows'),
    202: ('Accepted',
          'Request accepted, processing continues off-line'),
    203: ('Non-Authoritative Information', 'Request fulfilled from cache'),
    204: ('No Content', 'Request fulfilled, nothing follows'),
    205: ('Reset Content', 'Clear input form for further input.'),
    206: ('Partial Content', 'Partial content follows.'),
    }

def exists(url):    
    url_resource = url.split('rsync://')[1]
    try:
        response = urllib.request.urlopen('http://'+url_resource)
        code = response.getcode()
        if responses_ok[code]:
            return 'http://'+url_resource 
    except urllib.error.HTTPError:
        print("HTTP is not available; trying FTP")
        remote = ftplib.FTP(url_resource)
        remote.login()
        try:
            remote.cwd(path)
            return "ftp://" + url_resource 
        except ftplib.error_perm:
            print("sorry, resourcse is not available")
            return False