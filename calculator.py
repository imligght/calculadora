import customtkinter as ctk

# define o cálculo, inicialmente, como uma string vazia
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
root = ctk.CTk()
root.geometry("200x300")
root.title('Calculator')
# define um campo para mostrar os números que estão sendo operados e o resultado
text_result = ctk.CTkTextbox(root, width=200, height=50, font=("Arial", 24))
text_result.grid(columnspan=5)
# criando e posicionando os botões/teclas em seus devidos lugares
button_1 = ctk.CTkButton(root, text='1', command=lambda: Calculator().add_to_calculation(1), width=50, height=50, font=('Arial', 25))
button_1.grid(row=2, column=1)
button_2 = ctk.CTkButton(root, text='2', command=lambda: Calculator().add_to_calculation(2), width=50, height=50, font=('Arial', 25))
button_2.grid(row=2, column=2)
button_3 = ctk.CTkButton(root, text='3', command=lambda: Calculator().add_to_calculation(3), width=50, height=50, font=('Arial', 25))
button_3.grid(row=2, column=3)
button_4 = ctk.CTkButton(root, text='4', command=lambda: Calculator().add_to_calculation(4), width=50, height=50, font=('Arial', 25))
button_4.grid(row=3, column=1)
button_5 = ctk.CTkButton(root, text='5', command=lambda: Calculator().add_to_calculation(5), width=50, height=50, font=('Arial', 25))
button_5.grid(row=3, column=2)
button_6 = ctk.CTkButton(root, text='6', command=lambda: Calculator().add_to_calculation(6), width=50, height=50, font=('Arial', 25))
button_6.grid(row=3, column=3)
button_7 = ctk.CTkButton(root, text='7', command=lambda: Calculator().add_to_calculation(7), width=50, height=50, font=('Arial', 25))
button_7.grid(row=4, column=1)
button_8 = ctk.CTkButton(root, text='8', command=lambda: Calculator().add_to_calculation(8), width=50, height=50, font=('Arial', 25))
button_8.grid(row=4, column=2)
button_9 = ctk.CTkButton(root, text='9', command=lambda: Calculator().add_to_calculation(9), width=50, height=50, font=('Arial', 25))
button_9.grid(row=4, column=3)
button_0 = ctk.CTkButton(root, text='0', command=lambda: Calculator().add_to_calculation(0), width=50, height=50, font=('Arial', 25))
button_0.grid(row=5, column=2)
button_plus = ctk.CTkButton(root, text='+', command=lambda: Calculator().add_to_calculation('+'), width=50, height=50, font=('Arial', 25))
button_plus.grid(row=5, column=4)
button_minus = ctk.CTkButton(root, text='-', command=lambda: Calculator().add_to_calculation('-'), width=50, height=50, font=('Arial', 25))
button_minus.grid(row=4, column=4)
button_mult = ctk.CTkButton(root, text='*', command=lambda: Calculator().add_to_calculation('*'), width=50, height=50, font=('Arial', 25))
button_mult.grid(row=3, column=4)
button_division = ctk.CTkButton(root, text='/', command=lambda: Calculator().add_to_calculation('/'), width=50, height=50, font=('Arial', 25))
button_division.grid(row=2, column=4)
button_open_parentheses = ctk.CTkButton(root, text='(', command=lambda: Calculator().add_to_calculation('('), width=50, height=50, font=('Arial', 25))
button_open_parentheses.grid(row=5, column=1)
button_close_parentheses = ctk.CTkButton(root, text=')', command=lambda: Calculator().add_to_calculation(')'), width=50, height=50, font=('Arial', 25))
button_close_parentheses.grid(row=5, column=3)

button_equal = ctk.CTkButton(root, text='=', command=Calculator().evaluate_calculation, width=100, height=50, font=('Arial', 25))
button_equal.grid(row=6, column=1, columnspan=2)
button_clear= ctk.CTkButton(root, text='C', command=Calculator().clear_field, width=100, height=50, font=('Arial', 25))
button_clear.grid(row=6, column=3, columnspan=2)

root.mainloop()