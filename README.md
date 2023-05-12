# Flask App

This is a simple Flask app that serves static files and includes a route for JSON responses. It is designed to demonstrate basic functionality and serve as a starting point for further development.

## Features

- Serves static files from the `/static` directory.
- Includes a route to serve a static JSON file.
- Demonstrates a route that returns a JSON response.

## Requirements

- Python 3.x
- Flask

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/lmxx1234567/chatgpt-plugin-starter-python.git
   ```

2. Navigate to the project directory:

   ```bash
   cd chatgpt-plugin-starter-python
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Start the Plugin server:

   ```bash
   python main.py
   ```

2. Access the following routes in your browser or through API requests:

   - `/.well-known/ai-plugin.json` - Displays the content of the `ai-plugin.json` file located in the `static` directory.
   - `/static/*` - Matches any file name and displays its content from the `static` directory.
   - `/decorate` - Returns a JSON response with the message "Hello World!".

## Customization

- To modify the content of the `ai-plugin.json` file, update the file located in the `static` directory.
- Add your own static files to the `static` directory and access them through the `/static/*` route.
- Expand the functionality by adding more routes or modifying the existing ones in the `main.py` file.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please create a new issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).