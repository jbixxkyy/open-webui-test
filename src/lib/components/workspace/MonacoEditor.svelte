<script lang="ts">
	import { onMount } from 'svelte';

	let editorContainer: HTMLDivElement;
	let initialized = false;

	export let value = `// Cursor-style AI workspace\n\nfunction startAgentSystem() {\n\tconsole.log('Agent runtime initialized');\n}\n\nstartAgentSystem();`;

	onMount(async () => {
		try {
			const monaco = await import('monaco-editor');

			monaco.editor.create(editorContainer, {
				value,
				language: 'typescript',
				theme: 'vs-dark',
				automaticLayout: true,
				minimap: {
					enabled: true
				},
				fontSize: 14,
				fontFamily: 'JetBrains Mono, monospace'
			});

			initialized = true;
		} catch (err) {
			console.error('Monaco failed to initialize', err);
		}
	});
</script>

<div class="editor-wrapper">
	{#if !initialized}
		<div class="loading">Loading Monaco Editor...</div>
	{/if}

	<div bind:this={editorContainer} class="editor"></div>
</div>

<style>
	.editor-wrapper {
		position: relative;
		height: 100%;
		width: 100%;
		background: #1e1e1e;
	}

	.editor {
		height: 100%;
		width: 100%;
	}

	.loading {
		position: absolute;
		inset: 0;
		display: flex;
		align-items: center;
		justify-content: center;
		font-size: 14px;
		opacity: 0.7;
		z-index: 2;
	}
</style>
