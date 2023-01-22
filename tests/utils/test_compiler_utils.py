import parapyro.utils.compiler_utils as cu

def test_set_in_brackets():

    result = cu.set_in_brackets('test_string')
    assert result == "{test_string}"
    custom_bracket = cu.set_in_brackets('test_string', ['[', ']'])
    assert custom_bracket == "[test_string]"

def test_preempt_slash():

    result = cu.preempt_slash('test_string')
    assert result == "\\test_string"

def test_usepackage():

    result = cu.usepackage('test_string')
    assert result == '\\usepackage{test_string}'

def test_begin():

    result = cu.begin('test_string')
    assert result == '\\begin{test_string}'

def test_end():

    result = cu.end('test_string')
    assert result == '\\end{test_string}'

def test_to_latex_bool():

    true = cu.to_latex_bool(True)
    false = cu.to_latex_bool(False)
    assert true == 'true'
    assert false == 'false'

def test_stack_list_to_lines():

    list_of_lines = [
        'line_1',
        'line_2',
        'line_3'
    ]
    result = cu.stack_list_to_lines(list_of_lines)
    assert result == """line_1
line_2
line_3
"""