# ----------------------------------------------------------------------------
# Copyright (c) 2016--, QIIME development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

import qiime.plugin.model as model

from ..feature_data import (DNAFASTAFormat, AlignedDNAFASTAFormat,
                            TaxonomyFormat)
from ..tree import NewickFormat


class ReferenceFeaturesDirectoryFormat(model.DirectoryFormat):
    dna_sequences = model.File('dna-sequences.fasta', format=DNAFASTAFormat)
    aligned_dna_sequences = model.File('aligned-dna-sequences.fasta',
                                       format=AlignedDNAFASTAFormat)
    taxonomy = model.File('taxonomy.tsv', format=TaxonomyFormat)
    tree = model.File('tree.nwk', format=NewickFormat)
