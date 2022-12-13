"""
This file is an example of using doc as test with pytest.
"""
import os
import pytest
from doc_as_test_pytest import DocAsTest, doc, doc_class, doc_module



def test_first_chapter(doc):
    """
    The description of the chapter can be done with docstring.
    """

    doc.write("You can write in your test the information you want to see in your documentation.")


def test_second_chapter(doc):
    doc.write("""
The text written in the doc should provide enough information to say if the behaviour is correct.

Generally, we found input and output. 
    """)


def test_third_chapter(doc):
   
    doc.write("Nothing new for this third chapter")

@pytest.mark.parametrize("param", [
    ("Arg A"), 
    ("Arg B")
])
def test_chapter_with_parameters(doc, param):
   
    doc.write(f"Check it works with `{param}`")

@pytest.mark.usefixtures("doc_class")
class TestClassDemo:
    """
    The class description.
    """
    def test_first_chapter_in_a_class(self, doc):
        """
        The description of the chapter within a class.
        """

        doc.write("Write the expected content here.")

