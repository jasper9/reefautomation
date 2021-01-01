import urllib2
import xmltodict
import pprint
import blynklib

BLYNK_AUTH = "xxxx"
blynk = blynklib.Blynk(BLYNK_AUTH)
blynk.run()

print("Reading from Apex...")

file = urllib2.urlopen('http://x.x.x.x/cgi-bin/status.xml')
data = file.read()
file.close()

data = xmltodict.parse(data)
#pprint.pprint(data)

#print(data['status']['probes']['probe'][0])
#print(data['status']['probes']['probe'][1])


#quasi case statement to match 'Name' to a specific pin number of my choosing
pin = {'Tmp' : 20,
           'pH' : 21,
           'ORP': 22,
           'Salt': 23,
           'Alkx3': 24,
           'Cax3': 25,
           'Mgx3': 26
}

print("Writing to Blynk...")

#blynk.virtual_write(temp_29_pin, temp_29)
for probe in data['status']['probes']['probe']:
    if probe['name'] in pin:
        print(probe['name'] + ': ' + probe['value'])
        blynk.virtual_write(pin[probe['name']], probe['value'])
