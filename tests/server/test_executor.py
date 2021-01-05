from src.server.executor import Executor


class TestExecutor:
    def test_return_value_formatter_basic(self):
        data = "{\"a\",\"b\",3,n=3}"
        result = Executor.return_value_formatter(data)
        assert result == ["a", "b", 3]

    def test_return_value_formatter_one_gap(self):
        data = "{\"a\",\"b\",[4]=\"d\",n=4}"
        result = Executor.return_value_formatter(data)
        assert result == ["a", "b", None, "d"]

    def test_return_value_formatter_two_gaps(self):
        data = "{\"a\",[3]=\"c\",[4]=\"d\",[6]=\"f\",n=6}"
        result = Executor.return_value_formatter(data)
        assert result == ["a", None, "c", "d", None, "f"]

    def test_return_value_formatter_big_gaps(self):
        data = "{\"a\",[5]=\"e\",[9]=\"i\",[12]=\"l\",n=12}"
        result = Executor.return_value_formatter(data)
        assert result == ["a", None, None, None, "e", None, None, None, "i", None, None, "l"]

    def test_return_value_formatter_initial_gap(self):
        data = "{[3]=\"c\",[5]=\"e\",n=5}"
        result = Executor.return_value_formatter(data)
        assert result == [None, None, "c", None, "e"]

    def test_return_value_formatter_mixed_values(self):
        data = "{\"a\",1,[4]=false,n=4}"
        result = Executor.return_value_formatter(data)
        assert result == ["a", 1, None, False]

    def test_return_value_formatter_empty(self):
        data = "{n=0}"
        result = Executor.return_value_formatter(data)
        assert result == []
