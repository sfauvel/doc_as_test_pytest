"""
This file is an example of using doc as test with pytest.
"""
import os
import pytest
from doc_as_test_pytest import DocAsTest, doc, doc_module



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

class TestClassDemo:
    """
    The class description.
    """
    def test_first_chapter_in_a_class(self, doc):
        """
        The description of the chapter within a class.
        """

        doc.write("Write the expected content here.")


    def test_second_chapter_in_a_class(self, doc):
        doc.write("With this second chapter, doc of the class should not be write a second time.")

    class TestSubClassDemo:
        def test_chapter_on_a_subclass(self, doc):
            doc.write("Could execute a subclass")


        def test_second_chapter_on_a_subclass(self, doc):
            doc.write("Could execute a subclass")

