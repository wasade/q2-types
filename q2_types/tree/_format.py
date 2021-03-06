# ----------------------------------------------------------------------------
# Copyright (c) 2016--, QIIME development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

import skbio.io
import qiime.plugin.model as model


class NewickFormat(model.TextFileFormat):
    def sniff(self):
        sniffer = skbio.io.io_registry.get_sniffer('newick')
        return sniffer(str(self))[0]


NewickDirectoryFormat = model.SingleFileDirectoryFormat(
    'NewickDirectoryFormat', 'tree.nwk', NewickFormat)
