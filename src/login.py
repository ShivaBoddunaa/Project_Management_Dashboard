from fastapi import APIRouter, Request, Form
from src.utils import db, get_user_hash, hash_password
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse, JSONResponse
 
templates = Jinja2Templates(directory='templates')
router = APIRouter()
 
 
@router.get('/login')
def get_log_in(request: Request):
    return templates.TemplateResponse('login.html', {'request': request})
 
 
@router.post('/login')
def post_log_in(request: Request, email: str = Form(...), password: str = Form(...)):
    stored_hash = get_user_hash(email)
    if not stored_hash:
        return JSONResponse({'status': 'error', 'message': 'Invalid credentials'}, status_code=401)
 
    if hash_password(password) != stored_hash:
        return JSONResponse({'status': 'error', 'message': 'Invalid credentials'}, status_code=401)
 
    # successful login — redirect to projects page
    return RedirectResponse('/projects', status_code=302)
 
 
 