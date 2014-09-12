"""
    urlresolver XBMC Addon
    Copyright (C) 2011 t0mm0

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

import os,xml.dom.minidom
from t0mm0.common.addon import Addon
import xbmc
import xbmcaddon
import xbmcgui
import xbmcplugin

addon = Addon('script.module.urlresolver')
addon_path = addon.get_path()
plugins_path = os.path.join(addon_path, 'lib', 'urlresolver', 'plugins')
profile_path = addon.get_profile()
settings_file = os.path.join(addon_path, 'resources', 'settings.xml')
addon_version = addon.get_version()
try:
    # Open existing settings file
    settings_xml = xml.dom.minidom.parse(settings_file)
except:
    # Create an empty document
    settings_xml = xml.dom.minidom.parseString("<settings>  </settings>")

pretty_print = lambda f: '\n'.join([line for line in f.split('\n') if line.strip()])

def _update_settings_xml():
    '''
    This function writes a new ``resources/settings.xml`` file which contains
    all settings for this addon and its plugins.
    '''
    try:
        try:
            os.makedirs(os.path.dirname(settings_file))
        except OSError:
            pass

        f = open(settings_file, 'w')
        try:
            f.write("<?xml version=\"1.0\" ?>\n")
            f.write("<settings>\n")
            elements = settings_xml.getElementsByTagName('category')
            elements.sort(key=lambda x: x.getAttribute('label'))
            for i in elements:
                xml_text = i.toprettyxml()
                f.write(pretty_print(xml_text))
            f.write("\n</settings>\n")
        finally:
            f.close
    except IOError:
        addon.log_error('error writing ' + settings_file)

