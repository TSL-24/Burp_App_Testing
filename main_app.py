import tkinter as tk

class burp_app:
	def __init__(self, tk_root):
		self.tk_root = tk_root
		self.tk_root.title('Main Window')
		self.tk_root.geometry('1100x600')

		# Main Window
		self.main_frame = tk.Frame(self.tk_root, padx=10, pady=10)
		self.main_frame.pack(fill=tk.BOTH, expand=True)

		# Column 1 - Main Window
		self.mf_col_1 = tk.Frame(self.main_frame)
		self.mf_col_1.pack(side=tk.LEFT, fill=tk.BOTH, expand=False)

		# Frame - Column 1 - Main Window
		self.mf_c1_frame = tk.LabelFrame(self.mf_col_1, text="Navigation", padx=10)
		self.mf_c1_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=False)

		# Navigation Buttons
		self.mf_c1_nav_button_1 = tk.Button(self.mf_c1_frame, text="Bin Overview", padx=100, command=lambda: open_tk_bin_overview_window(self.tk_root))
		self.mf_c1_nav_button_1.pack(fill=tk.X)

		self.mf_c1_nav_button_2 = tk.Button(self.mf_c1_frame, text="Bin Manager", padx=100, command=lambda: open_tk_bin_manager_window(self.tk_root))
		self.mf_c1_nav_button_2.pack(fill=tk.X)

		self.mf_c1_nav_button_3 = tk.Button(self.mf_c1_frame, text="Settings", padx=100, command=lambda: open_tk_settings_window(self.tk_root))
		self.mf_c1_nav_button_3.pack(fill=tk.X)

		# Column 2 - Main Window
		self.mf_col_2 = tk.Frame(self.main_frame, padx=10)
		self.mf_col_2.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

		# Row 1 - Column 2 - Main Window
		self.mf_c2_row_1 = tk.LabelFrame(self.mf_col_2, text="Current System Status")
		self.mf_c2_row_1.pack(fill=tk.BOTH, expand=True)

		# Row 2 - Column 2 - Main Window
		self.mf_c2_row_2 = tk.LabelFrame(self.mf_col_2, text="Activity Log")
		self.mf_c2_row_2.pack(fill=tk.BOTH, expand=True)

		# Activity Log Text Box
		self.mf_c2_r2_textlog = tk.Text(self.mf_c2_row_2, height=15, state="disabled")
		self.mf_c2_r2_textlog.pack(fill=tk.BOTH, padx=10, pady=10)

if __name__ == '__main__':
	root = tk.Tk()
	app = burp_app(root)
	root.mainloop()
