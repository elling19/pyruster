from typing import TypeVar, Generic, Optional, Callable


T = TypeVar('T')
E = TypeVar('E')


class Result(Generic[T, E]):
    def __init__(self, value: Optional[T] = None, error: Optional[E] = None):
        self.value: Optional[T] = value
        self.error: Optional[E] = error

    @staticmethod
    def ok(value: T) -> 'Result[T, E]':
        return Result(value=value)

    @staticmethod
    def err(error: E) -> 'Result[T, E]':
        return Result(error=error)

    def is_ok(self) -> bool:
        return self.error is None

    def is_err(self) -> bool:
        return not self.is_ok()

    def unwrap(self) -> T:
        if self.is_ok():
            return self.value
        else:
            raise ValueError(f"Result is Err: {str(self.error)}")

    def unwrap_err(self) -> E:
        if self.is_err():
            return self.error
        else:
            raise ValueError(f"Result is Ok: {str(self.value)}")

    def map(self, func: Callable[[T], T]) -> 'Result[T, E]':
        if self.is_ok():
            return Result(func(self.value))
        else:
            return self

    def map_err(self, func: Callable[[E], E]) -> 'Result[T, E]':
        if self.is_err():
            return Result(self.value, func(self.error))
        else:
            return self
