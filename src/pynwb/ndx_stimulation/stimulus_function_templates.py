# add SFT to /general/stimulus or /stimulus/templates groups in NWBFile?

from pynwb import register_class
from pynwb.file import LabMetaData
from hdmf.utils import docval, get_docval, call_docval_func, popargs

from .stimulus_function_table import StimulusFunctionTable


@register_class('StimulusFunctionLabMetaData', 'ndx-stimulation')
class StimulusFunctionLabMetaData(LabMetaData):

    __nwbfields__ = (
        {'name': 'stimulus_function_table', 'child': True, 'required_name': 'stimulus_function_table'},
    )

    @docval(
        *get_docval(LabMetaData.__init__),
        {
            'name': 'stimulus_function_table',
            'type': 'StimulusFunctionTable',
            'doc': 'Table of stimulus waveform metadata.',
            'default': None,
        },
    )
    def __init__(self, **kwargs):
        stimulus_function_table = popargs('stimulus_function_table', kwargs)
        call_docval_func(super().__init__, kwargs)
        self.stimulus_function_table = stimulus_function_table




