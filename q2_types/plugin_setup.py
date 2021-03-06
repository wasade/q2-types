# ----------------------------------------------------------------------------
# Copyright (c) 2016--, QIIME development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

import importlib

import qiime.plugin
import qiime.sdk

from q2_types import __version__

citation_text = ('This plugin does not have a direct citation. Please instead '
                 'cite QIIME: %s' % qiime.sdk.CITATION)
user_support_text = ('To get help with this plugin, see the QIIME 2 wiki at '
                     'http://2.qiime.org, or post to the q2-types issue '
                     'tracker at: https://github.com/qiime2/q2-types/issues')

plugin = qiime.plugin.Plugin(
    name='types',
    version=__version__,
    website='https://github.com/qiime2/q2-types',
    package='q2_types',
    citation_text=citation_text,
    user_support_text=user_support_text
)

importlib.import_module('q2_types.feature_table')
importlib.import_module('q2_types.distance_matrix')
importlib.import_module('q2_types.tree')
importlib.import_module('q2_types.ordination')
importlib.import_module('q2_types.sample_data')
importlib.import_module('q2_types.feature_data')
importlib.import_module('q2_types.reference_features')
importlib.import_module('q2_types.per_sample_sequences')
