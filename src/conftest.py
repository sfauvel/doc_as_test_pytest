import pytest
from doc_as_test_pytest import DocAsTest, doc_module

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    This hook write in doc the exception that occured during test execution.
    """
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        doc_fixture_name = doc_module.__name__
        if doc_fixture_name in item.funcargs:
            doc = item.funcargs[doc_fixture_name]
            if isinstance(doc, DocAsTest):
                doc.write(f"Exception executing test:\n----\n{rep.longreprtext}\n----\n")
