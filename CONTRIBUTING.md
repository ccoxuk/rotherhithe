# Contributing to the Rotherhithe Theatre Manual

Thank you for your interest in contributing to the Rotherhithe Theatre Manual! This project is a living document designed to help venue managers and community groups.

## How to Contribute

### Reporting Issues
If you find an error, typo, or missing information, please [open an issue](https://github.com/ccoxuk/rotherhithe/issues) on GitHub.

### Suggesting Changes
1. **Fork the repository** to your own GitHub account.
2. **Clone the project** to your machine.
3. **Create a new branch** for your changes.
4. **Make your edits** in the `docs/` folder.
5. **Test your changes** locally using Docker (see README).
6. **Submit a Pull Request** (PR) to the `main` branch.

## Style Guide

- **Tone:** Professional, encouraging, and clear.
- **Formatting:** Use standard Markdown.
- **Interactivity:** Use `::: interactive-block` for sections where users should input their own data.

## Local Development

We use Docker to ensure a consistent environment.

```bash
docker compose up --build
```

This will serve the site at `http://localhost:8000`.
