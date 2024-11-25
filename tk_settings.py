import tkinter as tk

def open_tk_settings_window(root):
	settings_window = tk.Toplevel(root)
	settings_window.title("Settings")
	settings_window.geometry("525x200")

	settings_window_frame = tk.Frame(settings_window, padx=10, pady=10)
	settings_window_frame.pack(fill=tk.BOTH, expand=True)

	sw_col_1 = tk.Frame(settings_window_frame)
	sw_col_1.pack(side=tk.LEFT, fill=tk.BOTH, expand=False)

	sw_c1_frame = tk.LabelFrame(sw_col_1, text="Bin / Shelf Settings", width=250)
	sw_c1_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

	sw_c1_spacer = tk.Frame(sw_col_1, width=10)
	sw_c1_spacer.pack(side=tk.LEFT, fill=tk.BOTH)

	sw_col_2 = tk.Frame(settings_window_frame)
	sw_col_2.pack(side=tk.LEFT, fill=tk.BOTH, expand=False)

	sw_c2_frame = tk.LabelFrame(sw_col_2, text="General Settings", width=250)
	sw_c2_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
