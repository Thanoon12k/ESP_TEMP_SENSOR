# Temperature Display Dashboard

## Overview
This project is a web-based temperature display dashboard that shows the current temperature and plots temperature data over different time frames. It uses Tailwind CSS for styling and Chart.js for rendering the temperature plot.

## Features
- Displays the current temperature in a large, round format.
- Provides buttons to switch between daily, weekly, and monthly temperature views.
- Plots temperature data on a responsive chart that adjusts based on the selected time frame.

## Installation
To run this project locally, follow these steps:
1. Clone the repository to your local machine.
2. Open the `index.html` file in a web browser to view the dashboard.

## Usage
- The dashboard will display the current temperature upon loading.
- Use the "Increase", "Decrease", and "Reset" buttons to interact with the temperature display (Note: These buttons are for demonstration and do not change the temperature data).
- Click on the "Day", "Week", or "Month" buttons to view the temperature plot for the respective time frame.

## Technologies Used
- **HTML**: For structuring the web page.
- **Tailwind CSS**: For styling the components.
- **Chart.js**: For creating interactive temperature plots.
- **JavaScript**: For handling user interactions and updating the chart.
- **Flask**: For handling back-end Section for our Site.

## Project Structure
- `main.html`: The main HTML file that contains the structure of the dashboard.
- `flaskr.py`: The python file that contains the setup for flask app with one route "/".
- `data.py`: The python file that on future fetch data from google drive then inject it into flask app.

## Contributing
Contributions to this project are welcome. Please follow these steps to contribute:
1. Fork the repository.
2. Create a new branch for your feature.
3. Commit your changes.
4. Push to the branch.
5. Create a new Pull Request.

## License
This project is open source and available under the MIT License.

## Contact
For any queries or suggestions, please open an issue on the GitHub repository.

## Acknowledgments
- Thanks to Tailwind CSS for the utility-first CSS framework.
- Thanks to Chart.js for the simple yet flexible JavaScript charting.
- Thanks to Flask for the simple responsive app setup.

