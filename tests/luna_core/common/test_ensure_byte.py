# -*- coding: utf-8 -*-
'''
Created on October 17, 2019

@author: aukermaa@mskcc.org
'''
import pytest

from luna_core.common.EnsureByteContext import EnsureByteContext
import io

def test_open_posix_file():
    with open("tests/luna_core/common/testdata/test_file.txt", "w") as f:
       f.write("Test")
    with EnsureByteContext():
       f = open("tests/luna_core/common/testdata/test_file.txt", "r")
    assert f.read() == "Test"

def test_open_byte_file():
    with EnsureByteContext():
       f = open(io.BytesIO(b"Test"))
    print (f)
    assert f.read() == b"Test"

