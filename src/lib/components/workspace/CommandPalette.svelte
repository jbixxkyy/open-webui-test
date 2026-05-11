<script lang="ts">
	import { createEventDispatcher } from 'svelte';

	const dispatch = createEventDispatcher();

	let query = '';

	const commands = [
		'Open File',
		'Run Command',
		'Search Workspace',
		'Open Terminal',
		'Start Agent Task'
	];

	$: filtered = commands.filter((command) =>
		command.toLowerCase().includes(query.toLowerCase())
	);

	const execute = (command: string) => {
		dispatch('execute', { command });
	};
</script>

<div class="command-palette">
	<input bind:value={query} placeholder="Type a command..." />

	<div class="results">
		{#each filtered as command}
			<button on:click={() => execute(command)}>
				{command}
			</button>
		{/each}
	</div>
</div>

<style>
	.command-palette {
		display: flex;
		flex-direction: column;
		gap: 12px;
		padding: 16px;
		background: #11151b;
		border: 1px solid rgba(255,255,255,0.08);
		border-radius: 14px;
	}

	input {
		padding: 12px;
		border-radius: 10px;
		border: 1px solid rgba(255,255,255,0.08);
		background: rgba(255,255,255,0.04);
	}

	.results {
		display: flex;
		flex-direction: column;
		gap: 8px;
	}

	button {
		padding: 10px;
		border-radius: 10px;
		border: none;
		background: rgba(255,255,255,0.05);
		text-align: left;
		cursor: pointer;
	}
</style>
