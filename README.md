📑 Otaku House Automation Suite

📌 Project Overview
Welcome to the Otaku House Automation Suite! This project provides a comprehensive suite for automating the testing of Trello's UI and API functionalities. Leveraging industry-standard tools, this suite ensures that Trello's key features are both stable and performant.

🔑 Features
UI Automation: Automate and validate Trello's user interface using Selenium WebDriver.
API Testing: Perform in-depth testing of Trello's API endpoints with the Requests library.
Integrated Reporting: Generate detailed test reports with the Allure framework.
Jira Integration: Seamlessly manage and track test issues using Jira.
🎯 Test Scope
UI Tests: Ensure the core functionalities of Trello’s UI are working as expected.
API Tests: Validate critical Trello API endpoints for accuracy and performance.
Combined Tests: Demonstrate integration and interaction between UI and API tests.
🛠 Setup Instructions
Clone the Repository:

bash
Copy code
git clone https://github.com/imad-Ra/Trello_Final_Project.git
cd Trello_Final_Project
Install Dependencies:

bash
Copy code
pip install -r requirements.txt
Configure Environment Variables:

bash
Copy code
cp .env.example .env
Edit the .env file to include your Trello API key and token.

▶ Running Tests
UI Tests:

bash
Copy code
pytest test/web
API Tests:

bash
Copy code
pytest api/tests
Run All Tests with Allure Reporting:

bash
Copy code
pytest --alluredir=./reports
allure serve reports
🛠 Tools and Technologies
IDE: PyCharm 2024.1.1
Automation Framework: Selenium 4.22.0
Programming Language: Python 3.8+
Browser: Google Chrome 126.0.6478.127
API Testing: Requests library
Test Framework: Pytest
Reporting: Allure Framework
Version Control: Git
Bug Tracking: Jira
📊 Allure Reporting
To utilize Allure for test reporting:

Install Allure Command-Line Tool:

bash
Copy code
npm install -g allure-commandline
Generate and Serve the Allure Report:

bash
Copy code
pytest --alluredir=./reports
allure serve reports
🔗 API Reference
This project integrates with Trello's official REST API. For detailed API documentation, visit the Trello REST API Documentation.

Our test suite covers key API endpoints to ensure comprehensive validation of Trello's functionality.

📘 Documentation
Alongside the code, this project includes:

Software Test Plan (STP): Detailed strategy and approach for testing.
Test Cases Document: Comprehensive documentation of test cases in Word (STD file).
Postman Collections: For API testing and validation.
Detailed README: For project overview and setup instructions.
🙏 Acknowledgements
Special thanks to:

Trello API
Selenium
Pytest
Allure Framework
Jira
🤝 Contributing
We welcome contributions to this project! To contribute:

Fork the repository.
Create a feature branch:
bash
Copy code
git checkout -b feature/NewFeature
Commit your changes:
bash
Copy code
git commit -am 'Add NewFeature'
Push to the branch:
bash
Copy code
git push origin feature/NewFeature
Submit a pull request.
📞 Contact
For any questions or suggestions, feel free to reach out:

Name: Anan Sa
Email:an.sabek01@gmail.com
GitHub: AnanSa01
