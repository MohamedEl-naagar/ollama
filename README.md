# Keep Notes Search with SQLite and Ollama

## Overview
This project provides a simple way to store and search Google Keep notes in an SQLite database and use Ollama for generating responses based on stored notes.

## Features
- Stores Google Keep notes in an SQLite database
- Searches for relevant notes using text-based queries
- Uses Ollama to generate AI-driven responses based on stored notes

## Prerequisites
Ensure you have the following installed:
- Python 3.x
- SQLite3 (included with Python)
- Ollama Python package (`ollama`)

## Installation
1. Clone the repository or copy the script.
2. Install required dependencies:
   ```bash
   pip install ollama
   ```
3. Ensure the `main.json` file containing Google Keep notes is available at the specified path.

## Usage

### Storing Notes
Uncomment the following lines in the script to store notes in the SQLite database:
```python
cursor.execute("CREATE TABLE IF NOT EXISTS notes (id INTEGER PRIMARY KEY, text TEXT)")
for file in glob.glob(r"C:\Users\al nada\Desktop\ollama\GoogleKeep\main.json"):
    with open(file, "r", encoding="utf-8") as f:
        data = json.load(f)
    cursor.execute("INSERT INTO notes (text) VALUES (?)", (data["textContent"],))
conn.commit()
conn.close()
print("Notes stored successfully!")
```
Run the script once to save notes in the database.

### Searching Notes
To search for a keyword in stored notes:
```python
query = "Business Manager verification"
context = search_notes(query)
print("Retrieved Notes:", context)
```

### Generating AI Responses with Ollama
To get an AI-generated response based on stored notes:
```python
query = "Business Manager verification"
answer = ask_ollama(query)
print("Ollama Response:", answer)
```

## Notes
- The search function performs a basic SQL `LIKE` query. It can be enhanced using full-text search (FTS) in SQLite.
- Ensure the Ollama model (`deepseek-r1:1.5b`) is available. You may need to change the model name based on your setup.

## License
This project is open-source. Feel free to modify and improve it!

