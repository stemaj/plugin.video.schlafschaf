#!/usr/bin/python
# -*- coding: utf-8 -*-

import urllib2
import re
import httplib

class StemajUrl(object):

    def __init__(self, *args, **kwargs):
        return super(StemajUrl, self).__init__(*args, **kwargs)

    def __str__(self):
        return super(StemajUrl, self).__str__()

    error = "";

    def getUrl(self, url):
        link = ''
        req = urllib2.Request(url, headers={'accept': '*/*'})
        req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; rv:19.0) Gecko/20100101 Firefox/19.0')
        try:
            response = urllib2.urlopen(req)
            if not response:
                self.error = 'No response - Please try again'
        except urllib2.HTTPError as e:
            self.error = "Error code: " + str(e.code)
        except urllib2.URLError as e:
            self.error = 'Reason: ', + str(e.reason)
        except Exception as e:
            if e.message:
                self.error = e.message
            else:
                self.error = 'Other reason'
        if not self.error:
            try:
                link = response.read()
                if not link:
                    self.error = 'No data - Please try again'
            except httplib.IncompleteRead as e:
                self.error = str(e.message)
            except Exception as e:
                self.error = str(e.message)
    
        if not self.error:
            if response:
                response.close()

        return link


"""Helper Functions"""
def splitStartingFrom(str, tag):

    newStr = str.split(tag);
    newStr.pop(0)
    return newStr

def cutEndingWith(str, tag):

    newStr = str.split(tag);
    return newStr[0]
