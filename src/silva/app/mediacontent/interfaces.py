# Copyright (c) 2011 Infrae. All rights reserved.
# See also LICENSE.txt

from zope.i18nmessageid import MessageFactory
from zope.interface import Interface
from zope import schema
from silva.core import interfaces
from silva.core.references.reference import Reference

_ = MessageFactory('silva')


class IMediaContent(interfaces.IVersionedContent):
    """ A simple content type with title description and a reference
    to an image or video
    """


class IMediaContentVersion(interfaces.IVersion):
    """ Version for IMediaContent
    """


class IMediaContentFields(Interface):
    """ Fields for forms
    """
    text = schema.Text(
        title=_('text'),
        description=_('Plain text or restructured text format'),
        required=False)
    asset = Reference(interfaces.INonPublishable,
        title=_('asset'),
        description=_('Image or video asset'),
        required=False)
    link = Reference(interfaces.ISilvaObject,
        title=_('link'),
        description=_('Link target for more information'),
        required=False)


class IYouTubeVideo(interfaces.INonPublishable):
    """ A video linked from you tube
    """


class IYouTubeVideoFields(Interface):
    """ Fields for forms.
    """
    video_id = schema.TextLine(
        title=_(u'video id'),
        description=_(u'Tt is the id of the video on youtube.com,'
                      u'it can be found in the url as "v" parameter'),
        required=True)


