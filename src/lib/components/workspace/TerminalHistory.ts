export class TerminalHistory {
	private history: string[] = [];
	private pointer = -1;

	push(command: string) {
		this.history.push(command);
		this.pointer = this.history.length;
	}

	previous() {
		if (this.pointer > 0) {
			this.pointer -= 1;
		}

		return this.history[this.pointer] || '';
	}

	next() {
		if (this.pointer < this.history.length - 1) {
			this.pointer += 1;
		}

		return this.history[this.pointer] || '';
	}
}
