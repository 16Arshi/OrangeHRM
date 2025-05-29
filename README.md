# 🔐 OrangeHRM Login Page Automation Testing

This project contains automated test scripts for the **Login Page** of the [OrangeHRM](https://opensource-demo.orangehrmlive.com/) application. The testing is performed using **Selenium WebDriver**, **Python**, and **Pytest**, with a **data-driven approach** using Excel.

## 📌 Project Highlights

- ✅ Login functionality tested with multiple sets of credentials (valid & invalid)
- ✅ Data-driven testing using Excel (`openpyxl`)
- ✅ Logging implemented for test steps and results
- ✅ Screenshots captured for failures
- ✅ Test result verification using dynamic waits (Selenium `WebDriverWait`)
- ✅ Clean test structure using Page Object Model (POM)

---

## 📂 Project Structure

orangehrm_project/
│
├── base_pages/
│ └── test_login_page.py # Page Object Model for login page
│
├── test_pages/
│ └── test_login_datadriven.py # Main test script
│ └── conftest.py # Pytest fixture for setup/teardown
│
├── utilities/
│ ├── excel_utilis.py # Excel read/write utilities
│ ├── read_properties.py # Configuration reader
│ └── custom_logger.py # Logger setup
│
├── test_data/
│ └── orangehrm.xlsx # Excel file containing login test data
│
├── screenshots/ # Folder for screenshots on failure
│
├── report.html # Optional HTML report (if using pytest-html)
│
└── README.md # This file


---

## ⚙️ Tools & Technologies

- Python 3.x
- Selenium WebDriver
- Pytest
- openpyxl
- Pytest-html (optional for reports)
- Logging module

---

## 🧪 How to Run the Test

1. **Install Dependencies**  
   Run the following in your terminal or command prompt:

   ```bash
   pip install -r requirements.txt
   
2. Run the Test
pytest test_pages/test_login_datadriven.py --html=report.html

🔍 Test Case Summary

Test Case	Description

1. Title Verification	                 -    Verifies the page title
2. Login with Valid Credentials	       -    Logs in with valid credentials
3. Login with Invalid Credentials      -  	Verifies login fails as expected

📌 Note
This project only covers Login Page Testing.

More modules and end-to-end scenarios will be added in the future.


