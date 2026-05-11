export class TerminalResizeObserver {
	private observer: ResizeObserver | null = null;

	observe(element: HTMLElement, callback: () => void) {
		this.observer = new ResizeObserver(() => {
			callback();
		});

		this.observer.observe(element);
	}

	disconnect() {
		this.observer?.disconnect();
	}
}
