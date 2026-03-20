# 📚 Library Registration System

A modern Library Registration Web Application built using Django, AWS DynamoDB, Docker, and Jenkins for CI/CD automation.

---

## 🚀 Features

* Student registration form
* Modern UI with animations
* Data stored in AWS DynamoDB
* Success page after submission
* Dockerized application
* Automated build and deployment using Jenkins

---

## 📁 Project Structure

The project contains a Django application with a registration module, templates for UI, and configuration files for Docker and Jenkins. It is organized to follow a clean and scalable structure suitable for real-world projects.

---

## ⚙️ Setup Overview

To run this project, you need to:

* Clone the repository from GitHub
* Configure environment variables for AWS
* Run the application using Docker
* Access the app in your browser

---

## ☁️ AWS DynamoDB Setup

Create a DynamoDB table in AWS with the following configuration:

* Table name: LibraryUsers
* Primary key: id (String)

Ensure your AWS credentials are properly configured in environment variables.

---

## ⚙️ Jenkins CI/CD Integration

This project uses Jenkins for continuous integration and deployment.

### Workflow:

* Developer pushes code to GitHub
* Jenkins detects changes automatically
* Jenkins builds the Docker image
* Jenkins deploys the container
* Application becomes live

---

## 🔄 CI/CD Flow

Developer → GitHub → Jenkins → Docker Build → Deployment → Live Application

---

## 🧪 Local Development

You can also run the project locally by installing dependencies and starting the Django development server.

---

## 🔐 Security Notes

* Do not expose AWS credentials publicly
* Use environment variables for sensitive data
* Prefer IAM roles for production deployments

---

## 🚀 Future Enhancements

* User authentication system
* Admin dashboard to view registered users
* Data export functionality (CSV/Excel)
* React frontend integration
* Deployment on AWS EC2 with Nginx

---

## 🤝 Contributing

Contributions are welcome. You can fork the repository and submit pull requests.

---

## 📜 License

This project is open-source and available under the MIT License.

---

## 👨‍💻 Author

Nitin Panwar
B.Tech CSE | DevOps Enthusiast 🚀
