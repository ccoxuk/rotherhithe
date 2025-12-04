import re
import os

# Configuration: Mapping Headers to File Paths
# This dictionary maps the H1/H2/H3 headers in the source markdown to specific output files.
# The script will grab content starting from the header until the next mapped header.

HEADER_MAP = {
    r"^## Executive Summary": "getting-started/executive-summary.md",
    r"^## How to Use This Manual": "getting-started/how-to-use.md",
    r"^## Quick Start Playbook": "getting-started/quick-start.md",
    
    r"^3\. \*\*Discovery Phase\*\*": "phases/discovery.md",
    r"^4\. \*\*Implementation Phase\*\*": "phases/implementation.md",
    r"^5\. \*\*Closure Phase\*\*": "phases/closure.md",
    
    r"^## Appendix 13\.11": "specialist/rail-safety.md",
    r"^7\. \*\*Planning & Permissions\*\*": "specialist/planning.md",
    r"^8\. \*\*Health, Safety & Accessibility\*\*": "specialist/health-safety.md",
    r"^9\. \*\*Financial Management\*\*": "specialist/finance.md",
    r"^10\. \*\*Community & Partnerships\*\*": "specialist/partnerships.md",
    
    r"^## Appendix 13\.5": "toolkit/risk-register.md",
    r"^## Appendix 13\.6": "toolkit/audience-survey.md",
    r"^## Appendix 13\.8": "toolkit/funder-report.md",
    r"^## Appendix 13\.9": "toolkit/hs-checklist.md",
    r"^## Appendix 13\.10": "toolkit/closure-checklist.md",
    # Rail Safety Addendum is 13.11 but mapped to specialist above. 
    # We might want it in toolkit too or just link it. Let's map it to toolkit as well if it appears differently?
    # Actually, the manual has "6. Railway-Adjacent..." which links to Appx 13.11.
    # Let's stick to the manual's flow.
    
    r"^## Appendix 13\.12": "toolkit/gdpr.md",
    r"^## Appendix 13\.13": "toolkit/accessibility.md",
    r"^## Appendix 13\.14": "toolkit/director-playbook.md",
    r"^## Appendix 13\.15": "toolkit/raci.md",
    r"^## Appendix 13\.16": "toolkit/milestones.md",
    r"^## Appendix 13\.17": "toolkit/post-project.md",
    r"^## Appendix 13\.18": "toolkit/budget.md",
    r"^## Appendix 13\.19": "specialist/partnerships.md", # 13.19 is Partnerships Playbook
    r"^## Appendix 13\.20": "toolkit/procurement.md",
    r"^## Appendix 13\.21": "toolkit/mou.md",
    r"^## Appendix 13\.22": "toolkit/dpa.md",
    r"^## Appendix 13\.23": "toolkit/gantt.md",
    r"^## Appendix 13\.24": "toolkit/legal-review.md",
    
    r"^<a id=\"useful-contacts\"></a>": "resources/contacts.md",
    r"^<a id=\"glossary\"></a>": "resources/glossary.md",
    r"^## Bibliography": "resources/bibliography.md"
}

SOURCE_FILE = "/Users/craig/Downloads/Rotherhithe_Theatre_Interactive_Workbook.md"
OUTPUT_BASE = "/Users/craig/Downloads/Rotherhithe_Manual_Site/docs"

def process_interactive_blocks(content, page_id):
    """
    Converts ::: interactive-block ... ::: into HTML with textareas.
    """
    # Regex to find the block
    pattern = r"::: interactive-block\n(.*?)\n:::"
    
    def replace_func(match):
        block_content = match.group(1)
        # Create a unique ID for the textarea based on the page and content hash/slug
        # For simplicity, we'll use a random-ish ID or sequential if possible, 
        # but page_id + index is safer.
        # Let's just use a simple hash of the title for the ID.
        title_match = re.search(r"\*\*(.*?)\*\*", block_content)
        title = title_match.group(1) if title_match else "note"
        safe_id = f"{page_id}-{re.sub(r'[^a-z0-9]', '', title.lower())}"
        
        html = f"""
<div class="interactive-block">
    <h3>{title}</h3>
    <p>{block_content.replace(f'**{title}**', '').strip()}</p>
    <textarea id="{safe_id}" class="user-note" placeholder="Type your notes here... (Auto-saved)"></textarea>
</div>
"""
        return html

    return re.sub(pattern, replace_func, content, flags=re.DOTALL)

def split_markdown():
    with open(SOURCE_FILE, 'r') as f:
        full_text = f.read()

    # Create index.md manually from the top part
    # Everything before "## Executive Summary" goes to index.md
    intro_match = re.search(r"(.*?)## Executive Summary", full_text, re.DOTALL)
    if intro_match:
        intro_text = intro_match.group(1)
        with open(f"{OUTPUT_BASE}/index.md", "w") as f:
            f.write(intro_text)
            print(f"Created index.md")

    # Iterate through headers and extract content
    # We need to sort headers by position in file to extract chunks correctly
    
    indices = []
    for pattern, filename in HEADER_MAP.items():
        match = re.search(pattern, full_text, re.MULTILINE)
        if match:
            indices.append((match.start(), pattern, filename))
    
    indices.sort() # Sort by start position
    
    for i in range(len(indices)):
        start_pos, pattern, filename = indices[i]
        
        # End position is the start of the next mapped header, or EOF
        if i < len(indices) - 1:
            end_pos = indices[i+1][0]
        else:
            end_pos = len(full_text)
            
        content = full_text[start_pos:end_pos]
        
        # Process Interactive Blocks
        page_id = filename.replace('/', '-').replace('.md', '')
        content = process_interactive_blocks(content, page_id)
        
        # Ensure directory exists
        full_path = f"{OUTPUT_BASE}/{filename}"
        os.makedirs(os.path.dirname(full_path), exist_ok=True)
        
        with open(full_path, "w") as f:
            f.write(content)
            print(f"Created {filename}")

if __name__ == "__main__":
    # Create resources dir if not exists
    os.makedirs(f"{OUTPUT_BASE}/resources", exist_ok=True)
    split_markdown()
