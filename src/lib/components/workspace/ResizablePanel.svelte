<script lang="ts">
	export let width = 280;
</script>

<div class="panel" style={`width:${width}px`}>
	<slot />
</div>

<style>
	.panel {
		height: 100%;
		min-width: 180px;
		max-width: 600px;
		resize: horizontal;
		overflow: auto;
		border-right: 1px solid rgba(255,255,255,0.08);
	}
</style>
