import tkinter as tk
import customtkinter as ctk

#Configura o tema e a cor do customtkinter
ctk.set_appearance_mode("System")  # "System", "Dark", "Light"
ctk.set_default_color_theme("blue")  # "blue", "green", "dark-blue"

class CalculatorApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        #Configurações da janela
        self.title("Calculadora Simples")
        self.geometry("300x400")
        
        #Cria os widgets
        self.create_widgets()

    def create_widgets(self):
        #Frame para os campos de entrada e botões
        main_frame = ctk.CTkFrame(self)
        main_frame.pack(padx=20, pady=20, fill="both", expand=True)

        # Campos de entrada
        self.entry1 = ctk.CTkEntry(main_frame, placeholder_text="Número 1")
        self.entry1.pack(pady=10)

        self.entry2 = ctk.CTkEntry(main_frame, placeholder_text="Número 2")
        self.entry2.pack(pady=10)

        # Frame para os botões de operação
        button_frame = ctk.CTkFrame(main_frame)
        button_frame.pack(pady=10)

        # Botões de operação
        self.add_button = ctk.CTkButton(button_frame, text="+", command=lambda: self.calculate("add"))
        self.add_button.pack(side="left", padx=5)

        self.subtract_button = ctk.CTkButton(button_frame, text="-", command=lambda: self.calculate("subtract"))
        self.subtract_button.pack(side="left", padx=5)

        self.multiply_button = ctk.CTkButton(button_frame, text="*", command=lambda: self.calculate("multiply"))
        self.multiply_button.pack(side="left", padx=5)

        self.divide_button = ctk.CTkButton(button_frame, text="/", command=lambda: self.calculate("divide"))
        self.divide_button.pack(side="left", padx=5)
        
        # Campo de exibição do resultado
        self.result_label = ctk.CTkLabel(main_frame, text="Resultado:")
        self.result_label.pack(pady=20)
    
    def calculate(self, operation):
        try:
            num1 = float(self.entry1.get())
            num2 = float(self.entry2.get())

            if operation == "add":
                result = num1 + num2
            elif operation == "subtract":
                result = num1 - num2
            elif operation == "multiply":
                result = num1 * num2
            elif operation == "divide":
                if num2 == 0:
                    self.result_label.configure(text="Erro: Divisão por zero!")
                    return
                result = num1 / num2
            
            self.result_label.configure(text=f"Resultado: {result}")

        except ValueError:
            self.result_label.configure(text="Entrada inválida. Digite números.")

if __name__ == "__main__":
    app = CalculatorApp()
    app.mainloop()