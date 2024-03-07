## Flask Application Design for UI Mockup Website

### HTML Files

- **index.html**: Main page of the website, which presents a user interface for building and previewing mockups.
- **elements.html**: Contains a library of reusable UI elements, such as buttons, text fields, and images.
- **preview.html**: Displays a preview of the assembled mockup, allowing users to view their design in real-time.

### Routes

- **index**: Handles requests for the main page.
- **elements**: Renders the library of UI elements as a JSON response, providing access to their attributes and properties.
- **preview**: Assembles the selected UI elements based on their attributes and renders the assembled mockup in the browser.
- **save**: Receives the assembled mockup and stores it for future retrieval or sharing.
- **load**: Retrieves a previously saved mockup based on its unique ID and returns it as a JSON response.
- **delete**: Deletes a saved mockup based on its unique ID.