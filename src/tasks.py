 
from fastapi import APIRouter, Request, Form
from src.utils import db
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse, JSONResponse
 
templates = Jinja2Templates(directory='templates')
router = APIRouter()
 
 
@router.get('/projects/{project_id}/tasks')
def get_project_tasks(request: Request, project_id: str):
    res = db.table('tasks').select('*').eq('project_id', project_id).execute()
    data = res.data
    return templates.TemplateResponse('projects_tasks.html', {'request': request, 'tasks': data, 'project_id': project_id})
 
@router.get('/tasks')
def get_tasks(request: Request):
 res = db.table('tasks').select('*').execute()
 data=res.data
 return templates.TemplateResponse('tasks_home.html',{'request': request})
 
 
@router.get('/tasks/create')
def show_create_task_form(request: Request):
    project_id = request.query_params.get('project_id', '')
    return templates.TemplateResponse('create_task.html', {'request': request, 'project_id': project_id})
 
@router.post('/tasks/create')
def create_task_form(request: Request, task_id = Form(...),title = Form(...),description = Form(...),status =Form (...),project_id = Form(...)):
    data ={
        'id':task_id,
        'title':title,
        'description':description,
        'status':status,
        'project_id':project_id,
    }
    res=db.table('tasks').insert(data).execute()
    return RedirectResponse('/tasks',status_code=302)
 
 
@router.post('/tasks/update')
def update_task(request: Request, task_id: str = Form(...), title: str = Form(...), description: str = Form(...), status: str = Form(...), project_id: str = Form(...)):
    data = {
        'title': title,
        'description': description,
        'status': status,
        'project_id': project_id,
    }
    db.table('tasks').update(data).eq('id', task_id).execute()
    return RedirectResponse(f'/projects/{project_id}/tasks', status_code=302)
 
@router.get('/taskss/update')
def update_task_form(request: Request):
    return templates.TemplateResponse('update_task.html',{'request': request})
 
@router.get('/tasks/edit/{task_id}')
def edit_task_form(request: Request, task_id: str):
    res = db.table('tasks').select('*').eq('id', task_id).execute()
    data = None
    if res.data and len(res.data) > 0:
        data = res.data[0]
    return templates.TemplateResponse('update_task.html', {'request': request, 'task': data})
 
 
@router.delete('/tasks/delete/{task_id}')
def delete_task(task_id: str):
    res = db.table('tasks').delete().eq('id', task_id).execute()
    return {'status': 'success', 'message': 'task deleted successfully', 'result': res.data}
 