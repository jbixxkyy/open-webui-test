<script lang="ts">
	import ActivitySidebar from '$lib/components/workspace/ActivitySidebar.svelte';
	import AgentPanel from '$lib/components/workspace/AgentPanel.svelte';
	import FileExplorer from '$lib/components/workspace/FileExplorer.svelte';
	import MonacoEditor from '$lib/components/workspace/MonacoEditor.svelte';
	import ResizablePanel from '$lib/components/workspace/ResizablePanel.svelte';
	import TerminalPanel from '$lib/components/workspace/TerminalPanel.svelte';
	import WorkspaceLayout from '$lib/components/workspace/WorkspaceLayout.svelte';
	import WorkspaceProvider from '$lib/components/workspace/WorkspaceProvider.svelte';
	import WorkspaceTabs from '$lib/components/workspace/WorkspaceTabs.svelte';
</script>

<WorkspaceProvider>
	<WorkspaceLayout>
		<svelte:fragment slot="activity">
			<ActivitySidebar />
		</svelte:fragment>

		<svelte:fragment slot="explorer">
			<ResizablePanel>
				<FileExplorer />
			</ResizablePanel>
		</svelte:fragment>

		<svelte:fragment slot="tabs">
			<WorkspaceTabs />
		</svelte:fragment>

		<svelte:fragment slot="editor">
			<MonacoEditor />
		</svelte:fragment>

		<svelte:fragment slot="terminal">
			<TerminalPanel />
		</svelte:fragment>
	</WorkspaceLayout>
</WorkspaceProvider>

<div class="agent-drawer">
	<AgentPanel />
</div>

<style>
	.agent-drawer {
		position: fixed;
		top: 0;
		right: 0;
		width: 320px;
		height: 100vh;
		background: rgba(15,17,21,0.98);
		border-left: 1px solid rgba(255,255,255,0.08);
	}
</style>
