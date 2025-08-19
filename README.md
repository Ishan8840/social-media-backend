# SocialSphere API

A backend social media platform built with **Flask**, featuring JWT authentication, a PostgreSQL database with SQLAlchemy ORM, and containerized deployment using Docker.

---

## ✨ Features
- User registration & login with **JWT authentication**
- Secure password hashing
- CRUD operations for posts (create, read, update, delete)
- Likes & comments system
- User follow/unfollow functionality
- PostgreSQL database integration with **SQLAlchemy**
- Containerized setup with **Docker & Docker Compose**
- RESTful API with **Flask-RESTful**

---

## 🛠️ Tech Stack
- **Backend:** Flask, Flask-JWT-Extended, Flask-RESTful  
- **Database:** PostgreSQL + SQLAlchemy ORM  
- **Authentication:** JWT (JSON Web Tokens)  
- **Containerization:** Docker, Docker Compose  
- **Migrations:** Flask-Migrate (Alembic)  
- **Testing:** Pytest / Unittest  

---

## 📐 Architecture
```mermaid
graph TD
  Client -->|HTTP Requests| Flask_API
  Flask_API -->|SQLAlchemy ORM| PostgreSQL[(Postgres DB)]
  Flask_API --> JWT[JWT Authentication]
  Docker --> Flask_API
  Docker --> PostgreSQL
