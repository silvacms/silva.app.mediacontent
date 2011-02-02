# Copyright (c) 2011 Infrae. All rights reserved.
# See also LICENSE.txt

import AccessControl

from silva.core import conf as silvaconf
from silva.core.conf.installer import DefaultInstaller
from zope.interface import Interface


silvaconf.extension_name("silva.app.mediacontent")
silvaconf.extension_title("Silva Media Content")
silvaconf.extension_depends(["Silva"])


class IMediaContentExtension(Interface):
    """Silva media content types.
    """


install = DefaultInstaller("silva.app.mediacontent", IMediaContentExtension)

