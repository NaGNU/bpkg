from varbpkg import *
import json

listpath = "/var/bpkg/db/" + repo + "/pkglist.json"
print(listpath)
file = open(listpath, "r")
pkgs = json.load(file)

i = 0
while i < len(pkgs['packages']):
    print(pkgs['packages'][i])
    i += 1


