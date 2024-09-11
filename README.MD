# NimbusDocs

**NimbusDocs** is a comprehensive document management system with real-time notifications. It is designed to handle document storage, retrieval, and notifications efficiently. The project utilizes Django for the backend and Node.js for real-time notifications.

## Project Structure

```
NimbusDocs/
├── django_backend/
│   ├── document_management/
│   ├── documents/
│   ├── manage.py
│   ├── requirements.txt
│   ├── Dockerfile
│   ├── static/
│   ├── media/
│   └── db.sqlite3 (or PostgreSQL config)
│
├── node_notifications/
│   ├── src/
│   ├── public/
│   ├── package.json
│   ├── .env
│   ├── Dockerfile
│   └── node_modules/
│
├── docker-compose.yml
├── .github/
│   └── workflows/
│       └── ci-cd.yml
└── README.md
```

## Installation

### Prerequisites

- **Docker**: [Install Docker](https://docs.docker.com/get-docker/)
- **Docker Compose**: [Install Docker Compose](https://docs.docker.com/compose/install/)
- **Git**: [Install Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)

### Clone the Repository

```bash
git clone https://github.com/yourusername/nimbusdocs.git
cd nimbusdocs
```

### Setting Up the Project

1. **Build and Start Containers**

   Use Docker Compose to build and start all services:

   ```bash
   docker-compose up --build
   ```

2. **Migrate Database (Django)**

   After starting the containers, run database migrations:

   ```bash
   docker-compose exec django python manage.py migrate
   ```

3. **Create Superuser (Django)**

   Create a Django superuser to access the admin panel:

   ```bash
   docker-compose exec django python manage.py createsuperuser
   ```

4. **Access the Application**

   - **Django Backend**: http://localhost:8000
   - **Node.js Notifications**: http://localhost:5000

## CI/CD

The project uses GitHub Actions for CI/CD. The workflow automates:

- Building Docker images
- Running tests for Django and Node.js
- Deploying to the server

For details on the CI/CD process, see `.github/workflows/ci-cd.yml`.

## Dockerization

The project uses Docker to containerize the Django and Node.js applications. Dockerfiles are included for both services.

### **Django Dockerfile (`django_backend/Dockerfile`):**

```dockerfile
# Use an official Python runtime as a parent image
FROM python:3.8

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY django_backend/ /app/

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Run Django server when the container launches
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
```

### **Node.js Dockerfile (`node_notifications/Dockerfile`):**

```dockerfile
# Use an official Node.js runtime as a parent image
FROM node:14

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy package.json and package-lock.json
COPY node_notifications/package*.json ./

# Install any needed packages specified in package.json
RUN npm install

# Copy the rest of the application code
COPY node_notifications/ .

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Run the Node.js server when the container launches
CMD ["node", "src/app.js"]
```

### **Docker Compose File (`docker-compose.yml`):**

```yaml
version: '3'

services:
  django:
    build:
      context: ./django_backend
    ports:
      - "8000:8000"
    volumes:
      - ./django_backend:/app
    depends_on:
      - db

  node:
    build:
      context: ./node_notifications
    ports:
      - "5000:5000"
    volumes:
      - ./node_notifications:/usr/src/app

  db:
    image: postgres:latest
    environment:
      POSTGRES_DB: mydatabase
      POSTGRES_USER: myuser
      POSTGRES_PASSWORD: mypassword
    ports:
      - "5432:5432"
```

## Contributing

1. **Fork the Repository**
2. **Create a Feature Branch**
   ```bash
   git checkout -b feature/new-feature
   ```
3. **Commit Changes**
   ```bash
   git commit -am 'Add new feature'
   ```
4. **Push to the Branch**
   ```bash
   git push origin feature/new-feature
   ```
5. **Create a Pull Request**

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

For questions or feedback, please reach out to:

- **Email**: your.email@example.com
- **GitHub**: [Your GitHub Profile](https://github.com/yourusername)
```

-