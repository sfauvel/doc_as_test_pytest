"""
The module description.
"""
import os
import pytest
from DocAsTestPyTest import DocAsTest


@pytest.fixture(scope="function")
def doc(request, doc_module):
    yield doc_module

    doc_module.verify_function(request)

@pytest.fixture(scope="module")
def doc_module(request):
    doc = DocAsTest()

    yield doc

    doc.verify_module(request)

def test_with_description(request, doc):
    """
    The description of this chapter.
    """

    doc.write("Test to check")


def test_second(request, doc):
    """
    The description of the second chapter.
    """

    doc.write("Test to check")


def test_third(request, doc):
   
    doc.write("Nothing new for this third test")
