# Copyright (c) 2011 Infrae. All rights reserved.
# See also LICENSE.txt

from five import grok

from zope.i18nmessageid import MessageFactory
from zope import schema
from zope.interface import Interface
from AccessControl import ClassSecurityInfo

from zeam.form import silva as silvaforms

from silva.core.conf.interfaces import ITitledContent
from silva.core import interfaces as silvainterfaces
from silva.core import conf as silvaconf
from Products.Silva.Asset import Asset
from Products.Silva import SilvaPermissions as perms

_ = MessageFactory('silva')


class IYouTubeVideo(silvainterfaces.IAsset):
    """ A video linked from you tube
    """


class YouTubeVideo(Asset):
    __doc__ = _('You tube video.')

    meta_type = u'Silva YouTube Video'
    silvaconf.priority(-10)
    silvaconf.icon('static/contents/Youtube-icon.png')
    grok.implements(IYouTubeVideo)

    security = ClassSecurityInfo()

    # Fields
    _video_id = None

    security.declareProtected(perms.ChangeSilvaContent, 'set_video_id')
    def set_video_id(self, id):
        self._video_id = id
        return self._video_id

    security.declareProtected(perms.View, 'get_video_id')
    def get_video_id(self, id):
        return self._video_id


class IYouTubeVideoFields(Interface):
    """ Fields for forms.
    """
    video_id = schema.TextLine(
        title=_(u'video id'),
        description=_(u'it is the id of the video on youtube.com,'
                      u'it can be found in the url as "v" parameter'),
        required=True)


class YouTubeVideoAddForm(silvaforms.SMIAddForm):
    """SMI add form for Silva YouTube Video.
    """
    grok.context(IYouTubeVideo)
    grok.name(u'Silva YouTube Video')
    fields = silvaforms.Fields(ITitledContent, IYouTubeVideoFields)


class YouTubeVideoEditForm(silvaforms.SMIEditForm):
    """SMI edit form for Silva YouTube Video.
    """
    grok.context(IYouTubeVideo)
    fields = silvaforms.Fields(IYouTubeVideoFields)


