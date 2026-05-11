<script lang="ts">
	export let files: string[] = [
		'src/routes/+page.svelte',
		'src/lib/components/workspace/WorkspaceLayout.svelte',
		'backend/main.py'
	];

	export let selected = files[0];
</script>

<div class="explorer">
	<div class="header">EXPLORER</div>

	<div class="tree">
		{#each files as file}
			<button
				class:selected={selected === file}
				on:click={() => (selected = file)}
			>
				<span>📄</span>
				<span>{file}</span>
			</button>
		{/each}
	</div>
</div>

<style>
	.explorer {
		height: 100%;
		display: flex;
		flex-direction: column;
	}

	.header {
		padding: 14px;
		font-size: 12px;
		font-weight: 700;
		letter-spacing: 0.08em;
		opacity: 0.7;
	}

	.tree {
		display: flex;
		flex-direction: column;
		gap: 2px;
		padding: 0 8px;
	}

	button {
		display: flex;
		align-items: center;
		gap: 10px;
		padding: 10px;
		border-radius: 8px;
		background: transparent;
		border: none;
		cursor: pointer;
		text-align: left;
		font-size: 13px;
	}

	button:hover,
	button.selected {
		background: rgba(255,255,255,0.08);
	}
</style>
