# CPNS 2024 Formasi

This Python script streamlines the process for CPNS 2024 candidates to retrieve and export detailed information on job placements (formasi) aligned with their academic programs. It efficiently handles paginated API responses to gather complete data.

## Requirements

- Python 3.x https://www.python.org/downloads/
- `requests` library: `pip3 install requests`
- `pandas` library: `pip3 install pandas`
- `openpyxl` library (optional, for improved Excel formatting): `pip3 install openpyxl`

## Usage

1. **Install dependencies:**

   ```bash
   pip3 install requests pandas openpyxl
   ```

2. Modify the code:

- Replace `5100144` in the code with your actual `kode_ref_pend` (program study reference code). You can find this code from official CPNS resources or by browsing available programs on the BKN website (https://sscasn.bkn.go.id).

3. Run the script:

   ```bash
   python3 main.py
   ```

## Output

The script will generate an Excel file named `data_formasi_{kode_ref_pend}.xlsx` containing job placement data for your program study.

## Explanation

- `requests` library: Used for interacting with the BKN API and retrieving data.
- `pandas` library: Parses the retrieved data into a Pandas DataFrame for easier manipulation and export.
- `openpyxl` library: (Optional) Improves Excel formatting for numerical columns.

## Disclaimer

This script is provided for educational purposes only. It's recommended to use official CPNS resources (https://sscasn.bkn.go.id) for accurate information and application procedures. The script assumes the API's structure will remain consistent.

## Acknowledgements

This script was developed to assist CPNS 2024 candidates in finding suitable job placements (formasi). Special thanks to the BKN for providing the API and data.
