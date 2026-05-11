<script lang="ts">
	let logs: string[] = [
		'> npm run dev',
		'> starting workspace runtime...',
		'> agent system initialized'
	];
</script>

<div class="terminal-panel">
	<div class="terminal-header">
		<span>TERMINAL</span>
	</div>

	<div class="terminal-body">
		{#each logs as line}
			<div class="line">{line}</div>
		{/each}
	</div>
</div>

<style>
	.terminal-panel {
		height: 100%;
		display: flex;
		flex-direction: column;
		background: #0b0d10;
	}

	.terminal-header {
		height: 38px;
		display: flex;
		align-items: center;
		padding: 0 12px;
		border-bottom: 1px solid rgba(255,255,255,0.08);
		font-size: 12px;
		font-weight: 700;
	}

	.terminal-body {
		padding: 12px;
		font-family: monospace;
		font-size: 13px;
		overflow: auto;
	}

	.line {
		margin-bottom: 8px;
		color: #8ee28e;
	}
</style>
