import tkinter as tk
from tkinter import messagebox

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Python Calculator")
        self.root.geometry("400x600")
        self.root.configure(bg="#f4f4f9")

        self.expression = ""
        self.input_text = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        # Entry frame
        input_frame = tk.Frame(self.root, width=400, height=100, bd=0, highlightbackground="black", highlightcolor="black", highlightthickness=1)
        input_frame.pack(side=tk.TOP)

        input_field = tk.Entry(input_frame, font=('arial', 24, 'bold'), textvariable=self.input_text, width=50, bg="#eee", bd=0, justify=tk.RIGHT)
        input_field.grid(row=0, column=0)
        input_field.pack(ipady=30) 

        # Buttons frame
        btns_frame = tk.Frame(self.root, width=400, height=500, bg="grey")
        btns_frame.pack()

        # Row 1
        clear = tk.Button(btns_frame, text="C", width=32, height=3, bd=0, bg="#eee", cursor="hand2", command=lambda: self.bt_clear()).grid(row=0, column=0, columnspan=3, padx=1, pady=1)
        divide = tk.Button(btns_frame, text="/", width=10, height=3, bd=0, bg="#ffa500", cursor="hand2", command=lambda: self.bt_click("/")).grid(row=0, column=3, padx=1, pady=1)

        # Row 2
        seven = tk.Button(btns_frame, text="7", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: self.bt_click(7)).grid(row=1, column=0, padx=1, pady=1)
        eight = tk.Button(btns_frame, text="8", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: self.bt_click(8)).grid(row=1, column=1, padx=1, pady=1)
        nine = tk.Button(btns_frame, text="9", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: self.bt_click(9)).grid(row=1, column=2, padx=1, pady=1)
        multiply = tk.Button(btns_frame, text="*", width=10, height=3, bd=0, bg="#ffa500", cursor="hand2", command=lambda: self.bt_click("*")).grid(row=1, column=3, padx=1, pady=1)

        # Row 3
        four = tk.Button(btns_frame, text="4", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: self.bt_click(4)).grid(row=2, column=0, padx=1, pady=1)
        five = tk.Button(btns_frame, text="5", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: self.bt_click(5)).grid(row=2, column=1, padx=1, pady=1)
        six = tk.Button(btns_frame, text="6", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: self.bt_click(6)).grid(row=2, column=2, padx=1, pady=1)
        minus = tk.Button(btns_frame, text="-", width=10, height=3, bd=0, bg="#ffa500", cursor="hand2", command=lambda: self.bt_click("-")).grid(row=2, column=3, padx=1, pady=1)

        # Row 4
        one = tk.Button(btns_frame, text="1", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: self.bt_click(1)).grid(row=3, column=0, padx=1, pady=1)
        two = tk.Button(btns_frame, text="2", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: self.bt_click(2)).grid(row=3, column=1, padx=1, pady=1)
        three = tk.Button(btns_frame, text="3", width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: self.bt_click(3)).grid(row=3, column=2, padx=1, pady=1)
        plus = tk.Button(btns_frame, text="+", width=10, height=3, bd=0, bg="#ffa500", cursor="hand2", command=lambda: self.bt_click("+")).grid(row=3, column=3, padx=1, pady=1)

        # Row 5
        zero = tk.Button(btns_frame, text="0", width=21, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda: self.bt_click(0)).grid(row=4, column=0, columnspan=2, padx=1, pady=1)
        point = tk.Button(btns_frame, text=".", width=10, height=3, bd=0, bg="#eee", cursor="hand2", command=lambda: self.bt_click(".")).grid(row=4, column=2, padx=1, pady=1)
        equals = tk.Button(btns_frame, text="=", width=10, height=3, bd=0, bg="#ffa500", cursor="hand2", command=lambda: self.bt_equal()).grid(row=4, column=3, padx=1, pady=1)

    def bt_click(self, item):
        self.expression = self.expression + str(item)
        self.input_text.set(self.expression)

    def bt_clear(self):
        self.expression = ""
        self.input_text.set("")

    def bt_equal(self):
        try:
            result = str(eval(self.expression))
            self.input_text.set(result)
            self.expression = result
        except ZeroDivisionError:
            messagebox.showerror("Error", "Cannot divide by zero")
            self.bt_clear()
        except:
            messagebox.showerror("Error", "Invalid expression")
            self.bt_clear()

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
