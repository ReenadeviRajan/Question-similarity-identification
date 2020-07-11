from sympy import *
from latex2sympy import *
from sympy.parsing.latex import parse_latex
x=input()
expr = sympy.parsing.latex.parse_latex(x)
print(sympy.printing.latex(expr))

cnt=0
def open_img():
    x = filedialog.askopenfilename(title='Question')  # Select the Imagename from a folder
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
    k = pytesseract.image_to_string(x)
    ask_question(1 , k)
open_img()
