# 🛠️ JSON to CSV Converter

## 👨‍💻 Author: Or Pinto

This project provides a CLI tool for converting nested JSON structures into a flat and readable CSV format. The tool employs a recursive Depth-First Search (DFS) approach to flatten nested JSON objects into a single-level dictionary, ensuring that the hierarchical structure is preserved in the keys.

---

## ❓ Problem Statement

Dealing with nested JSON structures can be a real headache, especially when trying to analyze or process the data in tabular formats like CSV. Nested JSONs often contain dictionaries and arrays, making it tricky to represent them in a flat structure. This tool swoops in to save the day 🦸‍♂️ by flattening the JSON into a format that's super easy to work with in tools like Excel or data analysis libraries.

---

## 💡 Solution

The tool uses a recursive DFS algorithm to iterate through each nested JSON block. It flattens the structure by:
1. **📂 Handling Nested Dictionaries**: Keys are concatenated with a separator (`/` by default) to preserve the hierarchy.
2. **📋 Handling Arrays**: Arrays are stored as JSON-like strings in the CSV, ensuring that they remain compact and readable.
3. **✅ Primitive Values**: Non-nestable values (e.g., strings, numbers) are directly added to the flattened structure.

---

## ✨ Features

- 🔄 **Recursive Flattening**: Handles deeply nested JSON structures.
- 📦 **Array Handling**: Preserves arrays as single key-value pairs in the CSV.
- ⚙️ **Customizable Separator**: Allows customization of the separator used for nested keys.
- 🚨 **Error Handling**: Provides meaningful error messages for invalid or empty JSON files.

---

## 🚀 Usage

### 🛠️ Prerequisites
- 🐍 Python 3.x
- 📦 `typer` library (for CLI functionality)

### 📥 Installation
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```

2. Ensure you have Python 3.x installed. Then, create and activate a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies using `requirements.txt`:
   ```bash
   pip install -r requirements.txt
   ```

   This will install the `typer` library and any other required dependencies.

### ▶️ Running the Tool
To convert a JSON file to a CSV file, run:
```bash
python main.py <input_json_path> <output_csv_path>
```

#### Example:
```bash
python main.py src.json output.csv
```

---

### 🐳 Running with Docker

1. Build the Docker image:
   ```bash
   docker build -t json-to-csv .
   ```

2. Run the Docker container:
   ```bash
   docker run -v $(pwd):/app json-to-csv <input_json_path> <output_csv_path>
   ```

   Replace `<input_json_path>` with the path to your JSON file and `<output_csv_path>` with the desired path for the CSV file.

---