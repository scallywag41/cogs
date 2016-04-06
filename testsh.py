from sh import ping, nslookup, whois

bob = "stillsentry.com"
print(nslookup(bob))
print(whois(bob))
