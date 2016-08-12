#!/usr/bin/python
# -*- coding: utf-8 -*-

from stemajUrl import *

def reportError(err):
    i = 0

#url = "rtmpt://c14000-o.f.core.cdn.streamfarm.net/14000cina/mp4:ondemand/3492iptv/xx_erf_Mediathek/42_13_058_h264_200kb.mp4"
#url = "https://www.erf.de/fernsehen/mediathek/schlafschaf-tv/petrus-faengt-viele-fische/6710-37?PHPSESSID=f3584b851e25ae9d032a48de61028836"

def getSchlafschafData():
    urlBase = "https://www.erf.de"
    urlMain = urlBase + "/fernsehen/mediathek/schlafschaf-tv/6710-0"
    dataMain = getUrl(urlMain)

    if len(dataMain[1]) > 1:
        reportError(dataMain[1])

    data = splitStartingFrom(dataMain[0],"pageNavi");

    articles = splitStartingFrom(data[0], "article ")

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



def getDataFromLink(link, quality):

    dat = getUrl(link)

    if len(dat[1]) > 1:
        reportError(dat[1])

    url = "rtmpt://c14000-o.f.core.cdn.streamfarm.net/14000cina/mp4:ondemand/3492iptv/xx_erf_Mediathek/"
    spls = splitStartingFrom(dat[0], "xx_erf_Mediathek%2F")
    frag = cutEndingWith(spls[0], "_h264")
    
    if quality == 2:
        return url + frag + "_h264_1500kb.mp4"
    elif quality == 1:
        return url + frag + "_h264_750kb.mp4"
    else:
        return url + frag + "_h264_200kb.mp4"


#k = getDataFromLink(url, 2)
#data = getSchlafschafData()
#x = 0
#for x in range(0,len(data[0])-1):
#    title = data[0][x]
#    time = data[1][x]
