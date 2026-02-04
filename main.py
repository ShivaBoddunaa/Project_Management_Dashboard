from fastapi import FastAPI
from src.tasks import router as task_router
from src.projects import router as project_router
from src.signup import router as signup_router
from src.login import router as login_router
from fastapi.responses import RedirectResponse
 
app=FastAPI()
 
@app.get('/')
def root():
 return RedirectResponse('/signup')
 
app.include_router(project_router)
app.include_router(task_router)
app.include_router(signup_router)
app.include_router(login_router)
 
 