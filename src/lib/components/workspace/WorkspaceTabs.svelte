<script lang="ts">
	export let tabs: string[] = [
		'WorkspaceLayout.svelte',
		'FileExplorer.svelte'
	];

	export let activeTab = tabs[0];
</script>

<div class="tabs">
	{#each tabs as tab}
		<button class:active={activeTab === tab} on:click={() => (activeTab = tab)}>
			{tab}
		</button>
	{/each}
</div>

<style>
	.tabs {
		display: flex;
		align-items: center;
		height: 100%;
		overflow-x: auto;
	}

	button {
		height: 100%;
		padding: 0 16px;
		border: none;
		background: transparent;
		border-right: 1px solid rgba(255,255,255,0.08);
		cursor: pointer;
		font-size: 13px;
		opacity: 0.7;
	}

	button.active {
		opacity: 1;
		background: rgba(255,255,255,0.06);
	}
</style>
