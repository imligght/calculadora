import tkinter as tk

calculation = ''

# classe que representa uma calculadora
class Calculator():

    def add_to_calculation(self, symbol):
        global calculation
        calculation += str(symbol)
        text_result.delete(1.0, "end")
        text_result.insert(1.0, calculation)

    def clear_field(self):
       global calculation
       calculation = '' 
       text_result.delete(1.0, "end")

    def evaluate_calculation(self):
        global calculation
        try:
            calculation = str(eval(calculation)) 
            text_result.delete(1.0, "end")
            text_result.insert(1.0, calculation)
        except:
            self.clear_field()
            text_result.insert(1.0, "Error")

# cria a raiz, ou seja, uma janela. E define seu tamanho
root = tk.Tk()
root.geometry("315x260")
# define um campo para mostrar os números que estão sendo operados e o resultado
text_result = tk.Text(root, height=2, width=16, font=("Arial", 24))
text_result.grid(columnspan=5)
# criando e posicionando os botões/teclas em seus devidos lugares
button_1 = tk.Button(root, text='1', command=lambda: Calculator().add_to_calculation(1), width=5, font=('Arial', 14))
button_1.grid(row=2, column=1)
button_2 = tk.Button(root, text='2', command=lambda: Calculator().add_to_calculation(2), width=5, font=('Arial', 14))
button_2.grid(row=2, column=2)
button_3 = tk.Button(root, text='3', command=lambda: Calculator().add_to_calculation(3), width=5, font=('Arial', 14))
button_3.grid(row=2, column=3)
button_4 = tk.Button(root, text='4', command=lambda: Calculator().add_to_calculation(4), width=5, font=('Arial', 14))
button_4.grid(row=3, column=1)
button_5 = tk.Button(root, text='5', command=lambda: Calculator().add_to_calculation(5), width=5, font=('Arial', 14))
button_5.grid(row=3, column=2)
button_6 = tk.Button(root, text='6', command=lambda: Calculator().add_to_calculation(6), width=5, font=('Arial', 14))
button_6.grid(row=3, column=3)
button_7 = tk.Button(root, text='7', command=lambda: Calculator().add_to_calculation(7), width=5, font=('Arial', 14))
button_7.grid(row=4, column=1)
button_8 = tk.Button(root, text='8', command=lambda: Calculator().add_to_calculation(8), width=5, font=('Arial', 14))
button_8.grid(row=4, column=2)
button_9 = tk.Button(root, text='9', command=lambda: Calculator().add_to_calculation(9), width=5, font=('Arial', 14))
button_9.grid(row=4, column=3)
button_0 = tk.Button(root, text='0', command=lambda: Calculator().add_to_calculation(0), width=5, font=('Arial', 14))
button_0.grid(row=5, column=2)
button_plus = tk.Button(root, text='+', command=lambda: Calculator().add_to_calculation('+'), width=5, font=('Arial', 14))
button_plus.grid(row=5, column=4)
button_minus = tk.Button(root, text='-', command=lambda: Calculator().add_to_calculation('-'), width=5, font=('Arial', 14))
button_minus.grid(row=4, column=4)
button_mult = tk.Button(root, text='*', command=lambda: Calculator().add_to_calculation('*'), width=5, font=('Arial', 14))
button_mult.grid(row=3, column=4)
button_division = tk.Button(root, text='/', command=lambda: Calculator().add_to_calculation('/'), width=5, font=('Arial', 14))
button_division.grid(row=2, column=4)
button_open_parentheses = tk.Button(root, text='(', command=lambda: Calculator().add_to_calculation('('), width=5, font=('Arial', 14))
button_open_parentheses.grid(row=5, column=1)
button_close_parentheses = tk.Button(root, text=')', command=lambda: Calculator().add_to_calculation(')'), width=5, font=('Arial', 14))
button_close_parentheses.grid(row=5, column=3)

button_equal = tk.Button(root, text='=', command=Calculator().evaluate_calculation, width=13, font=('Arial', 14))
button_equal.grid(row=6, column=1, columnspan=2)
button_clear= tk.Button(root, text='C', command=Calculator().clear_field, width=13, font=('Arial', 14))
button_clear.grid(row=6, column=3, columnspan=2)

root.mainloop()