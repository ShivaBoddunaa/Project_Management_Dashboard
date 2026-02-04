 
📌 Simple Project Management App — FastAPI + Supabase
 
A clean and lightweight Project & Task Management System built using FastAPI, Jinja2 templates, and Supabase PostgreSQL.
Users can create, update, delete, and manage Projects and Tasks with a modern UI.
 
🚀 Features
✅ Project Management
 
(Backend router reference:
 
projects
 
)
 
Create new projects
 
View all projects
 
Edit project details
 
Update budget & duration
 
Delete projects with confirmation
 
Open project to view its tasks
 
📝 Task Management
 
(Backend router reference:
 
tasks
 
)
 
Create tasks and assign them to a project
 
View tasks grouped by project
 
Update task details
 
Delete tasks
 
Supports task status (pending, in progress, completed)
 
🎨 Frontend Templates (Jinja2)
 
Your UI is built using HTML templates with styling.
Each template is responsible for a specific page in the system:
 
Template    Description
home.html →
 
home
 
    Project listing screen
create_project.html →
 
create_project
 
    Form to create a new project
update_project.html →
 
update_project
 
    Edit project details
delete_project.html →
 
delete_project
 
    Delete confirmation page
project_tasks.html →
 
project_tasks
 
    Displays all tasks under a project
create_task.html →
 
create_task
 
    Form to create new task
update_task.html →
 
update_task
 
    Edit task page
🛢 Database — Supabase
 
Your Supabase database connection is initialized in utils.py:
 
(Reference:
 
utils
 
)
 
Fields required:
 
Projects table
 
id
 
name
 
description
 
budget
 
duration (days)
 
Tasks table
 
id
 
title
 
description
 
status
 
project_id (Foreign key)
 
🧩 Backend Structure
 
Your main API application is defined in main.py:
 
(Reference:
 
main
 
)
 
from fastapi import FastAPI
from src.tasks import router as task_router
from src.projects import router as project_router
 
app = FastAPI()
app.include_router(project_router)
app.include_router(task_router)
 
 
This registers the Projects Router and Tasks Router to expose all endpoints.
 
📁 Project Structure
.
├── main.py                          # FastAPI entry point
├── src/
│   ├── projects.py                  # Project CRUD logic
│   ├── tasks.py                     # Task CRUD logic
│   └── utils.py                     # Supabase client
├── templates/
│   ├── home.html
│   ├── create_project.html
│   ├── update_project.html
│   ├── delete_project.html
│   ├── project_tasks.html
│   ├── create_task.html
│   └── update_task.html
├── requirements.txt                 # Python dependencies
├── vercel.json                      # Deployment config
└── .gitignore                       # Ignored files (e.g., __pycache__)
 
📦 Requirements
 
Your app depends on the libraries listed in requirements.txt:
 
(Reference:
 
requirements
 
)
 
Includes major packages like:
 
FastAPI
 
Jinja2
 
Supabase
 
Uvicorn
 
Python Multipart
 
Starlette
 
Pydantic
 
Install all dependencies:
 
pip install -r requirements.txt
 
▶️ Running the Project Locally
1️⃣ Install dependencies
pip install -r requirements.txt
 
2️⃣ Start the server
uvicorn main:app --reload
 
3️⃣ Open in browser
http://localhost:8000/projects
 
🌍 Deploying on Vercel
 
Your deployment configuration is defined in vercel.json:
 
(Reference:
 
vercel
 
)
 
{
  "builds": [
    { "src": "main.py", "use": "@vercel/python" }
  ],
  "routes": [
    { "src": "/(.*)", "dest": "main.py" }
  ]
}
 
Steps:
 
Push project to GitHub
 
Import into Vercel
 
Deploy
 
Vercel detects main.py and handles FastAPI
 
🧹 .gitignore
 
Your .gitignore file ensures unnecessary files (e.g., cache) are not pushed:
 
(Reference:
 
.gitignore
 
)
 
__pycache__/
 
✔️ Summary
 
This repository provides:
 
Full CRUD for Projects & Tasks
 
Clean UI built with Jinja2 templates
 
FastAPI backend with Supabase database
 
Vercel-ready deployment configuration
 
Modular and easy-to-understand structure
 