----Selenium Automation Framework (Python + Pytest + POM)----

Project Overview :
This project is a UI automation framework built using Selenium WebDriver with Python. It follows the Page Object Model (POM) design pattern to ensure maintainability and scalability of test cases.

The framework automates key user flows on the Automation Exercise website, including login, navigation, and validation scenarios.

Tech :
- Python
- Selenium WebDriver
- Pytest
- Page Object Model (POM)


Project Structure:

selenium-project-automationexercise/
    /pageobject/ # Page classes (POM)
    /logs # logger
    /reports # html report generation
    /testcases/ # Test cases to automate
    /utility/ # Common reusable functions
    /conftest.py # Pytest fixtures
    /requirements.txt # package installation
    /testdata # data to use in automation
    /screenshots # take failed screenshots

Features :
- Structured using Page Object Model (POM)
- Reusable page classes and methods
- Pytest fixtures 
- Automated key user workflows:
  - Login functionality
  - Register/Sign Up functionality
  - Navigation flows
  - Validation checks
  - search functionality and validate
  

