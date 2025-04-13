# 🚀 eBay Helpers

🔍 A set of tools to help you manage and analyze eBay products efficiently. Whether you're looking for product details or automating searches, these scripts have got you covered.

## ✨ Description

This project includes two main components: a Flask web application (`app.py`) and a Python script (`main.py`). The web app allows users to search for products and view their details in real-time, while the script automates eBay product searches and displays them in a tabulated format. Perfect for market analysis, inventory management, or just keeping up with trending items.

## 🚀 Features

- **Flask Web Application**:
  - Search for products using keywords.
  - View detailed information about each product.
  - Keep track of search queries and their results.

- **Automated Product Search Script**:
  - Automate the process of searching for products on eBay.
  - Filter products by price range.
  - Display results in a tabulated format.

## 🛠️ Installation

### Prerequisites
- Python 3.8+
- pip (Python package installer)

### Installation Steps

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/gag3301v/ebayhelpers.git
   cd ebayhelpers
   ```

2. **Install Dependencies**:
   - For the Flask web app:
     ```bash
     pip install flask apscheduler
     ```
   - For the product search script:
     ```bash
     pip install beautifulsoup4 tabulate undetected-chromedriver colorama
     ```

## 📦 Usage

### Running the Flask Web App

1. **Run the Application**:
   ```bash
   python app.py
   ```

2. **Access the Web Interface**:
   Open your web browser and navigate to `http://127.0.0.1:80`. You should see the home page where you can start searching for products.

### Running the Product Search Script

1. **Execute the Script**:
   ```bash
   python main.py
   ```

2. **View Results**:
   The script will print search results in a tabulated format to your terminal.

## 🔧 Configuration (if applicable)

- **Flask Web App**: No additional configuration required.
- **Product Search Script**:
  - Ensure `undetected_chromedriver` is installed and working correctly. You may need to download the appropriate ChromeDriver binary and set it up in your system PATH.

## 🧪 Tests

No automated tests are provided at this time.

## 📁 Project Structure

```
ebayhelpers/
├── app.py
├── main.py
├── requirements.txt
└── README.md
```

- `app.py`: The Flask web application.
- `main.py`: The Python script for automated product searches.
- `requirements.txt`: Lists all dependencies required for the project.

## 🙌 Contributing

Contributions are welcome! Please read our [CONTRIBUTING](CONTRIBUTING.md) guidelines before submitting a pull request.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Developed with ❤️ by [@gag3301v](https://github.com/gag3301v)

[![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)