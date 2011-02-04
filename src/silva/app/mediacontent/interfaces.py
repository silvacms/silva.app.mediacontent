# Copyright (c) 2011 Infrae. All rights reserved.
# See also LICENSE.txt

from zope.i18nmessageid import MessageFactory
from zope.interface import Interface
from zope import schema
from silva.core import interfaces
from silva.core.references.reference import Reference

_ = MessageFactory('silva')


class IMediaContent(interfaces.IVersionedContent):
    """A simple content type with title description and a reference
    to an image or video
    """


class IMediaContentVersion(interfaces.IVersion):
    """Version for IMediaContent
    """


class IMediaContentFields(Interface):
    """Fields for forms
    """
    text = schema.Text(
        title=_(u'text'),
        description=_(u'Plain text or restructured text format.'),
        required=False)
    asset = Reference(interfaces.INonPublishable,
        title=_(u'asset'),
        description=_(u'Image or video asset.'),
        required=False)
    link = Reference(interfaces.ISilvaObject,
        title=_(u'link'),
        description=_(u'Link target for more information.'),
        required=False)
    external_url = schema.URI(
        title=_(u"external url"),
        description=_(u"Only used if link is not set."),
        required=False)


class IEmbed(interfaces.INonPublishable):
    """Embed html content.
    """


class IEmbedFields(Interface):
    """Fields for forms.
    """
    html = schema.Text(
        title=_(u'raw html'),
        required=True)


