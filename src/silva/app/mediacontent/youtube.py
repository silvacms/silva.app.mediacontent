# Copyright (c) 2011 Infrae. All rights reserved.
# See also LICENSE.txt

from five import grok

from zope.i18nmessageid import MessageFactory

from AccessControl import ClassSecurityInfo
from App.class_init import InitializeClass

from zeam.form import silva as silvaforms

from silva.core.conf.interfaces import ITitledContent
from silva.core import conf as silvaconf
from silva.core.views import views as silvaviews
from Products.Silva.Asset import Asset
from Products.Silva import SilvaPermissions as perms
from silva.app.mediacontent.interfaces import (IYouTubeVideo,
    IYouTubeVideoFields)

_ = MessageFactory('silva')


class YouTubeVideo(Asset):
    __doc__ = _('You tube video.')

    meta_type = 'Silva YouTubeVideo'
    silvaconf.priority(1100)
    silvaconf.icon('youtube.png')
    grok.implements(IYouTubeVideo)

    security = ClassSecurityInfo()

    # Fields
    _video_id = None

    security.declareProtected(perms.ChangeSilvaContent, 'set_video_id')
    def set_video_id(self, id):
        self._video_id = id
        return self._video_id

    security.declareProtected(perms.View, 'get_video_id')
    def get_video_id(self):
        return self._video_id


InitializeClass(YouTubeVideo)


class YouTubeView(silvaviews.View):
    """Default view to render an embed youtube video.
    """
    grok.context(IYouTubeVideo)
    width = '480'
    height = '390'

    @property
    def video_id(self):
        return self.context.get_video_id()


class YouTubeVideoAddForm(silvaforms.SMIAddForm):
    """SMI add form for Silva YouTube Video.
    """
    grok.context(IYouTubeVideo)
    grok.name(u'Silva YouTubeVideo')
    fields = silvaforms.Fields(ITitledContent, IYouTubeVideoFields)


class YouTubeVideoEditForm(silvaforms.SMIEditForm):
    """SMI edit form for Silva YouTube Video.
    """
    grok.context(IYouTubeVideo)
    fields = silvaforms.Fields(IYouTubeVideoFields)


