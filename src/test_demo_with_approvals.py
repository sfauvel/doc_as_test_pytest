"""
This file is an example of using doc as test with pytest.
"""
import os
import pytest
from doc_as_test_pytest import DocAsTest


@pytest.fixture(scope="function")
def doc(request, doc_module):
    yield doc_module

    doc_module.verify_function(request)

@pytest.fixture(scope="module")
def doc_module(request):
    doc = DocAsTest()

    yield doc

    doc.verify_module(request)

def test_first_chapter(request, doc):
    """
    The description of the chapter can be done with docstring.
    """

    doc.write("You can write in your test the information you want to see in your documentation.")


def test_second_chapter(request, doc):
    doc.write("""
The text written in the doc should provide enough information to say if the behaviour is correct.

Generally, we found input and output. 
    """)


def test_third_chapter(request, doc):
   
    doc.write("Nothing new for this third chapter")
