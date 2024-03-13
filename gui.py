import tkinter as tk
from tkinter import filedialog, messagebox
from rabin_karp import RabinKarp

class PlagiarismDetectorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Plagiarism Detector")
        self.root.geometry("500x250")
        self.root.configure(background="#f0f0f0")

        self.heading_label = tk.Label(root, text="Plagiarism Detector", font=("Arial", 20), bg="#f0f0f0")
        self.heading_label.grid(row=0, column=0, columnspan=3, pady=(20,10))

        self.file1_label = tk.Label(root, text="File 1:", font=("Arial", 12), bg="#f0f0f0")
        self.file1_label.grid(row=1, column=0, padx=(10,5), pady=5, sticky="e")
        self.file1_entry = tk.Entry(root, width=40, font=("Arial", 12))
        self.file1_entry.grid(row=1, column=1, padx=(0,10), pady=5, sticky="w")
        self.file1_button = tk.Button(root, text="Browse", font=("Arial", 12), command=self.browse_file1)
        self.file1_button.grid(row=1, column=2, pady=5, sticky="w")

        self.file2_label = tk.Label(root, text="File 2:", font=("Arial", 12), bg="#f0f0f0")
        self.file2_label.grid(row=2, column=0, padx=(10,5), pady=5, sticky="e")
        self.file2_entry = tk.Entry(root, width=40, font=("Arial", 12))
        self.file2_entry.grid(row=2, column=1, padx=(0,10), pady=5, sticky="w")
        self.file2_button = tk.Button(root, text="Browse", font=("Arial", 12), command=self.browse_file2)
        self.file2_button.grid(row=2, column=2, pady=5, sticky="w")

        self.detect_button = tk.Button(root, text="Detect Plagiarism", font=("Arial", 14), command=self.detect_plagiarism)
        self.detect_button.grid(row=3, column=0, columnspan=3, pady=(20,10))

        # Configure row and column weights to make the window expandable
        self.root.grid_rowconfigure(4, weight=1)
        self.root.grid_columnconfigure((0,1,2), weight=1)

    def browse_file1(self):
        file_path = filedialog.askopenfilename()
        self.file1_entry.delete(0, tk.END)
        self.file1_entry.insert(0, file_path)

    def browse_file2(self):
        file_path = filedialog.askopenfilename()
        self.file2_entry.delete(0, tk.END)
        self.file2_entry.insert(0, file_path)

    def detect_plagiarism(self):
        file1_path = self.file1_entry.get()
        file2_path = self.file2_entry.get()

        try:
            with open(file1_path, 'r') as f1, open(file2_path, 'r') as f2:
                text1 = f1.read()
                text2 = f2.read()
            
            plagiarism_detector = RabinKarp(text1, text2)
            plagiarism_rate = plagiarism_detector.check_similarity()
            if plagiarism_rate > 0:
                messagebox.showinfo("Plagiarism Detected", f"Plagiarism detected!\nPlagiarism rate: {plagiarism_rate:.2f}%")
            else:
                messagebox.showinfo("No Plagiarism Detected", "No plagiarism detected.")

        except FileNotFoundError:
            messagebox.showerror("Error", "Please select valid files.")

if __name__ == "__main__":
    root = tk.Tk()
    app = PlagiarismDetectorApp(root)
    root.mainloop()
