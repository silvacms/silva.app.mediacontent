
import unittest

from Products.Silva.testing import TestRequest
from Products.Silva.tests.test_xml_export import SilvaXMLTestCase

from silva.core.contentlayout.interfaces import IBlockManager, IBlockController
from silva.core.contentlayout.designs.registry import registry
from zeam.component import getWrapper

from ..block import SlideshowBlock
from ..testing import FunctionalLayer


class MediaContentXMLExportTestCase(SilvaXMLTestCase):
    layer = FunctionalLayer

    def setUp(self):
        self.root = self.layer.get_application()
        self.layer.login('chiefeditor')
        factory = self.root.manage_addProduct['Silva']
        factory.manage_addFolder('export', 'Export')
        factory = self.root.export.manage_addProduct['Silva']
        factory.manage_addFolder('images', 'Images')

    def test_export_sildeshow_block(self):
        factory = self.root.export.manage_addProduct['silva.core.contentlayout']
        factory.manage_addMockupPage('page', 'Page')

        page = self.root.export.page
        version = page.get_editable()
        version.set_design(registry.lookup_design_by_name('adesign'))
        slideshow = SlideshowBlock(u'slideshow 1')
        controller = getWrapper(
            (slideshow, version, TestRequest()),
            IBlockController)
        controller.container = self.root.export.images
        IBlockManager(version).add('one', slideshow)

        exporter = self.assertExportEqual(
            self.root.export,
            'test_export_slideshow_block.silvaxml')
        self.assertEqual(exporter.getZexpPaths(), [])
        self.assertEqual(exporter.getAssetPaths(), [])
        self.assertEqual(exporter.getProblems(), [])


def test_suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(MediaContentXMLExportTestCase))
    return suite
