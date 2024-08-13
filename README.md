
# 🏯 Otaku House Website API & UI Testing

## 🌟 Project Overview
Welcome to the Otaku House Website API and UI Testing Project! This suite ensures that the Otaku House eCommerce platform operates smoothly by validating both backend services and the user interface. Our goal is to guarantee a seamless and enjoyable shopping experience for all users.

## 🎯 Key Features
- **API Testing:** Validate backend services and ensure API endpoints are functioning as expected.
- **UI Testing:** Test the user interface for usability and compatibility across devices and browsers.
- **Functional Testing:** Verify core features like user registration, login, shopping cart, and checkout.

## 🔧 Tools & Technologies
- **Selenium:** Automating UI testing for cross-browser compatibility.
- **Postman:** API testing and endpoint validation.
- **Requests Library:** For API testing within Python scripts.
- **Pytest:** Test framework for running and managing test cases.
- **JIRA:** Track issues and manage project workflows.
- **Allure:** Generate and visualize test reports.

## 🚀 Quick Start

### 1. Clone the Repository
```bash
git clone https://github.com/AnanSa01/the_final_project
cd the_final_project
```

### 2. Set Up the Virtual Environment
```bash
python -m venv venv
venv\Scripts\activate # On Windows use
source venv/bin/activate  # On MacOS use
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Set Up the Local Website
To run the tests, you first need to set up the Otaku House website locally on your computer. Follow these steps:

- Clone the website repository from GitHub:
  ```bash
  git clone https://github.com/gagishmagi/ecommerce-django-react
  cd ecommerce-django-react
  ```
- **Update the Local Website's `requirements.txt`:**  
  Before running the website, update its `requirements.txt` file with the following dependencies:
  ```plaintext
  asgiref==3.8.1
  Django==5.1
  django-cors-headers==4.4.0
  djangorestframework==3.15.2
  djangorestframework-simplejwt==5.3.1
  gunicorn==23.0.0
  Pillow==10.4.0
  #psycopg2==2.9.3
  PyJWT==2.9.0
  pytz==2024.1
  sqlparse==0.5.1
  whitenoise==6.7.0
  ```
- Follow the instructions in the README of that repository to set up and run the website locally.

### 5. Run Tests
After setting up the website, you can run the tests:
```bash
python run_tests.py
```

## 🎨 Design Highlights
- **Responsive Design:** Ensures readability and usability across all screen sizes.
- **Custom Banners:** Visual elements like the Otaku House banner add a personal touch.
- **Clear Structure:** Sections are organized for easy navigation and understanding.

## 🛠 Project Structure
```bash
the_final_project/
├── infra/
├── logic/
├── tests/
│   ├── api/
│   ├── api_and_ui/
│   └── ui/
├── reports/
├── requirements.txt
└── README.md
```

## 📊 Allure Reporting

### Install Allure
```bash
npm install -g allure-commandline
```

### Run and Serve Reports
```bash
pytest --alluredir=./reports
allure serve reports
```

## 👥 Contributing
We welcome contributions! Here’s how you can get involved:

1. Fork the repository and create a new branch.
2. Make your changes and commit them with a meaningful message.
3. Push to the branch and submit a pull request.

## 📬 Contact Information
For now, placeholder info. Update it later!

- **Name:** Anan
- **Email:** an.sabek01@gmail.com
- **GitHub:** [AnanSa01](https://github.com/AnanSa01/the_final_project)
