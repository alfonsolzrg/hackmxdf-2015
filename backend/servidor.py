# -*- coding: UTF-8 -*-
import socket
import urls
import sys
from extraexceptions import NotEnoughArgsError, BadRequestError, VersionNotSupportedError, NotImplementedError

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.bind(('',80))
socket.listen(1)
print "listening on port 80\n"

LOCATION = "www"
NOT_FOUND_LOCATION = "www/404.html"
INTERNAL_SERVER_LOCATION = "www/500.html"
NOT_IMPLEMENTED_LOCATION = "www/501.html"
NOT_ENOUGH_ARGS_LOCATION = "www/500args.html"
BAD_REQUEST_LOCATION = "www/400.html"
ACCESS_CONTROL = "Access-Control-Allow-Origin: * \r\n"
CRLF = "\r\n"

def parsea(HTTPString):
    HTTP_string_len = len(HTTPString.split(CRLF))
    
    if len(HTTPString.split(CRLF)) <= 2:
        headers = "HTTP/1.1 400 Bad Request syntax \r\n"
        file = open(BAD_REQUEST_LOCATION)
        print headers
        headers = headers + ACCESS_CONTROL + CRLF
        response = headers + file.read() + CRLF
        client.send(response)
        return

    parse = HTTPString.split(CRLF)[0]
    print parse
    method = ''
    URI = ''
    version = ''

    try:
        method = parse.split(' ')[0]
        URI = parse.split(' ')[1]
        version = parse.split(' ')[2]
    except IndexError:
        headers = "HTTP/1.1 400 Bad Request syntax \r\n"
        file.open(BAD_REQUEST_LOCATION)
        print headers
        headers = headers + ACCESS_CONTROL + CRLF
        response = headers + file.read() + CRLF
        client.send(response)
        return

    try:

        if version != "HTTP/1.1":
            raise VersionNotSupportedError()

        if method == "POST" :
            raise NotImplementedError()

        elif (method == "PUT" or method == "DELETE" or method == "HEADER"):
            raise NotImplementedError()
        elif HTTPString.split(CRLF)[HTTP_string_len-1] != "":
            raise BadRequestError()

        if method == "GET" :
            serveGET(URI[1:])

    except BadRequestError:
        headers = "HTTP/1.1 400 Bad Request syntax \r\n"
        file = open(BAD_REQUEST_LOCATION)
        print headers
        headers = headers + ACCESS_CONTROL + CRLF
        response = headers + file.read() + CRLF
        client.send(response)
        return

    except VersionNotSupportedError:
        headers = "HTTP/1.1 505 HTTP Version Not Supported \r\n"
        print headers
        headers = headers + ACCESS_CONTROL + CRLF
        client.send(headers)
        return

    except NotImplementedError:
        headers = "HTTP/1.1 501 Not Implemented \r\n"
        file = open(NOT_IMPLEMENTED_LOCATION)
        print headers
        headers = headers + ACCESS_CONTROL + CRLF
        response = headers + file.read() + CRLF
        client.send(response)
        return


def serveGET(URL):
    try :

        try:
            args = URL.split('?')[1]
        except:
            args = None

        URL = URL.split('?')[0]
        fileLocation = LOCATION + URL
        response = "HTTP/1.1 200 OK \r\n"
        response = response + ACCESS_CONTROL
        contentType = "Content-Type: text/html ; charset=UTF-8\r\n"

        if URL in urls.get_urls:
            callback = urls.get_urls[URL]
            if args:
                args = parseArgs(args)
            result = callback(args);
            if result:
                client.send(response + CRLF + result + CRLF)
            else:
                raise IOError()
            return

        elif URL == "/":
            fileLocation = LOCATION + "/index.html"
        elif ".css" in URL :
            contentType = "Content-Type: text/css\r\n"
        elif ".js" in URL :
            contentType = "Content-Type: application/javascript\r\n"
        elif ".jpg" in URL :
            contentType = "Content-Type: image/jpeg\r\n"

        file = open(fileLocation)
        response = response+contentType+CRLF+file.read()+CRLF
            
        client.send(response)

    except NotImplementedError:
        headers = "HTTP/1.1 501 Not Implemented \r\n"
        file = open(NOT_IMPLEMENTED_LOCATION)
        print headers
        headers = headers + ACCESS_CONTROL + CRLF
        response = headers + file.read() + CRLF
        client.send(response)
        return

    except NotEnoughArgsError as e:
        headers = "HTTP/1.1 500 Not Enough Arguments \r\n"
        print headers
        headers = headers + ACCESS_CONTROL + CRLF
        result = prepareNotEnough(e.functName)
        response = headers + result + CRLF
        client.send(response)
        return

    except IOError:
        file = open(NOT_FOUND_LOCATION)
        headers = "HTTP/1.1 404 Not Found \r\n"
        print headers
        headers = headers + ACCESS_CONTROL + CRLF
        response = headers + file.read() + CRLF
        client.send(response)
        return


def prepareNotEnough(funct):
    file = open(NOT_ENOUGH_ARGS_LOCATION)
    fileString = file.read()
    fileString = fileString.split('{{')
    response = fileString[0] + funct + fileString[1].split('}}')[1] + CRLF
    return response


def parseArgs(args):
    args = args.split("&")
    parsed_args = {}

    for x in args:
        result = x.split("=")
        parsed_args[result[0]] = result[1]

    return parsed_args


try:
    while True:
        client, address = socket.accept()
        data = client.recv(4096)
        parsea(data)
        client.close()

except KeyboardInterrupt:
    print "\nCerrando socket y finalizando"
    socket.close()
    print "\nAdios!"
    sys.exit()

except socket.error:
    print "\nCerrando socket y finalizando"
    socket.close()
    print "\nAdios!"
    sys.exit()