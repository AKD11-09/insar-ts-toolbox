# coding=utf-8
"""Resources test.

.. note:: This program is free software; you can redistribute it and/or modify
     it under the terms of the GNU General Public License as published by
     the Free Software Foundation; either version 2 of the License, or
     (at your option) any later version.

"""

__author__ = 'ashwinkumard.11@gmail.com'
__date__ = '2025-10-03'
__copyright__ = 'Copyright 2025, Ashwin Kumar Dhanasekaran M. Sc.'

import os
import unittest

from qgis.PyQt.QtGui import QIcon
from qgis.PyQt.QtWidgets import QApplication
from qgis.core import QgsApplication

# QIcon/QPixmap cannot be constructed before a GUI-enabled Qt application
# exists. utilities.get_qgis_app() is not usable here: it does a relative
# import of qgis_interface while the tests import it as a top-level module,
# so the ImportError is swallowed and it returns None.
QGIS_APP = QApplication.instance()
if QGIS_APP is None:
    QGIS_APP = QgsApplication([], True)
    QGIS_APP.initQgis()

PLUGIN_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class InSAR_TS_ToolboxResourcesTest(unittest.TestCase):
    """Test that the plugin icon loads.

    The plugin loads its icon straight from icon.png rather than through a
    compiled .qrc bundle, so this checks the file on disk. The previous
    version of this test looked for ':/plugins/InSAR_TS_Toolbox/icon.png',
    a Qt resource path that never resolved because no resources module was
    ever imported.
    """

    def test_icon_file_exists(self):
        """icon.png must be present next to the plugin modules."""
        self.assertTrue(os.path.isfile(os.path.join(PLUGIN_DIR, 'icon.png')))

    def test_icon_png_loads(self):
        """icon.png must be a decodable image, not just a present file."""
        icon = QIcon(os.path.join(PLUGIN_DIR, 'icon.png'))
        self.assertFalse(icon.isNull())

    def test_icon_matches_metadata(self):
        """The icon named in metadata.txt must be the one that exists."""
        import configparser
        cfg = configparser.ConfigParser()
        with open(os.path.join(PLUGIN_DIR, 'metadata.txt'),
                  encoding='utf-8') as handle:
            cfg.read_file(handle)
        declared = cfg.get('general', 'icon')
        self.assertTrue(os.path.isfile(os.path.join(PLUGIN_DIR, declared)))


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(
        InSAR_TS_ToolboxResourcesTest)
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
