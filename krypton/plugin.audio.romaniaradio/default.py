# -*- coding: utf-8 -*-

import os
import sys
import xbmcaddon
__settings__ = xbmcaddon.Addon()
__version__ = __settings__.getAddonInfo('version')
__plugin__ = __settings__.getAddonInfo('name') + " v." + __version__
__root__ = __settings__.getAddonInfo('path')
__media__ = os.path.join(__root__, 'resources', 'media')

if (__name__ == "__main__" ):
    from resources import Core

    core = Core.Core()
    if (not sys.argv[2]):
        core.sectionMenu()
    else:
        params = core.getParameters(sys.argv[2])
        core.executeAction(params)
    del core
