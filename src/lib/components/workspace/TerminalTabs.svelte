<script lang="ts">
	import {
		createTerminalSession,
		terminalSessions
	} from '$lib/components/workspace/TerminalSessionManager';

	let active = '';

	const createSession = () => {
		const session = createTerminalSession();
		active = session.id;
	};
</script>

<div class="terminal-tabs">
	<div class="tabs">
		{#each $terminalSessions as session}
			<button class:active={active === session.id}>
				{session.name}
			</button>
		{/each}

		<button class="new" on:click={createSession}>+</button>
	</div>
</div>

<style>
	.terminal-tabs {
		display: flex;
		align-items: center;
		height: 40px;
		border-bottom: 1px solid rgba(255,255,255,0.08);
	}

	.tabs {
		display: flex;
		align-items: center;
		gap: 6px;
		padding: 0 8px;
	}

	button {
		padding: 6px 12px;
		border-radius: 8px;
		border: none;
		background: rgba(255,255,255,0.05);
		cursor: pointer;
	}

	button.active {
		background: rgba(255,255,255,0.12);
	}
</style>
