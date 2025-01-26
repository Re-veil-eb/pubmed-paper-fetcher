# PubMed Paper Fetcher

## **Overview**

The PubMed Paper Fetcher is a Python-based command-line tool that allows users to fetch research papers from PubMed using a query string, filter them for non-academic author affiliations (e.g., authors from pharmaceutical or biotech companies), and save the results to a CSV file.

---

## **Code Organization**

The project is structured as follows:

```
pubmed-paper-fetcher/
├── pubmed_paper_fetcher/       # Core package containing all the main logic.
│   ├── __init__.py             # Package initializer (empty, marks the folder as a Python package).
│   ├── cli.py                  # Command-line interface (CLI) entry point.
│   ├── fetch_papers.py         # Logic for fetching paper IDs from PubMed API.
│   └── process_papers.py       # Logic for processing paper details and extracting data.
├── tests/                      # Test suite for unit and integration tests.
│   ├── __init__.py             # Test package initializer.
│   └── test_fetch_papers.py    # Tests for the fetch_papers module.
├── README.md                   # Project documentation (this file).
├── pyproject.toml              # Poetry configuration file (handles dependencies, packaging, and metadata).
├── poetry.lock                 # Lock file for dependencies (ensures consistency in environments).
└── results.csv                 # Example output file with paper details (generated when the CLI is run).
```

**Explanation of Key Files**:

1. **`cli.py`**:

   - Entry point for the command-line tool.
   - Handles parsing command-line arguments and invoking the appropriate functions.
   - Example: Fetching research papers and saving results to a file.

2. **`fetch_papers.py`**:

   - Contains functions to query the PubMed API and fetch a list of paper IDs based on the user's query.

3. **`process_papers.py`**:

   - Handles processing of paper metadata, filtering authors with company affiliations, and extracting details like title, publication date, and corresponding author email.

4. **`tests/test_fetch_papers.py`**:

   - Unit tests to verify the correctness of functions in `fetch_papers.py`.
   - Example: Testing edge cases like empty queries and API timeouts.

5. **`pyproject.toml`**:
   - Defines project metadata, dependencies, and scripts.
   - Includes the `get-papers-list` script, which maps to the CLI entry point.

---

## **Installation Instructions**

### **Prerequisites**

- Python 3.12 or higher.
- Poetry (for dependency management and packaging). Install Poetry using:
  ```bash
  pip install poetry
  ```

---

### **Setup**

1. Clone the repository:

   ```bash
   git clone https://github.com/<your-username>/pubmed-paper-fetcher.git
   cd pubmed-paper-fetcher
   ```

2. Install the dependencies using Poetry:

   ```bash
   poetry install
   ```

3. Verify the installation:
   ```bash
   poetry check
   ```

---

### **Usage**

To run the tool, use the following command:

```bash
poetry run get-papers-list "<query>" -f <output_file.csv> -d
```

**Options**:

- `<query>`: The search query for PubMed (e.g., `"cancer research"`).
- `-f, --file`: Optional. File to save the results (e.g., `results.csv`). If not provided, results will be printed to the console.
- `-d, --debug`: Optional. Enable debug mode to display additional information during execution.

**Examples**:

1. Fetch papers about "cancer research" and save them to `results.csv`:

   ```bash
   poetry run get-papers-list "cancer research" -f results.csv
   ```

2. Fetch papers with debug information enabled:
   ```bash
   poetry run get-papers-list "machine learning" -d
   ```

---

## **Tools and Libraries Used**

1. **PubMed API**:

   - Source of data for fetching research papers.
   - Official documentation: [PubMed API Documentation](https://www.ncbi.nlm.nih.gov/books/NBK25499/).

2. **Click**:

   - Used to build the command-line interface (CLI).
   - Documentation: [Click - Python CLI Library](https://click.palletsprojects.com/).

3. **Poetry**:

   - For dependency management and packaging.
   - Documentation: [Poetry - Python Dependency Management](https://python-poetry.org/).

4. **Pandas**:

   - For data handling and exporting results to CSV files.
   - Documentation: [Pandas - Python Data Analysis Library](https://pandas.pydata.org/).

5. **Requests**:
   - For making HTTP requests to the PubMed API.
   - Documentation: [Requests - HTTP for Humans](https://docs.python-requests.org/).

---

## **Execution Flow**

1. **CLI**: The `cli.py` script handles user input via command-line arguments.
2. **Fetch Paper IDs**: The query is sent to the PubMed API, and a list of paper IDs is fetched.
3. **Process Papers**: For each paper ID, details like title, authors, and affiliations are fetched and processed.
4. **Save or Display**: Results are either saved to a file or displayed in the console.

---

## **Testing**

This project includes a suite of tests to ensure functionality and robustness.

### **Run Tests**

Execute the tests using:

```bash
poetry run pytest
```

### **Example Test Scenarios**

- Fetching paper IDs with a valid query.
- Handling empty queries gracefully.
- Simulating API failures or timeouts.

---

## **License**

This project is licensed under the MIT License. See the `LICENSE` file for more details.

---
