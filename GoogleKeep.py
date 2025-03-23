import sqlite3
import json
import glob

# Connect to SQLite database (creates a file if not exists)
conn = sqlite3.connect("keep_notes.db")
cursor = conn.cursor()

# Create table
# cursor.execute("CREATE TABLE IF NOT EXISTS notes (id INTEGER PRIMARY KEY, text TEXT)")

# # Load JSON notes and insert into DB
# for file in glob.glob(r"C:\Users\al nada\Desktop\ollama\GoogleKeep\main.json"):
#         with open(file, "r", encoding="utf-8") as f:
#             data = json.load(f)
#             print(data.get("textContent", ""))
#         cursor.execute("INSERT INTO notes (text) VALUES (?)", (data["textContent"],))

# conn.commit()
# conn.close()
# print("Notes stored successfully!")


def search_notes(query):
    conn = sqlite3.connect("keep_notes.db")
    cursor = conn.cursor()

    # Basic text search (can be improved with full-text search)
    cursor.execute("SELECT text FROM notes WHERE text LIKE ?", ('%' + query + '%',))
    results = cursor.fetchall()
    conn.close()

    return " ".join([r[0] for r in results]) if results else "No relevant notes found."

# Example
# query = "Business Manager verification"
# context = search_notes(query)
# print("Retrieved Notes:", context)



#############################

import ollama

# Function to generate a response using Ollama
def ask_ollama(query):
    context = search_notes(query)  # Retrieve relevant notes
    response = ollama.chat(model="deepseek-r1:1.5b", messages=[
        {'role': 'system', 'content': 'Use the following notes: ' + context},
        {'role': 'user', 'content': query}
    ])
    return response['message']['content']

# Example Usage
query = "Business Manager verification"
answer = ask_ollama(query)
print("Ollama Response:", answer)
