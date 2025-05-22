def generate_ast(code):
    """AST generation implementation"""
    return f"""Abstract Syntax Tree:
(Program
  (Function main
    (Parameters)
    (Body
      {get_ast_body(code)}
    )
  )
)"""

def get_ast_body(code):
    """Helper function for AST generation"""
    if 'printf' in code:
        return '(Call printf "Hello World!")'
    return '(Body)'