import tkinter as tk
from tkinter import messagebox
import requests

# Function to search online
def search_medical_info():
    query = entry.get()
    if not query:
        messagebox.showwarning("Input Error", "Please enter a medical term to search!")
        return
    
    # Replace with your API Key and Custom Search Engine ID
    API_KEY = "your_api_key"
    CX = "your_custom_search_engine_id"
    url = f"https://www.googleapis.com/customsearch/v1?q={query}&key={API_KEY}&cx={CX}"
    
    try:
        response = requests.get(url)
        data = response.json()
        results = data.get("items", [])
        if results:
            output_text.delete("1.0", tk.END)
            for result in results[:5]:  # Show top 5 results
                output_text.insert(tk.END, f  
