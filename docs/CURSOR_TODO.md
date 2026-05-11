# Cursor/Codex Workspace TODO

## Phase 1 — IDE Foundation

### Workspace UI
- [x] Create workspace shell layout
- [x] Create activity sidebar
- [x] Create file explorer UI
- [x] Create workspace tabs
- [x] Create terminal panel UI
- [x] Create Monaco editor component
- [x] Create AI agent panel
- [ ] Wire workspace into main app layout
- [ ] Add dockable/resizable panels
- [ ] Add workspace persistence
- [ ] Add command palette

---

## Phase 2 — Filesystem Layer

### Backend Filesystem API
- [x] Read files
- [x] Write files
- [ ] Create files
- [x] Delete files
- [ ] Rename files
- [ ] Create folders
- [ ] Watch file changes
- [ ] Workspace root selection

### Frontend File System
- [ ] Connect explorer to real filesystem
- [ ] Open files in Monaco editor
- [ ] Save modified files
- [ ] Multi-tab editing
- [ ] File icons + language detection

---

## Phase 3 — Terminal Runtime

### Backend Shell Runtime
- [ ] PTY shell backend
- [ ] Persistent terminal sessions
- [ ] Live terminal streaming
- [x] Command execution API
- [ ] Sandbox runtime support

### Frontend Terminal
- [ ] Connect xterm frontend
- [ ] Resize terminal dynamically
- [ ] Multiple terminal tabs
- [ ] Command history
- [ ] Terminal reconnect logic

---

## Phase 4 — Repo Intelligence

### Codebase Indexing
- [x] Repo scanner
- [ ] Symbol extraction
- [ ] tree-sitter integration
- [ ] ripgrep integration
- [ ] Dependency graph
- [ ] Workspace embeddings
- [ ] Vector database integration

### Semantic Search
- [ ] Semantic code search
- [ ] Function search
- [ ] Symbol search
- [ ] Cross-file references
- [x] Context ranking engine

---

## Phase 5 — Agent Runtime

### Agent System
- [x] Initial agent runtime structure
- [ ] Planner agent
- [ ] Tool execution engine
- [ ] Autonomous execution loop
- [ ] Retry/error recovery system
- [ ] Task orchestration
- [ ] Streaming agent updates

### Agent Tools
- [ ] Filesystem tool
- [ ] Terminal tool
- [ ] Git tool
- [ ] Search tool
- [ ] Browser tool
- [ ] Documentation tool
- [ ] Memory tool

---

## Phase 6 — Diff + Git Workflow

### Diff System
- [ ] Inline diff viewer
- [ ] Accept/reject edits
- [ ] Patch generation
- [ ] Rollback system
- [ ] File history viewer

### Git Integration
- [ ] Git status
- [ ] Branch switching
- [ ] Commit creation
- [ ] PR generation
- [ ] Git blame support
- [ ] Commit history browser

---

## Phase 7 — Memory + Context

### Long-Term Memory
- [ ] Repo summaries
- [ ] Architecture memory
- [ ] Coding style memory
- [ ] Prior decisions tracking
- [ ] Agent memory storage

### Context Engine
- [x] Context builder
- [ ] Context compression
- [ ] Smart retrieval pipeline
- [ ] Token budgeting
- [ ] Multi-file context assembly

---

## Phase 8 — Multi-Agent Architecture

### Specialized Agents
- [ ] Refactor agent
- [ ] Debug agent
- [ ] Search agent
- [ ] Test agent
- [ ] Documentation agent
- [ ] Review agent

### Coordination
- [ ] Agent orchestration layer
- [ ] Shared memory bus
- [ ] Inter-agent communication
- [ ] Task delegation system

---

## Phase 9 — Advanced Features

### Developer Experience
- [ ] AI autocomplete
- [ ] Inline edits
- [ ] Code actions
- [ ] AI terminal suggestions
- [ ] AI debugging workflows
- [ ] Workspace snapshots

### Collaboration
- [ ] Shared workspaces
- [ ] Live collaboration
- [ ] Shared agent sessions
- [ ] Multi-user editing
