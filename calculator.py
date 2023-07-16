import window as wdw
# define o cálculo, inicialmente, como uma string vazia
calculation = ''
# classe que representa uma calculadora
class Calculator():

    def add_to_calculation(self, symbol):
        global calculation
        calculation += str(symbol)
        wdw.text_result.delete(1.0, "end")
        wdw.text_result.insert(1.0, calculation)

    def clear_field(self):
       global calculation
       calculation = '' 
       wdw.text_result.delete(1.0, "end")

    def evaluate_calculation(self):
        global calculation
        try:
            calculation = str(eval(calculation)) 
            wdw.text_result.delete(1.0, "end")
            wdw.text_result.insert(1.0, calculation)
        except:
            self.clear_field()
            wdw.text_result.insert(1.0, "Error")