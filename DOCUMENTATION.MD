# NimbusDocs Documentation

## Overview

**NimbusDocs** is a document management system that integrates with real-time notifications. This documentation provides details on the application's design, API endpoints, and the setup of development and production environments.

## Backend: Django

### **Directory Structure**

- **`django_backend/`**
  - **`document_management/`**: Core Django project files.
  - **`documents/`**: Django app for managing documents.
  - **`manage.py`**: Django management command utility.
  - **`requirements.txt`**: Python dependencies.
  - **`Dockerfile`**: Docker configuration for the Django app.

### **API Endpoints**

- **`/api/documents/`**
  - **GET**: Retrieve a list of documents.
  - **POST**: Create a new document.

- **`/api/documents/{id}/`**
  - **GET**: Retrieve a specific document.
  - **PUT**: Update a specific document.
  - **DELETE**: Delete a specific document.

### **Admin Panel**

Access the Django admin panel at `/admin/` to manage documents and users.

## Notifications: Node.js

### **Directory Structure**

- **`node_notifications/`**
  - **`src/`**: Contains source code for the Node.js notifications service.
  - **`package.json`**: Node.js dependencies and scripts.
  - **`Dockerfile`**: Docker configuration for the Node.js app.

### **Endpoints**

- **`/notifications`**
  - **POST**: Endpoint to send real-time notifications to clients.

### **WebSocket**

The Node.js service uses WebSocket for real-time communication.

## CI/CD Integration

The CI/CD pipeline is defined in `.github/workflows/ci-cd.yml` and includes:

- **Build**: Docker images for Django and Node.js.
- **Test**: Run tests for both Django and Node.js applications.
- **Deploy**: Deploy updated Docker images to the server.

## Dockerization

### **Dockerfiles**

- **Django Dockerfile (`django_backend/Dockerfile`)**: Configures the Django application container.
- **Node.js Dockerfile (`node_notifications/Dockerfile`)**: Configures the Node.js application container.

### **Docker Compose**

**`docker-compose.yml`** orchestrates the multi-container setup, including services for Django, Node.js, and PostgreSQL.

## Development Workflow

1. **Build and Start Containers**
   ```bash
   docker-compose up --build
   ```

2. **Run Database Migrations (Django)**
   ```bash
   docker-compose exec django python manage.py migrate
   ```

3. **Create Superuser (Django)**
   ```bash
   docker-compose exec django python manage.py createsuperuser
   ```

## Contributing

Refer to the `README.md` for contributing guidelines.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Contact

For more information, refer to the `README.md` for contact details.
---
