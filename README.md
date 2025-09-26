# Azure CI/CD Pipeline for a Python Weather App

This project demonstrates a full CI/CD pipeline using Azure DevOps to automatically deploy a Python Flask web application to Azure App Service.

**Live Demo:** "thowfiq-app-2025-buhtduanhje5gndy.centralindia-01.azurewebsites.net"

---
## Project Architecture
The diagram below shows the workflow. A `git push` to this GitHub repository triggers a build pipeline in Azure DevOps, which then triggers a release pipeline to deploy the application to Azure App Service.


*(You can easily create a simple diagram using a free tool like diagrams.net, save it as a PNG, and add it to your GitHub repository.)*

---
## Key Features
- **Automated CI Pipeline:** The `azure-pipelines.yml` file defines a build that automatically tests and packages the application.
- **Automated CD Pipeline:** A release pipeline in Azure DevOps deploys the application to a staging and production environment.
- **Infrastructure as a Service (IaaS):** The application is hosted on **Azure App Service**, a fully managed platform.
- **Secure Key Management:** The OpenWeatherMap API key is securely stored in Azure App Service's configuration, not in the code.

## Technologies Used
- **Cloud:** Microsoft Azure (App Service)
- **CI/CD:** Azure DevOps (Pipelines, Repos)
- **Language & Framework:** Python, Flask
- **Tools:** Git, REST APIs, YAML
