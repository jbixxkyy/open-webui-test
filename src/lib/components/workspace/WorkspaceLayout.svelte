<script lang="ts">
	export let sidebarOpen = true;
	export let terminalOpen = true;
</script>

<div class="workspace-shell">
	<div class="activity-sidebar">
		<slot name="activity" />
	</div>

	{#if sidebarOpen}
		<div class="file-sidebar">
			<slot name="explorer" />
		</div>
	{/if}

	<div class="editor-region">
		<div class="workspace-tabs">
			<slot name="tabs" />
		</div>

		<div class="workspace-editor">
			<slot name="editor" />
		</div>

		{#if terminalOpen}
			<div class="workspace-terminal">
				<slot name="terminal" />
			</div>
		{/if}
	</div>
</div>

<style>
	.workspace-shell {
		display: flex;
		height: 100vh;
		width: 100%;
		background: var(--color-bg-0, #0f1115);
	}

	.activity-sidebar {
		width: 52px;
		border-right: 1px solid rgba(255,255,255,0.08);
	}

	.file-sidebar {
		width: 280px;
		border-right: 1px solid rgba(255,255,255,0.08);
	}

	.editor-region {
		flex: 1;
		display: flex;
		flex-direction: column;
	}

	.workspace-tabs {
		height: 42px;
		border-bottom: 1px solid rgba(255,255,255,0.08);
	}

	.workspace-editor {
		flex: 1;
		overflow: hidden;
	}

	.workspace-terminal {
		height: 240px;
		border-top: 1px solid rgba(255,255,255,0.08);
	}
</style>
