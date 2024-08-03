# ClimaticPulse

**ClimaticPulse** is a weather application built using Python that provides users with current weather information based on their city input. The application features a user-friendly graphical interface built with `tkinter`, and it fetches weather data from the OpenWeatherMap API.

## Features

- **City Input:** Enter a city name to get the current weather details.
- **Weather Information:** Displays temperature, weather description, humidity, and wind speed.
- **User Interface:** A clean and modern interface designed using `tkinter`.

## Prerequisites

- **Python 3.11.9**: Ensure you have Python 3 installed on your machine.
- **Requests Library**: Used for making API requests.

## Installation

1. **Clone the Repository:**
   git clone https://github.com/JaaniCoder/ClimaticPulse.git
   cd ClimaticPulse

2. **Install Dependencies:**
   - Install the `requests` library using pip:
     pip install requests

3. **Obtain an API Key:**
   - Sign up at [OpenWeatherMap](https://home.openweathermap.org/users/sign_up) to get your API key.
   - Replace `YOUR_API_KEY_HERE` in the code with your actual API key.

## Usage

1. **Run the Application:**
   - Navigate to the project directory and run the Python script:
     python weather.py

2. **Interacting with the Application:**
   - Enter the name of a city in the input field and click the "Get Weather Details" button.
   - The application will display the current weather information for the specified city.

## Code Overview

- **weather.py**: The main script containing the application logic and GUI implementation.
  - **fetch_weather(city)**: Fetches weather data from OpenWeatherMap API.
  - **display_weather()**: Updates the GUI with the weather information.


## Contribution

Contributions are welcome! If you have suggestions for improvements or find any issues, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For any questions or feedback, please reach out to *theshayarguyjaani@gmail.com* or open an issue on the GitHub repository.

---

Thank you for checking out ClimaticPulse!
