<script lang="ts">
	export let path = '';

	const getIcon = (value: string) => {
		if (value.endsWith('.ts')) return '📘';
		if (value.endsWith('.js')) return '📙';
		if (value.endsWith('.py')) return '🐍';
		if (value.endsWith('.svelte')) return '🔥';
		if (value.endsWith('.json')) return '🧩';
		if (value.endsWith('.md')) return '📝';
		return '📄';
	};
</script>

<span>{getIcon(path)}</span>
