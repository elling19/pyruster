from typing import TypeVar, Generic, Optional


T = TypeVar('T')


class Option(Generic[T]):
    def __init__(self, value: Optional[T]):
        self.value: Optional[T] = value

    @staticmethod
    def some(value: T) -> 'Option[T]':
        return Option(value=value)

    @staticmethod
    def none() -> 'Option[T]':
        return Option(value=None)

    def is_some(self) -> bool:
        return self.value is not None

    def is_none(self) -> bool:
        return not self.is_some()

    def unwrap(self) -> T:
        if self.is_some():
            return self.value
        else:
            raise ValueError("Option is None.")

    def unwrap_or(self, default: T) -> T:
        if self.is_some():
            return self.value
        else:
            return default
