export type AgentTask = {
	id: string;
	title: string;
	status: 'pending' | 'running' | 'completed' | 'failed';
};

export class AgentRuntime {
	private tasks: AgentTask[] = [];

	createTask(title: string) {
		const task: AgentTask = {
			id: crypto.randomUUID(),
			title,
			status: 'pending'
		};

		this.tasks.push(task);
		return task;
	}

	startTask(id: string) {
		const task = this.tasks.find((t) => t.id === id);

		if (task) {
			task.status = 'running';
		}
	}

	completeTask(id: string) {
		const task = this.tasks.find((t) => t.id === id);

		if (task) {
			task.status = 'completed';
		}
	}

	getTasks() {
		return this.tasks;
	}
}
