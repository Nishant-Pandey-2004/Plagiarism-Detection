import tkinter as tk
from tkinter import messagebox, filedialog
import subprocess

class PlagiarismDetectorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Plagiarism Detector")
        self.root.geometry("800x600")
        self.root.configure(background="#f0f0f0")

        self.heading_label = tk.Label(root, text="Plagiarism Detector", font=("Arial", 20), bg="#f0f0f0")
        self.heading_label.pack(pady=(20, 10))

        self.offline_button = tk.Button(root, text="Check Plagiarism Offline", font=("Arial", 14), command=self.run_offline)
        self.offline_button.pack(pady=10)

        self.online_button = tk.Button(root, text="Check Plagiarism Online", font=("Arial", 14), command=self.run_online)
        self.online_button.pack(pady=10)

    def run_offline(self):
        # Execute offline.py file using subprocess
        subprocess.Popen(["python", "offline.py"])

    def run_online(self):
        # Execute online.py file using subprocess
        subprocess.Popen(["python", "online.py"])

if __name__ == "__main__":
    root = tk.Tk()
    app = PlagiarismDetectorApp(root)
    root.mainloop()
