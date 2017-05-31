import requests, re, sys,os, random

class portRange:
	lower = None
	upper = None
	ports = None

	def __init__(self,lower,upper):
		self.lower = lower
		self.upper = upper
		self.ports = int(upper) - int(lower)

	def printRange(self):
		print "%s - %s (%s ports)" % (self.lower,self.upper, self.ports)


limit = int(sys.argv[1]) if len(sys.argv) == 2 else 1
print "Looking for %s contiguous unassigned ports..." % limit
print "Downloading current IANA port list..."
url = "http://www.iana.org/assignments/service-names-port-numbers/service-names-port-numbers.txt"
pattern = "([0-9]{5})-([0-9]{5})"

r = requests.get(url)
print "OK"
data = r.content
buff = iter(data.splitlines())

ports = []
for line in buff:
	if "Unassigned" in line:
		m = re.search(pattern,line)
		if(m):
			p = portRange(m.group(1), m.group(2))
			if p.ports >= limit:
				ports.append(p)

max = len(ports)
min = 0
pointer = random.randint(min,max)
p=ports[pointer]
print "Randomly selected candidate port range:"
p.printRange()			