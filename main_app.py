import tkinter as tk

class burp_app:
	def __init__(self, tk_root):
		self.tk_root = tk_root
		self.tk_root.title('Main Window')
		self.tk_root.geometry("900x450")

if __name__ == '__main__':
	root = tk.Tk()
	app = burp_app(root)
	root.mainloop()
