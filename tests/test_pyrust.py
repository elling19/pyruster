import sys
import unittest
from src.pyruster import Result, Option


def create_some_result(v: int) -> Result[int, str]:
    if v == 0:
        return Result.Err("v is zero.")
    return Result.Ok(v)

def create_some_option(v: int) -> Option[float]:
    if v == 0:
        return Option.None_()
    return Option.Some(float(v))

class PyRustTest(unittest.TestCase):

    def setUp(self):
        print(f"python version: {sys.version}")

    @staticmethod
    def test_option():
        option_none = Option.None_()
        assert option_none.is_none()
        option_none_ok_or = option_none.ok_or("no value")
        assert option_none_ok_or.is_err()
        assert option_none_ok_or.unwrap_err()
        option_none_two: Option[int] = Option.None_()
        assert option_none_two.is_none()
        option_none_two_ok_or = option_none_two.ok_or("no value")
        assert option_none_two_ok_or.is_err()
        option_some = Option.Some(2.71)
        assert option_some.is_some()
        option_some_ok_or = option_some.ok_or("no value")
        assert option_some_ok_or.is_ok()
        assert option_some_ok_or.unwrap() == 2.71

    @staticmethod
    def test_result():
        result_ok = Result.Ok("ok")
        assert result_ok.is_ok()
        assert result_ok.unwrap() == "ok"
        result_ok_one = result_ok.ok()
        assert result_ok_one.is_some()
        assert result_ok.ok().is_some()
        result_ok_two = Result.Ok(42).ok()
        assert result_ok_two.is_some()
        assert result_ok_two.unwrap() == 42
        result_err = Result.Err("error info")
        assert result_err.is_err()
        result_err_one = result_err.err()
        assert result_err_one.is_some()
        result_err_tow = result_err.ok()
        assert result_err_tow.is_none()
        err_info = "err info"
        result_err = Result("err", err_info)
        assert result_err.is_err()
        assert result_err.unwrap_err() == err_info
        assert result_err.err().is_some()
        result_ok = create_some_result(v=2)
        assert result_ok.unwrap() == 2
        result_err = create_some_result(v=0)
        assert result_err.is_err()
        option_some = Option.Some("some")
        option_some_result = option_some.ok_or("is none")
        assert option_some_result.unwrap() == "some"


if __name__ == "__main__":
    unittest.main()
