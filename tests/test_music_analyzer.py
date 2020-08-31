from unittest import TestCase
import numpy as np
from music_analysis.core import *

SAMPLE_FNAME = "samples/sample1.mp3"

class TestCoreLibrary(TestCase):
    
    def test_read_as_array_returns_ndarray(self):
        track = read_as_array(SAMPLE_FNAME)
        self.assertTrue(isinstance(track, np.ndarray))
