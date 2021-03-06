# ----------------------------------------------------------------------------
# Copyright (c) 2016--, QIIME development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

from qiime.plugin import SemanticType

from ..plugin_setup import plugin
from . import ReferenceFeaturesDirectoryFormat


ReferenceFeatures = SemanticType('ReferenceFeatures', field_names='type')
SSU = SemanticType('SSU', variant_of=ReferenceFeatures.field['type'])

plugin.register_semantic_type(ReferenceFeatures)
plugin.register_semantic_type(SSU)

plugin.register_semantic_type_to_format(
    ReferenceFeatures[SSU],
    artifact_format=ReferenceFeaturesDirectoryFormat)
