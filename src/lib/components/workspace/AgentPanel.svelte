<script lang="ts">
	let tasks = [
		'Repo indexing',
		'Workspace analysis',
		'Agent planning'
	];
</script>

<div class="agent-panel">
	<div class="header">AI AGENT</div>

	<div class="task-list">
		{#each tasks as task}
			<div class="task-item">
				<span class="status"></span>
				<span>{task}</span>
			</div>
		{/each}
	</div>
</div>

<style>
	.agent-panel {
		height: 100%;
		display: flex;
		flex-direction: column;
		padding: 14px;
		gap: 12px;
	}

	.header {
		font-size: 12px;
		font-weight: 700;
		letter-spacing: 0.08em;
		opacity: 0.7;
	}

	.task-list {
		display: flex;
		flex-direction: column;
		gap: 10px;
	}

	.task-item {
		display: flex;
		align-items: center;
		gap: 10px;
		padding: 10px;
		border-radius: 10px;
		background: rgba(255,255,255,0.04);
	}

	.status {
		width: 8px;
		height: 8px;
		border-radius: 999px;
		background: #58d68d;
	}
</style>
