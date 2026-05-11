<script lang="ts">
	import { onMount } from 'svelte';

	import {
		getWorkspaceFiles,
		getWorkspaceTasks
	} from '$lib/apis/workspace';

	import {
		workspaceFiles,
		workspaceTasks
	} from '$lib/stores/workspace';

	onMount(async () => {
		try {
			const files = await getWorkspaceFiles();
			workspaceFiles.set(files);

			const tasks = await getWorkspaceTasks();
			workspaceTasks.set(tasks);
		} catch (error) {
			console.error('Workspace provider failed', error);
		}
	});
</script>

<slot />
