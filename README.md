# Website Status Checker

This Python script checks your current IP and compares it to the contents of the JSON file, updating it if necessary.

## Prerequisites

- Python 3.x
- Required Python packages: `requests`

## Usage

1. Clone this repository or download the Python script to your local machine.
2. Ensure you have Python 3.x installed on your system.
3. Install the required Python packages using pip:

    `pip install requests`


4. Prepare a JSON file. The JSON file should have the following structure:

```json
{
    "OldIP": "0.0.0.0",
    "NewIP": "0.0.0.0",
    "IPChangeTime": ""
}
```

Run the script using the following command:

    python ip_checker.py
