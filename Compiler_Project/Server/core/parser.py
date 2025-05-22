def analyze_syntax(code):
    return f"""Syntax Analysis:
- Balanced brackets: {'✓' if code.count('{') == code.count('}') else '✗'}
- Semicolons present: {'✓' if ';' in code else '✗'}
- Return statement: {'✓' if 'return' in code else '✗'}
"""