<script lang="ts">
	type ActivityItem = {
		id: string;
		label: string;
		icon: string;
	};

	export let active = 'explorer';
	export let items: ActivityItem[] = [
		{ id: 'explorer', label: 'Explorer', icon: '📁' },
		{ id: 'search', label: 'Search', icon: '🔎' },
		{ id: 'agent', label: 'Agent', icon: '🤖' },
		{ id: 'git', label: 'Source Control', icon: '⑂' },
		{ id: 'settings', label: 'Settings', icon: '⚙️' }
	];

	const select = (id: string) => {
		active = id;
	};
</script>

<nav class="activity-sidebar" aria-label="Workspace activity bar">
	{#each items as item}
		<button
			class:active={active === item.id}
			title={item.label}
			aria-label={item.label}
			on:click={() => select(item.id)}
		>
			<span>{item.icon}</span>
		</button>
	{/each}
</nav>

<style>
	.activity-sidebar {
		display: flex;
		align-items: center;
		flex-direction: column;
		gap: 6px;
		padding: 10px 6px;
		height: 100%;
		background: rgba(255, 255, 255, 0.02);
	}

	button {
		width: 40px;
		height: 40px;
		display: grid;
		place-items: center;
		border-radius: 10px;
		border: 1px solid transparent;
		background: transparent;
		font-size: 18px;
		cursor: pointer;
		opacity: 0.68;
	}

	button:hover,
	button.active {
		opacity: 1;
		background: rgba(255, 255, 255, 0.08);
		border-color: rgba(255, 255, 255, 0.08);
	}
</style>
