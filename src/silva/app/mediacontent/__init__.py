# Copyright (c) 2011 Infrae. All rights reserved.
# See also LICENSE.txt

import AccessControl

from silva.core import conf as silvaconf
from silva.core.conf.installer import DefaultInstaller
from zope.interface import Interface


silvaconf.extension_name("silva.app.document")
silvaconf.extension_title("Silva new Document")
silvaconf.extension_depends(["Silva", "silva.core.editor"])


class IMediaContentExtension(Interface):
    """Silva media content types.
    """


install = DefaultInstaller("silva.app.mediacontent", IMediaContentExtension)

AccessControl.allow_module('silva.app.mediacontent')

