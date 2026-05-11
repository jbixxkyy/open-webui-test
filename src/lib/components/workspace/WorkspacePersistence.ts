const STORAGE_KEY = 'open-webui-workspace-layout';

export type WorkspaceLayoutState = {
	sidebarOpen: boolean;
	terminalOpen: boolean;
	activePanel: string;
};

export const defaultWorkspaceState: WorkspaceLayoutState = {
	sidebarOpen: true,
	terminalOpen: true,
	activePanel: 'explorer'
};

export const saveWorkspaceState = (state: WorkspaceLayoutState) => {
	localStorage.setItem(STORAGE_KEY, JSON.stringify(state));
};

export const loadWorkspaceState = (): WorkspaceLayoutState => {
	const raw = localStorage.getItem(STORAGE_KEY);

	if (!raw) {
		return defaultWorkspaceState;
	}

	try {
		return JSON.parse(raw);
	} catch {
		return defaultWorkspaceState;
	}
};
