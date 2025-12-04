# Rotherhithe Theatre Project Manual - Digital Edition

This repository contains the source code and content for the interactive digital edition of the **Rotherhithe Theatre Project Manual**.

The site is built using **MkDocs** with the **Material** theme, designed to be a "living workbook" for venue development projects.

## 🚀 Quick Start (Using Docker)

The easiest way to run the site is using Docker. You do not need to install Python or MkDocs locally.

### Prerequisites
- Docker Desktop installed and running.

### Run the Site
1. Open a terminal in this folder.
2. Run the following command:
   ```bash
   docker compose up --build
   ```
3. Open your browser to **[http://localhost:8000](http://localhost:8000)**.

The site will automatically reload if you edit any files in the `docs/` folder.

---

## 🛠️ Manual Installation (No Docker)

If you prefer to run it natively on your machine:

1. **Install Python 3.9+**
2. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Run the Dev Server:**
   ```bash
   mkdocs serve
   ```

---

## 📂 Project Structure

- **`docs/`**: Contains all the content files (Markdown).
    - **`getting-started/`**: Executive Summary, Quick Start.
    - **`phases/`**: Core project phases (Discovery, Implementation, Closure).
    - **`specialist/`**: Deep-dive guides (Rail Safety, Finance, etc.).
    - **`toolkit/`**: Templates and checklists.
    - **`assets/`**: CSS and JavaScript files.
- **`mkdocs.yml`**: The main configuration file (navigation, theme settings).
- **`Dockerfile`**: Configuration for the Docker container.

## 📝 Editing Content

1. Navigate to the `docs/` folder.
2. Open any `.md` file in a text editor (VS Code, Notepad++, etc.).
3. Make your changes.
4. If the server is running, the site will update instantly.

### Interactive Blocks
To add a new interactive note area, use the following HTML structure in your Markdown:

```html
<div class="interactive-block">
    <h3>MY BLOCK TITLE</h3>
    <p>Instructions for the user...</p>
    <textarea id="unique-id-for-persistence" class="user-note" placeholder="Type here..."></textarea>
</div>
```
*Note: The `id` must be unique for the data to be saved correctly.*

## 📄 License
© 2025 Craig Cox. See the Manual for full copyright and usage notices.
