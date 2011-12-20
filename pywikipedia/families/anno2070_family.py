# -*- coding: utf-8 -*-
"""
This family file was auto-generated by $Id: generate_family_file.py 9734 2011-11-09 22:17:11Z valhallasw $
Configuration parameters:
  url = http://anno2070.wikia.com/wiki/Anno_2070_Wiki
  name = anno2070

Please do not commit this to the SVN repository!
"""

import family

class Family(family.Family):
    def __init__(self):
        family.Family.__init__(self)
        self.name = 'anno2070'
        self.langs = {
            'en': u'anno2070.wikia.com',
        }

        self.namespaces[-2] = self.namespaces.get(-2, {})
        self.namespaces[-2]['en'] = [u'Media']
        self.namespaces[-1] = self.namespaces.get(-1, {})
        self.namespaces[-1]['en'] = [u'Special']
        self.namespaces[1] = self.namespaces.get(1, {})
        self.namespaces[1]['en'] = [u'Talk']
        self.namespaces[2] = self.namespaces.get(2, {})
        self.namespaces[2]['en'] = [u'User']
        self.namespaces[3] = self.namespaces.get(3, {})
        self.namespaces[3]['en'] = [u'User talk']
        self.namespaces[4] = self.namespaces.get(4, {})
        self.namespaces[4]['en'] = [u'Anno 2070 Wiki']
        self.namespaces[5] = self.namespaces.get(5, {})
        self.namespaces[5]['en'] = [u'Anno 2070 Wiki talk']
        self.namespaces[6] = self.namespaces.get(6, {})
        self.namespaces[6]['en'] = [u'File']
        self.namespaces[7] = self.namespaces.get(7, {})
        self.namespaces[7]['en'] = [u'File talk']
        self.namespaces[8] = self.namespaces.get(8, {})
        self.namespaces[8]['en'] = [u'MediaWiki']
        self.namespaces[9] = self.namespaces.get(9, {})
        self.namespaces[9]['en'] = [u'MediaWiki talk']
        self.namespaces[10] = self.namespaces.get(10, {})
        self.namespaces[10]['en'] = [u'Template']
        self.namespaces[11] = self.namespaces.get(11, {})
        self.namespaces[11]['en'] = [u'Template talk']
        self.namespaces[12] = self.namespaces.get(12, {})
        self.namespaces[12]['en'] = [u'Help']
        self.namespaces[13] = self.namespaces.get(13, {})
        self.namespaces[13]['en'] = [u'Help talk']
        self.namespaces[14] = self.namespaces.get(14, {})
        self.namespaces[14]['en'] = [u'Category']
        self.namespaces[15] = self.namespaces.get(15, {})
        self.namespaces[15]['en'] = [u'Category talk']
        self.namespaces[110] = self.namespaces.get(110, {})
        self.namespaces[110]['en'] = [u'Forum']
        self.namespaces[111] = self.namespaces.get(110, {})
        self.namespaces[111]['en'] = [u'Forum talk']
        self.namespaces[902] = self.namespaces.get(902, {})
        self.namespaces[902]['en'] = [u'Layout']
        self.namespaces[400] = self.namespaces.get(400, {})
        self.namespaces[400]['en'] = [u'Video']
        self.namespaces[401] = self.namespaces.get(401, {})
        self.namespaces[401]['en'] = [u'Video talk']
        self.namespaces[500] = self.namespaces.get(500, {})
        self.namespaces[500]['en'] = [u'User blog']
        self.namespaces[501] = self.namespaces.get(501, {})
        self.namespaces[501]['en'] = [u'User blog comment']
        self.namespaces[502] = self.namespaces.get(502, {})
        self.namespaces[502]['en'] = [u'Blog']
        self.namespaces[503] = self.namespaces.get(503, {})
        self.namespaces[503]['en'] = [u'Blog talk']
        self.namespaces[902] = self.namespaces.get(902, {})
        self.namespaces[902]['en'] = [u'Layout']
        self.namespaces[1100] = self.namespaces.get(1100, {})
        self.namespaces[1100]['en'] = [u'RelatedVideos']
        self.namespaces[1200] = self.namespaces.get(1200, {})
        self.namespaces[1200]['en'] = [u'Message Wall']
        self.namespaces[1201] = self.namespaces.get(1201, {})
        self.namespaces[1201]['en'] = [u'Thread']
        self.namespaces[1202] = self.namespaces.get(1202, {})
        self.namespaces[1202]['en'] = [u'Message Wall Greeting']


    def scriptpath(self, code):
        return {
            'en': u'',
        }[code]

    def version(self, code):
        return {
            'en': u'1.16.5',
        }[code]
