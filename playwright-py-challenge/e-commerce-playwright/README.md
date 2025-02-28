# Playwright Challenge with Python

## Description
This project is an example of an e-commerce application for practicing test automation using Playwright, Pytest-BDD, and Python.

## Steps to Run the Project

1. Clone the repository:
   ```bash
   git clone [your-repository-url]
   cd playwright-challenge
   ```

2. Create and activate a virtual environment (recommended):
   ```bash
   python -m venv venv
   # On Windows
   venv\Scripts\activate
   # On macOS/Linux
   source venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Install Playwright browsers:
   ```bash
   playwright install
   ```

5. Start the web application (keep the React app as is):
   ```bash
   cd src
   npm install
   npm start
   ```

6. Run the tests:
   ```bash
   pytest
   ```

7. To run tests with HTML report:
   ```bash
   pytest --html=report.html
   ```

## Application Features

1. **Home Page**:
   - Product list with name and price.
   - Links to product detail pages.

2. **Product Page**:
   - Details of a specific product.
   - Button to add the product to the cart.

3. **Cart Page**:
   - List of products added to the cart.
   - Link to proceed to checkout.

4. **Checkout Page**:
   - Form to complete the purchase.

5. **Profile Page**:
   - Displays user information: name and email.

## Project Structure

- `src/`: Application source code (React app kept as is).
- `tests/`: Playwright test cases and configurations.
  - `features/`: BDD feature files
  - `pages/`: Page Object Models
  - `step_definitions/`: Step definition files
  - `utils/`: Utility files and constants

## Key Differences from Cypress Version

- Uses Playwright instead of Cypress for browser automation
- Uses pytest and pytest-bdd instead of Cucumber.js
- Implements Page Object Model pattern in Python
- Leverages Python's testing ecosystem for reporting and fixtures

Good luck!