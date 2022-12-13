import pytest

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    This hook write in doc the exception that occured during test execution.
    """
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        doc = item.funcargs["doc_module"]
        doc.write(f"Exception executing test:\n----\n{rep.longreprtext}\n----\n")
