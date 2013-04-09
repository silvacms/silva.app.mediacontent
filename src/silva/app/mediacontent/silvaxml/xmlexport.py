
from five import grok
from silva.core.xml import producers
from zope.interface import Interface

from silva.app.mediacontent.block import SlideshowBlock
from silva.app.mediacontent.silvaxml import NS_MEDIACONTENT_URI


class SlideshowBlockProducer(producers.SilvaProducer):
    """Export SlideshowBlock to XML.
    """
    grok.adapts(SlideshowBlock, Interface)

    def sax(self, parent=None):
        self.startElementNS(
            NS_MEDIACONTENT_URI, 'slideshowblock',
            {'slideshow': parent.get_reference(self.context.identifier)})
        self.endElementNS(NS_MEDIACONTENT_URI, 'slideshowblock')
