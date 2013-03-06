# -*- coding: utf-8 -*-
# Copyright (c) 2011-2013 Infrae. All rights reserved.
# See also LICENSE.txt

import AccessControl

from silva.core import conf as silvaconf
from silva.core.conf.installer import DefaultInstaller
from silva.core.editor.interfaces import ICKEditorService
from zope.interface import Interface
from zope.component import getUtility

silvaconf.extension_name("silva.app.mediacontent")
silvaconf.extension_title("Silva Media Content")
silvaconf.extension_depends(["Silva"])


class IMediaContentExtension(Interface):
    """Silva media content types.
    """


class MediaContentInstaller(DefaultInstaller):

    def install_custom(self, root):
        declare = getUtility(ICKEditorService).declare_configuration
        declare('Silva Media Content')


install = MediaContentInstaller(
    "silva.app.mediacontent",
    IMediaContentExtension)

