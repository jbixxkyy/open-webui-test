from fastapi import APIRouter
from pydantic import BaseModel

from open_webui.workspace.agent_manager import AgentManager
from open_webui.workspace.context_engine import ContextEngine
from open_webui.workspace.filesystem import WorkspaceFileSystem
from open_webui.workspace.indexer import WorkspaceIndexer
from open_webui.workspace.terminal_runtime import TerminalRuntime


router = APIRouter(prefix='/workspace', tags=['workspace'])

workspace_root = '.'

filesystem = WorkspaceFileSystem(workspace_root)
indexer = WorkspaceIndexer(workspace_root)
terminal = TerminalRuntime(workspace_root)
context_engine = ContextEngine()
agent_manager = AgentManager()


class CommandPayload(BaseModel):
    command: str


class FilePayload(BaseModel):
    path: str
    content: str = ''


class RenamePayload(BaseModel):
    old_path: str
    new_path: str


@router.get('/files')
def list_files():
    return filesystem.list_files()


@router.post('/files/read')
def read_file(payload: FilePayload):
    return {
        'path': payload.path,
        'content': filesystem.read_file(payload.path)
    }


@router.post('/files/write')
def write_file(payload: FilePayload):
    return filesystem.write_file(payload.path, payload.content)


@router.post('/files/create')
def create_file(payload: FilePayload):
    return filesystem.create_file(payload.path)


@router.post('/folders/create')
def create_folder(payload: FilePayload):
    return filesystem.create_folder(payload.path)


@router.post('/files/rename')
def rename_path(payload: RenamePayload):
    return filesystem.rename_path(payload.old_path, payload.new_path)


@router.post('/files/delete')
def delete_file(payload: FilePayload):
    return filesystem.delete_file(payload.path)


@router.get('/index')
def index_workspace():
    return indexer.scan_workspace()


@router.post('/terminal/run')
def run_command(payload: CommandPayload):
    return terminal.run_command(payload.command)


@router.get('/tasks')
def get_tasks():
    return agent_manager.get_tasks()
