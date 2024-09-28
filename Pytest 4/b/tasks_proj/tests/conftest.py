import pytest
import tasks
from tasks import Task


@pytest.fixture(scope='session')
def tasks_db_session(tmpdir_factory):
    temp_dir = tmpdir_factory.mktemp('temp')
    tasks.start_tasks_db(str(temp_dir), 'tiny')
    
    yield 
    
    tasks.stop_tasks_db()
    

@pytest.fixture()
def tasks_db(tasks_db_session):
    tasks.delete_all()
    
 
   
@pytest.fixture(scope='session')
def tasks_just_a_few():
    return (
        Task('Write some code', 'Will', True),
        Task("Codi reviews Will code", "Codi", False),
        Task("Fix Will code", "Jess", False))
    
    
    
@pytest.fixture(scope='session')
def tasks_multi_per_owner():
    return(
        Task("Make breakfast", 'Adam'),
        Task("Clean", "Adam"),
        Task("Cook", "Adam"),
        
        Task("Create", 'Pamela'),
        Task("Edit", "Pamela"),
        Task("Copy", "Pamela"), 
        
        Task("Bake", 'Guillermo'),
        Task("Broil", "Guillermo"),
        Task("Fry", "Guillermo"))
    
    
    
@pytest.fixture()
def db_with_3_tasks(tasks_db, tasks_just_a_few):
    for t in tasks_just_a_few:
        tasks.add(t)
        

@pytest.fixture()
def db_with_multi_per_owner(tasks_db, tasks_multi_per_owner):
    for t in tasks_multi_per_owner:
        tasks.add(t)    
    
    
    
    
    
    
