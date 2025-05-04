# Cyber-Guardian-Scanner
this is website vulnerability scanner mocking real vulnerability scanner

## 💡 Disclaimer

**CyberGuardian AI is a demonstration tool and should not be used for actual security assessments.** It does not perform real vulnerability scanning. The reported vulnerabilities are simulated for illustrative purposes only. For genuine security testing, please use professional-grade vulnerability scanning tools and consult with security experts.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## ❤️ Acknowledgements

* Inspired by the functionality of real-world web vulnerability scanners.
* Built using the Flask framework for the backend and standard web technologies for the frontend.

---


# CyberGuardian AI - Mock Web Vulnerability Scanner

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://github.com/your-username/cyberguardian-ai/graphs/commit-activity)
[![Built With Python](https://img.shields.io/badge/Built%20With-Python-blue.svg?style=flat-square&logo=python)](https://www.python.org/)
[![Built With JavaScript](https://img.shields.io/badge/Built%20With-JavaScript-yellow.svg?style=flat-square&logo=javascript)](https://www.javascript.com/)
[![Built With Flask](https://img.shields.io/badge/Built%20With-Flask-brightgreen.svg?style=flat-square&logo=flask)](https://flask.palletsprojects.com/)

**CyberGuardian AI** is a web application that provides a compelling demonstration of how a web vulnerability scanner operates. By accepting a target URL, it simulates the process of scanning and presents a report of potential security weaknesses in a clear and understandable format. **Please note that this is a simulated scanner and does not perform actual in-depth security analysis.** It serves as an educational tool and a visual representation of vulnerability scanning concepts.

## ✨ Key Features

* **Intuitive User Interface:** A clean and modern web interface allows users to easily input target URLs.
* **Simulated Scanning Process:** A visual loading animation provides feedback, mimicking the time a real scan might take.
* **Detailed Mock Vulnerability Reports:** Presents simulated findings with clear names, severity levels, descriptions, and suggested remediation steps.
* **Visually Engaging Presentation:** Utilizes modern CSS styling to create an appealing and informative user experience.
* **Client-Side Interaction:** Dynamic updates to the page using JavaScript to display scan results without full page reloads.
* **Backend Powered by Flask:** A lightweight Python framework handles the "scanning" logic and serves the vulnerability data.
* **Security Headers:** Demonstrates basic security best practices by including security-related HTTP headers in the server responses.

## 🚀 Getting Started

Follow these simple steps to run CyberGuardian AI locally:

### Prerequisites

* **Python 3.6+:** Ensure you have Python installed on your system. You can download it from [https://www.python.org/downloads/](https://www.python.org/downloads/)
* **pip:** Python package installer (usually included with Python installations).

### Installation

1.  **Clone the repository** (if you have the files in a repository):
    ```bash
    git clone <repository-url>
    cd cyberguardian-ai
    ```

2.  **Navigate to the project directory** (if you've downloaded the files directly):
    ```bash
    cd <directory-containing-files>
    ```

3.  **Install Flask and Flask-CORS:**
    ```bash
    pip install Flask Flask-CORS
    ```

### Running the Application

1.  **Run the Flask development server:**
    ```bash
    python app.py
    ```

2.  **Open your web browser** and navigate to `http://127.0.0.1:5000/`.

3.  **Enter a URL** in the provided input field and click the "Scan" button to see the simulated results.

## 🛠️ How It Works (Simplified)

1.  **User Input:** The user enters a website URL into the form on the `index.html` page.
2.  **Frontend Request:** `script.js` sends an asynchronous request (AJAX) to the `/scan` endpoint on the backend (`app.py`) with the provided URL.
3.  **Simulated Backend Processing:** The Flask application receives the URL, simulates a scanning delay using `time.sleep(2)`, and then returns a predefined list of mock vulnerabilities as a JSON response.
4.  **Frontend Rendering:** `script.js` receives the JSON response and dynamically updates the `index.html` page to display the vulnerability information in a user-friendly table.
5.  **Styling:** `styles.css` provides the visual styling for all elements, ensuring a clean and professional presentation.

## 📂 File Structure
**Thank you for exploring CyberGuardian AI!**
