This repository contains **Python + Selenium** automation tests as an assessment for the Sentact.  
It demonstrates how to validate UI components, such as **navigation dropdowns** and **form submissions**, using a modern Selenium and Pytest setup.

**ADD DEPENDENCIES**
pip install -r requirements.txt

**You can run all tests using pytest by using the command:**
pytest -v
**RUNNING A SINGLE TEST FILE**
pytest tests/test_nav_dropdown.py -v
pytest tests/test_contact_form.py -v

**TEST DETAILS**

**Navigation Dropdown Test**

File: tests/test_nav_dropdown.py
Purpose: Verifies that top navigation menus (e.g., “Solutions”) expand when hovered and collapse when the mouse moves away.
Checks include:
1. Dropdown becomes visible on hover.
2. Expected submenu items are displayed.
3. Dropdown collapses correctly when focus moves away.

**Contact Form Test**

File: tests/test_contact_form.py
Purpose: Automates submission of the Contact Us form.
Checks include:
1. All input fields are visible and can be filled.
2. Form submission triggers a success message.
3. Basic UI validation and field presence.

**TECH STACK**
Language: Python 3.10+
Framework: Pytest
Automation Tool: Selenium WebDriver
Browser: Google Chrome

**Author**

Pranav Kapadnis
QA Automation and Manual Tester
awerora.kapadnis@gmail.com
