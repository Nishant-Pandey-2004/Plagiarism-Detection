import tkinter as tk
from tkinter import messagebox, Text
from PIL import Image, ImageTk
import requests

class PlagiarismDetectorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Plagiarism Detector")
        self.root.geometry("600x400")
        self.root.configure(background="#f0f0f0")

        # Load and resize an image for the GUI using Pillow (PIL fork)
        image = Image.open("logo.png")  # Replace "logo.png" with your image file
        image = image.resize((150, 150), Image.LANCZOS)  # Resize with Lanczos resampling
        self.logo = ImageTk.PhotoImage(image)

        self.logo_label = tk.Label(root, image=self.logo, bg="#f0f0f0")
        self.logo_label.grid(row=0, column=0, padx=10, pady=10)

        self.heading_label = tk.Label(root, text="Plagiarism Detector", font=("Arial", 24), bg="#f0f0f0", fg="blue")
        self.heading_label.grid(row=0, column=1, columnspan=2, pady=(20,10))

        self.text_label = tk.Label(root, text="Enter Text:", font=("Arial", 16), bg="#f0f0f0", fg="black")
        self.text_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")
        self.text_entry = Text(root, width=50, height=10, font=("Arial", 12))
        self.text_entry.grid(row=1, column=1, columnspan=2, padx=10, pady=5, sticky="w")

        self.detect_button = tk.Button(root, text="Detect Plagiarism", font=("Arial", 16), command=self.detect_plagiarism_wikipedia, bg="green", fg="white")
        self.detect_button.grid(row=2, column=0, columnspan=3, pady=(20,10))

        self.root.grid_rowconfigure((3,4), weight=1)
        self.root.grid_columnconfigure((0,1,2), weight=1)

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
            'format': 'json',
            'srlimit': 10  # Limiting the number of search results to improve relevance
        }

        try:
            # Make the API request
            response = requests.get(url, params=params)
            data = response.json()

            # Extract search results if available
            if 'query' in data and 'search' in data['query']:
                search_results = data['query']['search']
                relevant_results = [result for result in search_results if self.is_relevant_result(result)]
                relevant_results_count = len(relevant_results)
                total_articles_count = data['query']['searchinfo']['totalhits']
                plagiarism_percentage = (relevant_results_count / total_articles_count) * 100
                return plagiarism_percentage
            else:
                return 0

        except Exception as e:
            print("Error occurred:", e)
            return 0

    def is_relevant_result(self, result):
        # Check if a search result is relevant based on specific criteria
        # You can customize this method to define relevance based on your requirements
        return 'title' in result and 'snippet' in result

if __name__ == "__main__":
    root = tk.Tk()
    app = PlagiarismDetectorApp(root)
    root.mainloop()
