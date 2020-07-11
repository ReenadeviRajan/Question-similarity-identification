from sympy import *
from latex2sympy import *
from sympy.parsing.latex import parse_latex
x=symbols("x")
print(latex(1/( (x+2)*(x+1) )))
expr = parse_latex(r"\frac {1 + \sqrt {\a}} {\b}")
print(expr)
expr = sympy.parsing.latex.parse_latex(r"\frac {1 + \sqrt {\a}} {\b}")
print(sympy.printing.latex(expr))

cnt=0
def open_img():
    x = filedialog.askopenfilename(title='Question')  # Select the Imagename from a folder
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
    k = pytesseract.image_to_string(x)
    ask_question(1 , k)

