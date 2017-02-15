try:
    f = open("Illus/README.md", "r")
except IOError:
    f = open("README.md", "r")
print "Welcome to Illus\n\n"
print '\n'.join(f.readlines())
f.close()


import Illus

