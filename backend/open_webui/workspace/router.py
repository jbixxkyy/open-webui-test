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


@router.get('/files')
def list_files():
    return filesystem.list_files()


@router.get('/index')
def index_workspace():
    return indexer.scan_workspace()


@router.post('/terminal/run')
def run_command(payload: CommandPayload):
    return terminal.run_command(payload.command)


@router.get('/tasks')
def get_tasks():
    return agent_manager.get_tasks()
