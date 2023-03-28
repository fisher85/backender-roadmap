# Support HTTP2


## Generate certs

openssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -days 365 -nodes -config "C:\Program Files\Git\usr\ssl\openssl.cnf"