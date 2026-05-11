import {
	activeWorkspaceTab,
	workspaceTabs
} from '$lib/stores/workspace';

import {
	readWorkspaceFile,
	writeWorkspaceFile
} from '$lib/apis/workspace';

export const openWorkspaceFile = async (path: string) => {
	const file = await readWorkspaceFile(path);

	workspaceTabs.update((tabs) => {
		const exists = tabs.find((tab) => tab.path === path);

		if (exists) {
			activeWorkspaceTab.set(exists.id);
			return tabs;
		}

		const tab = {
			id: crypto.randomUUID(),
			path,
			content: file.content
		};

		activeWorkspaceTab.set(tab.id);

		return [...tabs, tab];
	});
};

export const saveWorkspaceTab = async (
	path: string,
	content: string
) => {
	return writeWorkspaceFile(path, content);
};
