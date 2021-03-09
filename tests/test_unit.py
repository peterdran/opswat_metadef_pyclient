from .context import upload_file

def test_result_formatter():
    assert upload_file.result_formatter(None) is not None
