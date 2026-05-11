const WORKSPACE_API_BASE = '/api/v1/workspace';

export const getWorkspaceFiles = async () => {
	const response = await fetch(`${WORKSPACE_API_BASE}/files`);
	return response.json();
};

export const getWorkspaceIndex = async () => {
	const response = await fetch(`${WORKSPACE_API_BASE}/index`);
	return response.json();
};

export const runWorkspaceCommand = async (command: string) => {
	const response = await fetch(`${WORKSPACE_API_BASE}/terminal/run`, {
		method: 'POST',
		headers: {
			'Content-Type': 'application/json'
		},
		body: JSON.stringify({ command })
	});

	return response.json();
};

export const getWorkspaceTasks = async () => {
	const response = await fetch(`${WORKSPACE_API_BASE}/tasks`);
	return response.json();
};
