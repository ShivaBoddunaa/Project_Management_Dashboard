from fastapi import APIRouter,Request,Form
from src.utils import db
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse, JSONResponse
 
templates=Jinja2Templates(directory='templates')
router = APIRouter()
 
# @router.get('/')
# def home_sign_up():
#     return RedirectResponse('/home.html')
 
@router.get('/projects')
def get_projects(request: Request):
 res = db.table('projects').select('*').execute()
 data=res.data
 return templates.TemplateResponse('home.html',{'request': request, 'project':data})
 
@router.get('/projects/create')
def show_create_project_form(request: Request):
    return templates.TemplateResponse('create_project.html',{'request': request})
 
@router.post('/projects/create')
def create_project_form(request: Request, project_id = Form(...),project_name = Form(...),description = Form(...),budget =Form (...),duration = Form(...)):
    data ={
        'id':project_id,
        'name':project_name,
        'description':description,
        'budget':budget,
        'duration':duration
    }
    res=db.table('projects').insert(data).execute()
    return RedirectResponse('/projects',status_code=302)
 
@router.get('/projects/update')
def update_project_form(request: Request):
    return templates.TemplateResponse('update_project.html',{'request': request})
 
@router.post('/projects/update')
def update_project(request: Request, project_id: str = Form(...), project_name: str = Form(...), description: str = Form(...), budget: str = Form(...), duration: str = Form(...)):
    data = {
        'name': project_name,
        'description': description,
        'budget': budget,
        'duration': duration
    }
    db.table('projects').update(data).eq('id', project_id).execute()
    return RedirectResponse('/projects', status_code=302)
 
@router.get('/projects/edit/{project_id}')
def edit_project_form(request: Request, project_id: str):
    res = db.table('projects').select('*').eq('id', project_id).execute()
    data = None
    if res.data and len(res.data) > 0:
        data = res.data[0]
    return templates.TemplateResponse('update_project.html', {'request': request, 'project': data})
 
@router.delete('/projects/delete/{project_id}')
def delete_project(project_id: str):
    res = db.table('projects').delete().eq('id', project_id).execute()
    return {'status': 'success', 'message': 'project deleted successfully', 'result': res.data}
 