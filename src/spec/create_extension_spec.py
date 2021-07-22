# -*- coding: utf-8 -*-

import os.path

from pynwb.spec import NWBNamespaceBuilder, export_spec, NWBGroupSpec, NWBAttributeSpec
# TODO: import the following spec classes as needed
from pynwb.spec import NWBDatasetSpec, NWBRefSpec, NWBDtypeSpec


def main():
    # these arguments were auto-generated from your cookiecutter inputs
    ns_builder = NWBNamespaceBuilder(
        doc="""An extension for building descriptions of 1D stimulus waveforms referenced to an ontology.""",
        name="""ndx-stimulation""",
        version="""0.1.0""",
        author=list(map(str.strip, """Pamela Baker""".split(','))),
        contact=list(map(str.strip, """pamela.baker@alleninstitute.org""".split(',')))
    )

    # TODO: specify the neurodata_types that are used by the extension as well
    # as in which namespace they are found
    # this is similar to specifying the Python modules that need to be imported
    # to use your new data types
    # as of HDMF 1.6.1, the full ancestry of the neurodata_types that are used by
    # the extension should be included, i.e., the neurodata_type and its parent
    # type and its parent type and so on. this will be addressed in a future
    # release of HDMF.

    #    ns_builder.include_type('NWBDataInterface', namespace='core')
    #    ns_builder.include_type('Data', namespace='hdmf-common')

    ## Q: are these in core or hdmf-common? since file says hdmf-common, recently added to core?
    ns_builder.include_type('Container', namespace='core')
    ns_builder.include_type('DynamicTable', namespace='core')
    #    ns_builder.include_type('DynamicTableRegion', namespace='hdmf-common')
    ns_builder.include_type('VectorIndex', namespace='hdmf-common')
    ns_builder.include_type('VectorData', namespace='hdmf-common')


    # Defining compound datatypes for float and functional parameters

    float_parameter_dtype = [ 
        NWBDtypeSpec(name='name',
                     dtype='text',
                     doc="The float parameter name."),
        NWBDtypeSpec(name='value',
                     dtype='float32',
                     doc="The float parameter value."),
        NWBDtypeSpec(name='unit',
                     dtype='text',
                     doc='The float parameter units.')
        ]


    function_parameter_dtype = [
        NWBDtypeSpec(name='name',
                     dtype='text',
                     doc="The function parameter name."),
        NWBDtypeSpec(name='index',
                     dtype='int32',
                     doc="The index of the function parameter in the stimulus function table."),
        NWBDtypeSpec(name='unit',
                     dtype='text',
                     doc='The function parameter units.')
        ]



    # Defining the table columns (no aligned tables yet)

    function_name_spec = NWBDatasetSpec(
        name='function_name',
        neurodata_type_inc='VectorData',
        doc='Column storing the names of the 1D stimulus waveforms.',
        dtype='text'
    )

    float_parameters_spec = NWBDatasetSpec(
        name='float_parameters',
        neurodata_type_inc='VectorData',
        doc='Column storing the float parameter containers for the 1D stimulus waveforms.',
        quantity='?',
        dtype=float_parameter_dtype
    )

    # targets above by naming convention                                                                                   
    float_parameters_index_spec = NWBDatasetSpec(
        name='float_parameters_index',
        neurodata_type_inc='VectorIndex',
        doc='Index dataset for the float_parameters column.',
        quantity='?'
        )                                           

    function_parameters_spec = NWBDatasetSpec(
        name='function_parameters',
        neurodata_type_inc='VectorData',
        doc='Column storing the function parameters used in the 1D stimulus waveforms.',
        quantity='?',
        dtype=function_parameter_dtype
    )

    # targets above by naming convention                                                                                   
    function_parameters_index_spec = NWBDatasetSpec(
        name='function_parameters_index',
        neurodata_type_inc='VectorIndex',
        doc='Index dataset for the function_parameters column.',
        quantity='?'
    )                                                                



    # Build the full StimulusFunctionTable

    stimulus_function_table_spec = NWBGroupSpec(
        neurodata_type_inc='DynamicTable',
        neurodata_type_def='StimulusFunctionTable',
        doc='Table for storing 1D-waveform stimulus descriptions with references to a stimulus ontology.',
        attributes=[NWBAttributeSpec(name='description',
                                     dtype='text',
                                     doc='Description of what is in this dynamic table.',
                                     value='Table for storing ontologized 1D stimulus descriptions.')],
        datasets=[function_name_spec,
                  float_parameters_spec,
                  float_parameters_index_spec,
                  function_parameters_spec,
                  function_parameters_index_spec,
                 ]
    )


    sft_labmetadata_spec = NWBGroupSpec(
        neurodata_type_def='StimulusFunctionLabMetaData',
        neurodata_type_inc='LabMetaData',
        doc=('An enhanced LabMetaData type that has an additional field for a StimulusFunctionTable. '
             'NOTE: If this proposal for extension to NWB gets merged with the core schema, then this type would be '
             'removed and the Stimulus templates specification updated instead.'),
        groups=[
            NWBGroupSpec(
                  name='stimulus_function_table',
                  neurodata_type_inc='StimulusFunctionTable',
                  doc='Stimulus waveform metadata.',
                  quantity='?'
            ),
        ],
    )


    # TODO: add all of your new data types to this list
    new_data_types = [stimulus_function_table_spec, sft_labmetadata_spec]

    # export the spec to yaml files in the spec folder
    output_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'spec'))
    export_spec(ns_builder, new_data_types, output_dir)


if __name__ == "__main__":
    # usage: python create_extension_spec.py
    main()
