# 🛠️ JSON to CSV Converter

## 👨‍💻 Author: Or Pinto

This project provides a CLI tool for converting nested JSON structures into a flat and readable CSV format. The tool is designed to handle JSON data files mimicking MongoDB collections and convert them into SQL-like tabular data. It addresses challenges such as schema handling, nested data, and array fields.

---

## ❓ Problem Statement

Dealing with nested JSON structures can be a real headache, especially when trying to analyze or process the data in tabular formats like CSV. Nested JSONs often contain dictionaries and arrays, making it tricky to represent them in a flat structure. This tool solves these challenges by flattening the JSON into a format that's easy to work with in tools like Excel or SQL databases.

---

## 💡 Solution

The tool uses a recursive DFS algorithm to iterate through each nested JSON block. It flattens the structure by:
1. **📂 Handling Nested Dictionaries**: Keys are concatenated with a separator (`/` by default) to preserve the hierarchy.
2. **📋 Handling Arrays**: Arrays are stored as JSON-like strings in the CSV, ensuring that they remain compact and readable.
3. **✅ Primitive Values**: Non-nestable values (e.g., strings, numbers) are directly added to the flattened structure.

### Design Decisions
- **Schema Handling**: The tool dynamically generates a schema by analyzing the keys in the JSON data. This ensures compatibility with schema-less NoSQL data.
- **Nested Data**: Nested objects are flattened using a customizable separator to maintain hierarchy in the keys.
- **Data Types**: The tool assumes consistent data types for each key. If inconsistencies are detected, they are logged for review.
- **Array Fields**: Arrays are converted into JSON-like strings to preserve their structure in a single column.

---

## ✨ Features

- 🔄 **Recursive Flattening**: Handles deeply nested JSON structures.
- 📦 **Array Handling**: Preserves arrays as single key-value pairs in the CSV.
- ⚙️ **Customizable Separator**: Allows customization of the separator used for nested keys.
- 🚨 **Error Handling**: Provides meaningful error messages for invalid or empty JSON files.
- 🆘 **About Command**: Displays information about the tool and its usage.
- 🧪 **Unit Tests**: Includes tests for the data transformation logic.

---

## 🚀 Usage

### 🛠️ Prerequisites
- 🐍 Python 3.x
- 📦 `typer` library (for CLI functionality)
- 🧪 `pytest` (for testing)

### 📥 Installation
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

### ▶️ Running the Tool
To convert a JSON file to a CSV file, run:
```bash
python main.py convert <input_json_path> <output_csv_path>
```

#### Example:
```bash
python main.py convert src.json output.csv
```

### ℹ️ About Command
To display information about the tool, run:
```bash
python main.py about
```

This will print a brief description of the tool and its usage.

---

## 🧪 Unit Testing

Unit tests are included to validate the data transformation logic. To run the tests, use:
```bash
pytest test_main.py
```

This will execute all the test cases defined in the `test_main.py` file to ensure the correctness of the data transformation logic.

---

## 🐳 Docker Support

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

## 🛠️ Development Environment

This project uses a virtual environment for dependency management. A `requirements.txt` file is provided for reproducible builds. To set up the environment:
1. Create a virtual environment:
   ```bash
   python -m venv venv
   ```

2. Activate the virtual environment:
   ```bash
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## 📋 Challenges Addressed

### Schema Handling
The tool dynamically generates a schema by analyzing the keys in the JSON data, ensuring compatibility with schema-less NoSQL data.

### Nested Data
Nested objects are flattened using a customizable separator to maintain hierarchy in the keys.

### Data Types
The tool assumes consistent data types for each key. If inconsistencies are detected, they are logged for review.

### Array Fields
Arrays are converted into JSON-like strings to preserve their structure in a single column.

---

## 📦 Deliverables

- Complete Python CLI application code
- Unit tests
- Sample JSON data files
- A comprehensive README.md
- Dockerfile
- `requirements.txt` for dependencies