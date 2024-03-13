import tkinter as tk
from tkinter import messagebox, Text
import requests

class PlagiarismDetectorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Plagiarism Detector")
        self.root.geometry("500x300")
        self.root.configure(background="#f0f0f0")

        self.heading_label = tk.Label(root, text="Plagiarism Detector", font=("Arial", 20), bg="#f0f0f0")
        self.heading_label.grid(row=0, column=0, columnspan=2, pady=(20,10))

        self.text_label = tk.Label(root, text="Enter Text:", font=("Arial", 12), bg="#f0f0f0")
        self.text_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")
        self.text_entry = Text(root, width=40, height=10, font=("Arial", 12))
        self.text_entry.grid(row=1, column=1, padx=10, pady=5, sticky="w")

        self.detect_button = tk.Button(root, text="Detect Plagiarism (Wikipedia)", font=("Arial", 14), command=self.detect_plagiarism_wikipedia)
        self.detect_button.grid(row=2, column=0, columnspan=2, pady=(20,10))

        # Configure row and column weights to make the window expandable
        self.root.grid_rowconfigure((3,4), weight=1)
        self.root.grid_columnconfigure((0,1), weight=1)

    def detect_plagiarism_wikipedia(self):
        text = self.text_entry.get("1.0", tk.END).strip()

        if not text:
            messagebox.showerror("Error", "Please enter some text.")
            return

        plagiarism_percentage = self.search_similar_text_wikipedia(text)
        messagebox.showinfo("Wikipedia Plagiarism Detection", f"Plagiarism percentage: {plagiarism_percentage:.2f}%")

    def search_similar_text_wikipedia(self, text):
        # Wikipedia API URL
        url = 'https://en.wikipedia.org/w/api.php'

        # Parameters for the API request
        params = {
            'action': 'query',
            'list': 'search',
            'srsearch': text,
            'format': 'json'
        }

        try:
            # Make the API request
            response = requests.get(url, params=params)
            data = response.json()

            # Extract search results if available
            if 'query' in data and 'search' in data['query']:
                search_results_count = len(data['query']['search'])
                total_articles_count = data['query']['searchinfo']['totalhits']
                plagiarism_percentage = (search_results_count / total_articles_count) * 100
                return plagiarism_percentage
            else:
                return 0

        except Exception as e:
            print("Error occurred:", e)
            return 0

if __name__ == "__main__":
    root = tk.Tk()
    app = PlagiarismDetectorApp(root)
    root.mainloop()
