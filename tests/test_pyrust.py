import sys
import unittest
from .context import Option, Result


class PyRustTest(unittest.TestCase):

    def setUp(self):
        print(f"python version: {sys.version}")

    @staticmethod
    def test_option():
        option_none = Option(None)
        assert option_none.is_none()
        option_some = Option("some")
        assert option_some.is_some()

    @staticmethod
    def test_result():
        result_ok = Result("ok")
        assert result_ok.is_ok()
        assert result_ok.unwrap() == "ok"
        err_info = "err info"
        result_err = Result("err", err_info)
        assert result_err.is_err()
        assert result_err.unwrap_err() == err_info


if __name__ == "__main__":
    unittest.main()
