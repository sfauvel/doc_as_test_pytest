"""
This file is an example of using doc as test with pytest.
"""
import inspect
import os
import pytest
import textwrap
from doc_as_test_pytest import DocAsTest, doc, doc_module

class CodeExtractor:
    def extract_code(object, tag:str):
        return inspect.getsource(object)\
            .split(f"# >>>{tag}")[1]\
            .split(f"# <<<{tag}")[0]
            
def format_code(request, tag):
    code = CodeExtractor.extract_code(request.module, tag)
    return (textwrap.dedent("""\

        .Code use to generate this chapter
        [%collapsible]
        ====
        [source,python,indent=0]
        ----
        {}
        ----
        ====
        """).format(code))

# >>>simple_chapter
def test_simple_chapter(request, doc):
    doc.write(textwrap.dedent("""
        You can write in your test the information you want to see in your documentation.
        """))

# <<<simple_chapter
    doc.write(format_code(request, "simple_chapter"))

# >>>using_doc_string
def test_using_doc_string(request, doc):
    """
    The description of the chapter can be done using Python docstring.
    """

    doc.write(textwrap.dedent("""
        This doc string is placed in the document just under the title and before the text added within the test function.
        """))

# <<<using_doc_string
    doc.write(format_code(request, "using_doc_string"))

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

