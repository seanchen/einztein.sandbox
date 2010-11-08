#! /usr/bin/env python

# query.py

__doc__ = """A simple Python code to demonstrate Einztein.com query APIs"""
__docformat__ = 'plaintext'

import urllib
import urllib2
import optparse
import simplejson as json

def query(auth_key, query_string):

    """
    perform a simple query based for the given string.
    """

    query_pattern = 'http://www.einztein.com/api/v1/courses.json?query=%s&key=%s'
    query = urllib.quote(query_string)

    query_url = query_pattern % (query, auth_key)
    json_response = urllib2.urlopen(query_url)
    query_result = json.loads(json_response.read())

    # return the search result in JSON format.
    return query_result

def format_json_result(json_result):

    """
    print out the json result nicely.
    """

    index = 0
    for item in json_result:
        index = index + 1
        print "==========="
        print "Course %d" % index
        print "==========="
        for each in item.iteritems():
            print '%s: %s' % (each[0], each[1])
    
    print "------------------------------------------------"
    print 'found %d courses in total' % index

def main():

    """
    the main entry for this query script.
    """

    cli_parser = optparse.OptionParser()
    cli_parser.add_option('-k', '--key', dest='auth_key', 
                          help='Specify your Einztein API key')

    # set the usage message.
    cli_parser.set_usage('%prog [options] SEARCH_STRING')

    # parse the arguments from command line.
    options, args = cli_parser.parse_args()

    if options.auth_key is None or args == []:
        cli_parser.print_help()
        return

    ret = query(options.auth_key, args[0])
    format_json_result(ret)

if __name__ == "__main__":
    main()
