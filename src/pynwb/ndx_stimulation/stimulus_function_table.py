import numpy as np
import warnings

from pynwb import register_class
from pynwb.core import DynamicTable
from hdmf.utils import docval, get_docval, getargs, popargs, call_docval_func, AllowPositional
from hdmf.common.resources import Key


# TODO: import your classes here or define your class using get_class to make
# them accessible at the package level                 
# StimulusFunctionTable = get_class('StimulusFunctionTable', 'ndx-stimulation')

@register_class('StimulusFunctionTable', 'ndx-stimulation')
class StimulusFunctionTable(DynamicTable):

    __columns__ = (
                    {'name':'function_name',
                     'description': 'The names of the 1D stimulus waveforms.',
                     'required': True,
                     'index': False},
                    {'name':'float_parameters',
                     'description': 'The names of the float parameters for the 1D stimulus wave\
forms.',
                     'required': True,
                     'index': True},
                    {'name':'function_parameters',
                     'description': 'The function parameters for the 1D stimulus waveforms.',
                     'required': True,
                     'index': True}
    )


    @docval(*get_docval(DynamicTable.__init__, 'id', 'columns', 'colnames'))
    def __init__(self, **kwargs):
        kwargs['name'] = ('StimulusFunctionTable')
        kwargs['description'] = ('Table for storing ontologized 1D stimulus waveform metadata')
        call_docval_func(super().__init__, kwargs)


### Ryan adds functions for the tables here as well...
### What funcitonality should I add and code in here?

### EG HIS add_external_resource function? how to modify for SFT?

### add_genotype --> add_stimwave? add_params?
