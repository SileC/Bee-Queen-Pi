import xbmcaddon

import os

#########################################################
#         Global Variables - DON'T EDIT!!!              #
#########################################################
ADDON_ID = xbmcaddon.Addon().getAddonInfo('id')
PATH = xbmcaddon.Addon().getAddonInfo('path')
ART = os.path.join(PATH, 'resources', 'media')
#########################################################

#########################################################
#        User Edit Variables                            #
#########################################################
ADDONTITLE = '[COLOR orangered]Al8inA [/COLOR] [COLOR chocolate]Matrix Wizard[/COLOR]'
BUILDERNAME = '[COLOR darkorange]Al8inA[/COLOR] '
EXCLUDES = [ADDON_ID, '']
# Text File with build info in it.
BUILDFILE = 'https://archive.org/download/builds19/buildfile.txt'
# How often you would like it to check for build updates in days
# 0 being every startup of kodi
UPDATECHECK = 0
# Text File with apk info in it.  Leave as 'http://' to ignore
APKFILE = 'http://'
# Text File with Youtube Videos urls.  Leave as 'http://' to ignore
YOUTUBETITLE = '[COLOR orangered]Youtube[/COLOR]'
YOUTUBEFILE = 'https://archive.org/download/builds19/youtube.txt'
# Text File for addon installer.  Leave as 'http://' to ignore
ADDONFILE = 'http://'
# Text File for advanced settings.  Leave as 'http://' to ignore
ADVANCEDFILE = 'http://'
#########################################################

#########################################################
#        Theming Menu Items                             #
#########################################################
# If you want to use locally stored icons the place them in the Resources/Art/
# folder of the wizard then use os.path.join(ART, 'imagename.png')
# do not place quotes around os.path.join
# Example:  ICONMAINT     = os.path.join(ART, 'mainticon.png')
#           ICONSETTINGS  = 'https://www.yourhost.com/repo/wizard/settings.png'
# Leave as http:// for default icon
ICONBUILDS = os.path.join(ART, 'builds.png')
ICONMAINT = os.path.join(ART, 'maintenance.png')
ICONSPEED = os.path.join(ART, 'speed.png')
ICONAPK = os.path.join(ART, 'apkinstaller.png')
ICONADDONS = os.path.join(ART, 'addoninstaller.png')
ICONYOUTUBE = os.path.join(ART, 'youtube.png')
ICONSAVE = os.path.join(ART, 'savedata.png')
ICONTRAKT = os.path.join(ART, 'keeptrakt.png')
ICONREAL = os.path.join(ART, 'keepdebrid.png')
ICONLOGIN = os.path.join(ART, 'keeplogin.png')
ICONCONTACT = os.path.join(ART, 'information.png')
ICONSETTINGS = os.path.join(ART, 'settings.png')
# Hide the section separators 'Yes' or 'No'
HIDESPACERS = 'No'
# Character used in separator
SPACER = '='

# You can edit these however you want, just make sure that you have a %s in each of the
# THEME's so it grabs the text from the menu item
COLOR1 = 'orangered'
COLOR2 = 'chocolate'
# Primary menu items   / {0} is the menu item and is required
THEME1 = u'[COLOR {color1}][I][COLOR {color1}][/COLOR][COLOR {color2}][COLOR {color1}] [/I][/COLOR] [COLOR {color2}]{{}}[/COLOR]'.format(color1=COLOR1, color2=COLOR2)
# Build Names          / {0} is the menu item and is required
THEME2 = u'[COLOR {color1}]{{}}[/COLOR]'.format(color1=COLOR1)
# Alternate items      / {0} is the menu item and is required
THEME3 = u'[COLOR {color1}]{{}}[/COLOR]'.format(color1=COLOR1)
# Current Build Header / {0} is the menu item and is required
THEME4 = u'[COLOR {color1}]Current Build: [/COLOR] [COLOR {color2}]{{}}[/COLOR]'.format(color1=COLOR1, color2=COLOR2)
# Current Theme Header / {0} is the menu item and is required
THEME5 = u'[COLOR {color1}]Current Theme: [/COLOR] [COLOR {color2}]{{}}[/COLOR]'.format(color1=COLOR1, color2=COLOR2)

# Message for Contact Page
# Enable 'Contact' menu item 'Yes' hide or 'No' dont hide
HIDECONTACT = 'Yes'
# You can add \n to do line breaks
CONTACT = 'Keep Calm and Carry On!Thank you for choosing Al8inA Matrix Wizard.'
# Images used for the contact window.  http:// for default icon and fanart
CONTACTICON = 'https://archive.org/download/al8ina/albina%2050%2050%20transparent.png'
CONTACTFANART = 'https://archive.org/download/al8ina/bee%20queen.jpg'
#########################################################

#########################################################
#        Auto Update For Those With No Repo             #
#########################################################
# Enable Auto Update 'Yes' or 'No'
AUTOUPDATE = 'No'
#########################################################

#########################################################
#        Auto Install Repo If Not Installed             #
#########################################################
# Enable Auto Install 'Yes' or 'No'
AUTOINSTALL = 'No'
# Addon ID for the repository
REPOID = ''
# Url to Addons.xml file in your repo folder(this is so we can get the latest version)
REPOADDONXML = 'https://raw.githubusercontent.com/a4k-openproject/repository.openwizard/master/zips/addons.xml'
# Url to folder zip is located in
REPOZIPURL = 'https://'
#########################################################

#########################################################
#        Notification Window                            #
#########################################################
# Enable Notification screen Yes or No
ENABLE = 'Yes'
# Url to notification file
NOTIFICATION = 'https://archive.org/download/builds19/notify.txt'
# Use either 'Text' or 'Image'
HEADERTYPE = 'Text'
# Font size of header
FONTHEADER = 'Font14'
HEADERMESSAGE = '[COLOR orangered][B]Al8inA[/B][/COLOR] [COLOR chocolate]Matrix Wizard[/COLOR]'
# url to image if using Image 424x180
HEADERIMAGE = 'http://'
# Font for Notification Window
FONTSETTINGS = 'Font13'
# Background for Notification Window
BACKGROUND = 'http://'
#########################################################