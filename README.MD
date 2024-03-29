[![Python Version](https://img.shields.io/badge/python-3.6-blue)](https://www.python.org/)
# PyRuster
## Features
Implementing some syntax like rust:

- `Result`
  - `Ok()`
  - `Err() `
  - `is_ok()`
  - `is_ok_and()`
  - `is_err()`
  - `is_err_and()`
  - `ok()`
  - `err()`
  - `map()`
  - `map_or()`
  - `map_or_else()`
  - `map_err()`
  - `inspect()`
  - `inspect_err()`
  - `expect()`
  - `expect_err()`
  - `unwrap()`
  - `unwrap_or()`
  - `unwrap_or_else()`
  - `unwrap_err()`
  - `and_()`
  - `and_then()`
  - `or_()`
  - `or_else()`

- `Option`
  - `Some()`
  - `None_()`
  - `is_some()`
  - `is_some_and()`
  - `is_none()`
  - `expect()`
  - `unwrap()`
  - `unwrap_or()`
  - `unwrap_or_else()`
  - `map()`
  - `inspect()`
  - `map_or()`
  - `map_or_else()`
  - `ok_or()`
  - `ok_or_else()`
  - `and_()`
  - `and_then()`
  - `filter()`
  - `or_()`
  - `or_else()`
  - `xor()`
  - `zip()`
  - `zip_with()`
  - `unzip()`

# Installation
`pip install pyruster`

# Usage
```python
from src.pyruster import Result, Option
result_ok = Result.Ok("ok")
option_some = Option.Some("some")
```