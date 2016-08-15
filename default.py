#!/usr/bin/python
# -*- coding: utf-8 -*-

import xbmc
import xbmcaddon
import xbmcgui
import xbmcplugin
import urllib
import os.path
from schlafschafCore import SchlafschafCore

#import ptvsd
#ptvsd.enable_attach(secret = 'm')
#ptvsd.wait_for_attach()

addonID = 'plugin.video.schlafschaf'
addon = xbmcaddon.Addon(id=addonID)
addon_handle = int(sys.argv[1])
addonDir = xbmc.translatePath(addon.getAddonInfo('path'))
icon = os.path.join(addonDir ,'fanart.jpg')
xbmcplugin.setContent(addon_handle, "movies")
path = os.path.dirname(os.path.realpath(__file__))
addonID = os.path.basename(path)
videoquality = (int)(addon.getSetting("videoquality"))

def addDir(title, stream, thumb, mode):
    link = sys.argv[0]+"?url="+urllib.quote_plus(stream)+"&mode="+str(mode)
    liz = xbmcgui.ListItem(title, iconImage=None, thumbnailImage=thumb)
    liz.setInfo(type="Video", infoLabels={"Title": title})
    return xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=link, listitem=liz, isFolder=True)

def addLink(name, url, mode, iconimage, date):
    u = sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+urllib.quote_plus(mode)
    ok = True
    liz = xbmcgui.ListItem(name, iconImage=icon, thumbnailImage=iconimage)
    liz.setInfo(type="Video", infoLabels={"Title": name, "Tagline": date})
    liz.setProperty("fanart_image", icon)
    liz.setProperty('IsPlayable', 'true')
    ok = xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=u, listitem=liz)
    return ok

def parameters_string_to_dict(parameters):
	paramDict = {}
	if parameters:
		paramPairs = parameters[1:].split("&")
		for paramsPair in paramPairs:
			paramSplits = paramsPair.split('=')
			if (len(paramSplits)) == 2:
				paramDict[paramSplits[0]] = paramSplits[1]
	return paramDict

params = parameters_string_to_dict(sys.argv[2])
mode = urllib.unquote_plus(params.get('mode', ''))
url = urllib.unquote_plus(params.get('url', ''))
name = urllib.unquote_plus(params.get('name', ''))

def notification(text):
    xbmc.executebuiltin('Notification(%s, %s, %d, %s)'%(addonID, text, 4500, icon))

def listVideos():
    sc = SchlafschafCore()
    data = sc.getSchlafschafData()
    if (len(sc.error) > 0):
        notification(sc.error)
        return
    x = 0
    for x in range(0,len(data[0])):
        addLink(data[1][x] + " - " + data[0][x], data[2][x], 'playVideo', data[3][x], data[1][x])
    xbmcplugin.endOfDirectory(addon_handle)

def playVideo(url):
    sc = SchlafschafCore()
    vLink = sc.getDataFromLink(url, videoquality)
    if (len(sc.error) > 0):
        notification(sc.error)
        return
    listitem = xbmcgui.ListItem(path=vLink)
    xbmcplugin.setResolvedUrl(addon_handle, True, listitem)


if mode == "playVideo":
    playVideo(url)
else:
    listVideos()
