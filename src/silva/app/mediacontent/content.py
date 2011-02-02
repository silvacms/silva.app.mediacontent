# Copyright (c) 2011 Infrae. All rights reserved.
# See also LICENSE.txt

from five import grok
from zope.i18nmessageid import MessageFactory
from zope.component import getUtility

from Acquisition import aq_inner
from AccessControl import ClassSecurityInfo
from App.class_init import InitializeClass

from zeam.form import silva as silvaforms
from silva.core import conf as silvaconf
from silva.app.mediacontent import interfaces
from silva.core.views import views as silvaviews
from silva.core.conf.interfaces import ITitledContent
from silva.core.references.reference import get_content_id
from silva.core.references.interfaces import IReferenceService
from Products.Silva.VersionedContent import VersionedContent
from Products.Silva.Version import Version
from Products.Silva import SilvaPermissions as perms

_ = MessageFactory('silva')


class MediaContentVersion(Version):
    """ Version for Media Content
    """
    grok.implements(interfaces.IMediaContentVersion)

    security = ClassSecurityInfo()

    _description = None
    _asset = None
    _link = None

    security.declareProtected(perms.View, 'get_description')
    def get_description(self):
        return self._description

    security.declareProtected(perms.ChangeSilvaContent, 'set_description')
    def set_description(self, description):
        self._description = description
        return self._description

    security.declareProtected(perms.View, 'get_asset')
    def get_asset(self):
        service = getUtility(IReferenceService)
        reference = service.get_reference(
            aq_inner(self), name=u'asset', add=True)
        return reference.target

    security.declareProtected(perms.ChangeSilvaContent, 'set_asset')
    def set_asset(self, target):
        service = getUtility(IReferenceService)
        reference = service.get_reference(
            aq_inner(self), name=u'asset', add=True)
        if not isinstance(target, int):
            target = get_content_id(target)
        reference.set_target_id(target)

    security.declareProtected(perms.View, 'get_link')
    def get_link(self):
        service = getUtility(IReferenceService)
        reference = service.get_reference(
            aq_inner(self), name=u'link', add=True)
        return reference.target

    security.declareProtected(perms.ChangeSilvaContent, 'set_link')
    def set_link(self, target):
        service = getUtility(IReferenceService)
        reference = service.get_reference(
            aq_inner(self), name=u'link', add=True)
        if not isinstance(target, int):
            target = get_content_id(target)
        reference.set_target_id(target)


InitializeClass(MediaContentVersion)


class MediaContent(VersionedContent):
    __doc__ = _(u"A simple content type with title description and a reference "
                u"to an image or video and a link to another content.")
    grok.implements(interfaces.IMediaContent)
    silvaconf.priority(1000)
    silvaconf.version_class(MediaContentVersion)
    silvaconf.icon('mediacontent.png')

    meta_type = 'Silva MediaContent'
    security = ClassSecurityInfo()


InitializeClass(MediaContentVersion)


class MediaContentView(silvaviews.View):
    """ Default view for media content.
    """
    grok.context(interfaces.IMediaContent)


class MediaContentEditForm(silvaforms.SMIEditForm):
    """SMI edit form for media content.
    """
    grok.context(interfaces.IMediaContent)
    fields = silvaforms.Fields(
        ITitledContent, interfaces.IMediaContentFields).omit('id')


class MediaContentAddForm(silvaforms.SMIAddForm):
    """SMI add form for media content.
    """
    grok.context(interfaces.IMediaContent)
    grok.name(u'Silva MediaContent')
    fields = silvaforms.Fields(ITitledContent, interfaces.IMediaContentFields)


