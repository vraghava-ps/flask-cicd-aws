🚀 CI/CD Pipeline — Flask App with GitHub Actions, Docker & AWS

📌 Project Overview

This project demonstrates a complete end-to-end CI/CD pipeline that automates building, testing, and deploying a Python Flask application using modern DevOps tools.

👉 On every GitHub push:

Code is tested using pytest
Docker image is built
Image is pushed to AWS ECR
Application is deployed automatically to AWS EC2

🧱 Architecture
GitHub → GitHub Actions → Docker → AWS ECR → AWS EC2 → Flask App

🛠️ Tech Stack
Component            Technology Used
Source Code	         GitHub
CI/CD Pipeline	     GitHub Actions
Containerization	   Docker
Container Registry	 AWS ECR
Deployment	         AWS EC2 (Ubuntu)
Application	         Python Flask
Testing	             Pytest

📂 Project Structure
flask-cicd-aws/
├── app.py
├── requirements.txt
├── Dockerfile
├── tests/
│   └── test_app.py
└── .github/
    └── workflows/
        └── deploy.yml

⚙️ How It Works
🔹 1. Code Push
Developer pushes code to GitHub

🔹 2. CI Stage
Install dependencies
Run unit tests using pytest

🔹 3. Build Stage
Build Docker image
Tag image with commit SHA
Push image to AWS ECR

🔹 4. Deployment Stage
SSH into EC2
Pull latest Docker image
Stop old container
Run new container

🚀 Setup Instructions
1️⃣ Clone Repository
git clone https://github.com/YOUR_USERNAME/flask-cicd-aws.git
cd flask-cicd-aws

2️⃣ Configure AWS
Create ECR repository
Launch EC2 instance
Install Docker on EC2

3️⃣ Add GitHub Secrets
Go to Settings → Secrets → Actions and add:
Secret Name	Description
AWS_ACCESS_KEY_ID	AWS Access Key
AWS_SECRET_ACCESS_KEY	AWS Secret Key
AWS_REGION	ap-south-1
ECR_REPOSITORY	Your ECR repo name
EC2_HOST	EC2 public IP
EC2_USERNAME	ubuntu
EC2_SSH_KEY	.pem file content

4️⃣ Run the Pipeline
git add .
git commit -m "Initial CI/CD setup"
git push origin main

👉 Go to GitHub Actions tab to see pipeline execution
🌐 Access Application
After successful deployment:
http://<EC2_PUBLIC_IP>:5000

🧪 API Endpoints
Endpoint	Description
/	Returns app info
/health	Health check

📸 Sample Output
{
  "message": "Hello from DevOps Project!",
  "version": "1.0.0",
  "status": "running"
}

💡 Key Features
✅ Fully automated CI/CD pipeline
✅ Docker-based deployment
✅ AWS ECR integration
✅ Zero-downtime deployment (container replacement)
✅ Automated testing before deployment

👨‍💻 Author
Venkat Raghava P S
DevOps Enthusiast 🚀
