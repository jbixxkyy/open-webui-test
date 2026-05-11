import { writable } from 'svelte/store';

export type WorkspaceTab = {
	id: string;
	path: string;
	content?: string;
	isDirty?: boolean;
	language?: string;
};

export const workspaceFiles = writable<string[]>([]);
export const workspaceTabs = writable<WorkspaceTab[]>([]);
export const activeWorkspaceTab = writable<string | null>(null);
export const workspaceTerminalOutput = writable<string[]>([]);
export const workspaceTasks = writable<any[]>([]);
export const workspaceEditorContent = writable<string>('');
