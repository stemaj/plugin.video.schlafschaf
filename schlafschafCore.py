#!/usr/bin/python
# -*- coding: utf-8 -*-

from stemajUrl import *

class SchlafschafCore(object):

    def __init__(self, *args, **kwargs):
        return super(SchlafschafCore, self).__init__(*args, **kwargs)

    def __str__(self):
        return super(SchlafschafCore, self).__str__()

    error = "";

    def getSchlafschafData(self):
        urlBase = "https://www.erf.de"
        urlMain = urlBase + "/fernsehen/mediathek/schlafschaf-tv/6710-0"

        stUrl = StemajUrl()
        dataMain = stUrl.getUrl(urlMain)

        self.error = stUrl.error;
        if len(self.error) > 0:
            return;

        articles = splitStartingFrom(dataMain, "article ")

        links =[]
        imgs =[]
        titles=[]
        datums=[]

        for article in articles:
            links.append(urlBase + re.compile("<a href=\"(.+?)\"><img", re.DOTALL).findall(article)[0])
            imgs.append(urlBase + re.compile("<img src=\"(.+?)\" alt=", re.DOTALL).findall(article)[0])
            titles.append(re.compile("Vorschaubild: (.+?)\" /></a>", re.DOTALL).findall(article)[0])
            datums.append(re.compile("<h3>(.+?)</h3>", re.DOTALL).findall(article)[0])

        return (titles, datums, links, imgs)


    def getDataFromLink(self, link, quality):

        stUrl = StemajUrl()
        dat = stUrl.getUrl(link)

        self.error = stUrl.error
        if len(self.error) > 0:
            return;

        url = "https://"
        frag = re.compile("\"og:video\" content=\"https://(.+?)_h264_1500kb.mp4", re.DOTALL).findall(dat)[0]
    
        if quality == 2:
            return url + frag + "_h264_1500kb.mp4"
        elif quality == 1:
            return url + frag + "_h264_750kb.mp4"
        else:
            return url + frag + "_h264_200kb.mp4"


#TEST
#url = "rtmpt://c14000-o.f.core.cdn.streamfarm.net/14000cina/mp4:ondemand/3492iptv/xx_erf_Mediathek/42_13_058_h264_200kb.mp4"
#url = "https://www.erf.de/erf-mediathek/sendungen-a-z/schlafschaf-tv/ein-neuer-juenger/6710-79"

#sc = SchlafschafCore()
#data = sc.getSchlafschafData()
#if (len(sc.error) == 0):
#    x = 0
#    for x in range(0,len(data[0])):
#        title = data[0][x]
#        time = data[1][x]

#sc.error = ""
#k = sc.getDataFromLink(url, 0)
#if (len(sc.error) == 0):
#    y = 0
