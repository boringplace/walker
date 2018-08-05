import requests
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


def exists(url, directories):
    url_resource = url.split('rsync://')[1]
    try:
        response = requests.get('http://' + url_resource)
        if responses_ok[response.status_code]:
            return 'http://' + url_resource
    except urllib.error.HTTPError:
        print("HTTP is not available; trying FTP")
        remote = ftplib.FTP(url_resource)
        remote.login()
        try:
            for d in directories:
                remote.cwd(d)
                remote.cwd('..')
            return "ftp://" + url_resource
        except ftplib.error_perm:
            print("sorry, resourcse is not available")
            return False
