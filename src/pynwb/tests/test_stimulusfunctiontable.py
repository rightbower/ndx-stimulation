import datetime
from dateutil.tz import tzlocal
from random import random, randint
import numpy as np
import unittest
import warnings

from pynwb import NWBHDF5IO, NWBFile
from pynwb.core import DynamicTableRegion
from pynwb.testing import TestCase, remove_test_file

from ndx_stimulation import StimulusFunctionTable

from hdmf.utils import docval, popargs



###
## 1. Do round trip
## 2. Check test_icephys for other tests to consider
##


# Setting up file basics - do I need this?
def set_up_nwbfile():

    nwbfile = NWBFile(
        session_description='session_description',
        identifier='identifier',
        session_start_time=datetime.datetime.now(datetime.timezone.utc)
    )

    return nwbfile



class TestSFTConstructor(TestCase):

    def test_sft_constructor(self):

        float_value = random()
        function_index = randint(0, 10)
        float_param = ('name', float_value, 'units')
        function_param = ('name', function_index, 'units')

        row = {
            'function_name':'function_name', 
            'float_parameters': float_param, 
            'function_parameters': function_param
            }

        stim_func_table = StimulusFunctionTable()
        stim_func_table.add_row(data=row)

        self.assertEqual(stim_func_table['function_name'].data[:][0], 'function_name')
        self.assertEqual(stim_func_table['float_parameters'].target[0], 'name')
        self.assertEqual(stim_func_table['float_parameters'].target[1], float_value)
        self.assertEqual(stim_func_table['float_parameters'].target[2], 'units')
        self.assertEqual(stim_func_table['function_parameters'].target[0], 'name')
        self.assertEqual(stim_func_table['function_parameters'].target[1], function_index)
        self.assertEqual(stim_func_table['function_parameters'].target[2], 'units')



class TestSFTRoundtrip(TestCase):

    def setUp(self):
        self.nwbfile = set_up_nwbfile()
        self.path = 'test.nwb'

    def tearDown(self):
        remove_test_file(self.path)

    def test_roundtrip(self):
        """
        Add an SFT to an NWBFile, write it to file, read the file, 
        and test that the SFT from the file matches the original SFT.
        """

        float_value = random()
        function_index = randint(0, 10)
        float_param = ('name', float_value, 'units')
        function_param = ('name', function_index, 'units')

        row = {
            'function_name':'function_name',
            'float_parameters': [float_param],
            'function_parameters': [function_param]
            }

        stim_func_table = StimulusFunctionTable()
        stim_func_table.add_row(data=row)


        self.nwbfile.add_acquisition(stim_func_table)

        with NWBHDF5IO(self.path, mode='w') as io:
            io.write(self.nwbfile)

        with NWBHDF5IO(self.path, mode='r', load_namespaces=True) as io:
            read_nwbfile = io.read()
            self.assertContainerEqual(stim_func_table, 
                                      read_nwbfile.acquisition['StimulusFunctionTable'])

