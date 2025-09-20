# Azure CI/CD Pipeline for a Python Weather App

This project is a complete, end-to-end CI/CD pipeline built with Azure DevOps. It automatically builds and deploys a Python Flask web application that fetches live weather data from the OpenWeatherMap API.

## Key Features
- **Automated CI Pipeline:** Builds and packages the application using YAML.
- **Automated CD Pipeline:** Deploys the application to Azure App Service.
- **Secure Key Management:** API keys are managed securely using Azure's configuration settings.

## Technologies Used
- **Cloud:** Microsoft Azure (App Service)
- **CI/CD:** Azure DevOps (Pipelines, Repos)
- **Language & Framework:** Python, Flask
- **Tools:** Git, REST APIs, YAML

## How to Run Locally
1. Clone the repository.
2. Create a virtual environment: `python -m venv env`
3. Activate it: `.\env\Scripts\activate`
4. Install dependencies: `pip install -r requirements.txt`
5. Create a `.env` file and add your `WEATHER_API_KEY`.
6. Run the app: `flask --app pyapp run`
