import { writable } from 'svelte/store';

export type TerminalSession = {
	id: string;
	name: string;
	output: string[];
};

export const terminalSessions = writable<TerminalSession[]>([]);

export const createTerminalSession = (name = 'terminal') => {
	const session = {
		id: crypto.randomUUID(),
		name,
		output: []
	};

	terminalSessions.update((sessions) => [...sessions, session]);

	return session;
};
