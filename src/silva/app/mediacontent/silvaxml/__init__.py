# -*- coding: utf-8 -*-
# Copyright (c) 2013 Infrae. All rights reserved.
# See also LICENSE.txt
# package

from silva.core.xml import NS_SILVA_URI, registerNamespace

NS_MEDIACONTENT_URI = NS_SILVA_URI + '/silva-app-mediacontent'
registerNamespace('mediacontent', NS_MEDIACONTENT_URI)
