
# query.py

__doc__ = """A simple Python code to demonstrate Einztein.com query APIs"""
__docformat__ = 'plaintext'

import urllib
import urllib2
import simplejson as json

query_pattern = 'http://www.einztein.com/api/v1/courses.json?query=%s&key=%s'
query = urllib.quote('YOUR QUERY STRING HERE')
key = 'YOUR EINZTEIN.COM API KEY HERE'
query_url = query_pattern % (query, key)
json_response = urllib2.urlopen(query_url)
query_result = json.loads(json_response.read())

index = 0
for item in query_result:
    index = index + 1
    print "==========="
    print "Course %d" % index
    print "==========="
    for each in item.iteritems():
        print '%s: %s' % (each[0], each[1])

print "------------------------------------------------"
print 'found %d courses in total' % index

