import pytest
from DocGenerator import DocGenerator, FullDocGenerator

@pytest.fixture(scope="function")
def doc(request, doc_file):
    generator = DocGenerator(request, (globals()[request.node.name].__doc__))
    doc_file.register(generator.doc_file_name())
    yield generator
    generator.finish()


@pytest.fixture(scope="module")
def doc_file():
    full_doc = FullDocGenerator("Demo.adoc")
    yield full_doc
    full_doc.finish()

def test_with_description(doc):
    """
    The description of this chapter.
    """

    doc.write("""The content of the chapter.
In python, it's easy to write a multiline text.
So, we can write the doc directly in the test.
""")

def test_a_second_chapter(doc):
    doc.write("""This econd chapter is visible in the general documentation
""")