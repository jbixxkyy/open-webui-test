const WORKSPACE_API_BASE = '/api/v1/workspace';

export const getWorkspaceFiles = async () => {
	const response = await fetch(`${WORKSPACE_API_BASE}/files`);
	return response.json();
};

export const readWorkspaceFile = async (path: string) => {
	const response = await fetch(`${WORKSPACE_API_BASE}/files/read`, {
		method: 'POST',
		headers: {
			'Content-Type': 'application/json'
		},
		body: JSON.stringify({ path })
	});

	return response.json();
};

export const writeWorkspaceFile = async (path: string, content: string) => {
	const response = await fetch(`${WORKSPACE_API_BASE}/files/write`, {
		method: 'POST',
		headers: {
			'Content-Type': 'application/json'
		},
		body: JSON.stringify({ path, content })
	});

	return response.json();
};

export const createWorkspaceFile = async (path: string) => {
	const response = await fetch(`${WORKSPACE_API_BASE}/files/create`, {
		method: 'POST',
		headers: {
			'Content-Type': 'application/json'
		},
		body: JSON.stringify({ path })
	});

	return response.json();
};

export const createWorkspaceFolder = async (path: string) => {
	const response = await fetch(`${WORKSPACE_API_BASE}/folders/create`, {
		method: 'POST',
		headers: {
			'Content-Type': 'application/json'
		},
		body: JSON.stringify({ path })
	});

	return response.json();
};

export const renameWorkspacePath = async (old_path: string, new_path: string) => {
	const response = await fetch(`${WORKSPACE_API_BASE}/files/rename`, {
		method: 'POST',
		headers: {
			'Content-Type': 'application/json'
		},
		body: JSON.stringify({ old_path, new_path })
	});

	return response.json();
};

export const deleteWorkspaceFile = async (path: string) => {
	const response = await fetch(`${WORKSPACE_API_BASE}/files/delete`, {
		method: 'POST',
		headers: {
			'Content-Type': 'application/json'
		},
		body: JSON.stringify({ path })
	});

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
