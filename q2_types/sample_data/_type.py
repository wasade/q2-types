# ----------------------------------------------------------------------------
# Copyright (c) 2016--, QIIME development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

from qiime.plugin import SemanticType

from ..plugin_setup import plugin
from . import AlphaDiversityDirectoryFormat


SampleData = SemanticType('SampleData', field_names='type')

AlphaDiversity = SemanticType('AlphaDiversity',
                              variant_of=SampleData.field['type'])

plugin.register_semantic_type(SampleData)
plugin.register_semantic_type(AlphaDiversity)

plugin.register_semantic_type_to_format(
    SampleData[AlphaDiversity],
    artifact_format=AlphaDiversityDirectoryFormat
)
