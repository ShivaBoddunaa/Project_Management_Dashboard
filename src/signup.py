from fastapi import APIRouter, Request, Form
from src.utils import db, save_user, hash_password, get_user_hash
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse, JSONResponse
 
templates = Jinja2Templates(directory='templates')
router = APIRouter()
 
 
@router.get('/signup')
def get_sign_up(request: Request):
  return templates.TemplateResponse('signup.html', {'request': request})
 
 
@router.post('/signup')
def post_sign_up(request: Request, email: str = Form(...), password: str = Form(...), confirm_password: str = Form(...)):
  if password != confirm_password:
    return JSONResponse({'status': 'error', 'message': 'Passwords do not match'}, status_code=400)
 
  if len(password) < 8:
    return JSONResponse({'status': 'error', 'message': 'Password too short'}, status_code=400)
 
  # Save locally (simple store). If you prefer Supabase auth, integrate here.
  save_user(email, password)
 
  return RedirectResponse('/login', status_code=302)
 
 