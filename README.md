# Azure CI/CD Pipeline for a Python Weather App

This project demonstrates a complete, end-to-end CI/CD pipeline built with Azure DevOps. It automatically builds and deploys a Python Flask web application that fetches live weather data from the OpenWeatherMap API.

**Live Demo:** [https://thowfiq-app-2025-buhtduanhje5gndy.centralindia-01.azurewebsites.net/](https://thowfiq-app-2025-buhtduanhje5gndy.centralindia-01.azurewebsites.net/) 

---
## Project Architecture
This project uses a "pipeline-as-code" approach with a multi-stage YAML file to define both the build (CI) and deployment (CD) processes. A `git push` to the main branch automatically triggers the entire workflow, deploying the application to Azure App Service.



---
## Key Features
- **Automated CI/CD:** A multi-stage YAML pipeline in Azure DevOps automates the entire process from code commit to live deployment.
- **Self-Contained Deployments:** Python dependencies are packaged with the application during the build phase, ensuring a reliable and consistent deployment environment.
- **Secure Key Management:** The sensitive OpenWeatherMap API key is securely stored in Azure App Service's configuration and is not exposed in the source code.

## Technologies Used
- **Cloud Platform:** Microsoft Azure (App Service)
- **CI/CD:** Azure DevOps (Multi-stage YAML Pipelines)
- **Languages:** Python, YAML, Bash
- **Frameworks:** Flask
- **Tools & Version Control:** Git, REST APIs

## Setup and Local Run Instructions
1. Clone the repository.
2. Create a virtual environment: `python -m venv env`
3. Activate it: `.\env\Scripts\activate` (on Windows) or `source env/bin/activate` (on Mac/Linux).
4. Install dependencies: `pip install -r requirements.txt`
5. Create a `.env` file and add your `WEATHER_API_KEY`.
6. Run the app: `flask --app pyapp run`
