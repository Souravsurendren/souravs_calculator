Basic Calculator
                This project is a Basic Calculator built using Flask for the backend, with HTML, CSS, and JavaScript for the frontend. It performs basic arithmetic operations like addition, subtraction, multiplication, and division. The design is modern and responsive, ensuring a smooth user experience.
Project Structure
graphql
Copy code
calculator/
│
├── app.py                # Main Flask application
│
├── static/
│   ├── css/
│   │   └── style.css      # Stylesheet for the calculator UI
│   └── js/
│       └── script.js      # JavaScript for dynamic behavior
│
└── templates/
    └── calculator.html    # HTML template for the calculator interface
Features
Perform basic arithmetic operations: +, -, ×, and ÷.
Modern, clean, and responsive UI.
User-friendly button layout for easy input.
Erase function to delete single digits.
Clear function to reset the entire input.
Technologies Used
Flask: A lightweight Python web framework for managing server-side operations.
HTML/CSS: Provides the structure and design of the calculator UI.
JavaScript: Handles button interactions and arithmetic operations.
File Descriptions
app.py: The main Flask application that serves the calculator UI and handles requests.

static/css/style.css: The stylesheet containing all the CSS for the layout, styling, and color schemes of the calculator.

static/js/script.js: JavaScript file that contains the dynamic functionality for handling button clicks, updating the display, and performing operations like clear and erase.

templates/calculator.html: HTML file that serves as the UI for the calculator, defining the structure and integration of JavaScript and CSS.

