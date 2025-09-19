def are_brackets_balanced(s: str) -> bool:
    """
    Return True if brackets in s are balanced and correctly nested.
    Consider only (), {}, [].
    """
    stack = []
    # map closing bracket -> corresponding opening bracket
    match = {')': '(', '}': '{', ']': '['}

    for ch in s:
        if ch in '({[':
            stack.append(ch)
        elif ch in ')}]':
            if not stack:
                return False  # closing with no opening
            if stack[-1] != match[ch]:
                return False  # mismatched types
            stack.pop()

    return len(stack) == 0
tests = [
    ("", True),                              # empty string -> balanced
    ("()", True),
    ("([]){}", True),
    ("([{}])", True),
    ("(]", False),                           # wrong match
    ("([)]", False),                         # wrong nesting
    ("((()", False),                         # leftover opens
    (")(", False),                           # closing before opening
    ("a + (b - [c * {d/e}])", True),         # ignore non-bracket chars
    ("function(x) { return [x]; }", True),
    ("{[(])}", False),                       # nested mismatch
]

for s, expected in tests:
    result = are_brackets_balanced(s)
    print(f"{s!r:30} -> {result} (expected {expected})")
