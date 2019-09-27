MP2: Functions
==============

This MP consists of two parts. Both parts are also commonly used as "screening"
questions in technical interviews.

Fibonacci numbers
=================

The [*Fibonacci numbers*](https://en.wikipedia.org/wiki/Fibonacci_number) are a
integer sequence such that each number is the sum of the two preceding numbers.

By convention, the "zero"th number in the sequence is 0, and the "first" number
is 1, respectively. Thus the sequence is given by 0, 1, 1, 2, 3, 5, 8, 13, 21, ...

### What to do

Write a function of the form:

```python
def fib(n: int) -> int:
    pass  # FIXME.
```

which `return`s the `n`th Fibonacci number where `n` is a non-negative integer.

Then, test it (using `assert`) for 1, 2, 3, and 100.

### Test support

The 100th Fibonacci number is 354224848179261915075.

### Hints

-   First compute the `n`th Fibonacci number, then `return` it (don't `print`
    it).
-   Do not try to define this recursively; it will be too slow for `fib(100)`.

### Stretch goal

Write a infinite generator function of the form:

```python
from typing import Iterator

def fib_generator() -> Iterator[int]:
    pass  # FIXME
```

which generates the infinite Fibonacci sequence. Then show it is correct up to
100 using the following snippet:

```python
gen = fib_generator()
for i in range(100):
    assert next(gen) == fib(i)
```

Bigrams
=======

A *bigram* is a ordered pair of contiguous symbols (usually, but not
necessarily) words. For instance, the previous sentence contains bigrams such as
`["of", "contiguous"]`, and `["but", "not"]`, but not `["is", "ordered"]`
(because those words are not contiguous) or `["a", "is"]` (because those words
do not occur in that order).

### What to do

Write a function of the form:

```python
from typing import List

def bigrams(sequence: List[str]) -> List[List[str]]:
    pass  # FIXME
```

which returns all bigrams (in order) from `sequence` (a list of strings). If
`sequence` is empty, or of length one, it should return nothing, but crucially,
your function **should not** crash.

### Test support

Your implementation should pass the following assertion tests:

```python
# Empty list.
tokens = []
assert not bigrams(tokens)

# List with one element,
tokens = ["Hi"]
assert not bigrams(tokens)

# List with many elements.
tokens = ["Four", "score", "and", "seven", "years"]
assert bigrams(tokens) == [["Four", "score"],
                           ["score", "and"],
                           ["and", "seven"],
                           ["seven", "years"]]
```

### Stretch goal

Write a generator function of the form:

```python
from typing import List, Iterable

def ngram_generator(sequence: List[str], n: int = 2) -> Iterable[List[str]]:
    pass  # FIXME
```

where `n` is the "order" of the bigrams (e.g., n = 2 gives bigrams, n = 3 gives
trigrams). Then, write some basic assertion tests to show its correctness.
