import os

def clean_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    if not lines:
        return

    # Check for start marker
    start_index = 0
    if lines[0].strip().startswith('```'):
        print(f"Found start marker in {filepath}")
        start_index = 1
    
    # Check for end marker
    end_index = len(lines)
    if lines[-1].strip() == '```':
        print(f"Found end marker in {filepath}")
        end_index = -1
    elif lines[-1].strip() == '' and lines[-2].strip() == '```':
         print(f"Found end marker in {filepath} (before newline)")
         end_index = -2

    if start_index == 0 and end_index == len(lines):
        return # No changes needed

    new_content = lines[start_index:end_index]
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.writelines(new_content)
    print(f"Cleaned {filepath}")

def main():
    docs_dir = 'docs'
    for root, dirs, files in os.walk(docs_dir):
        for file in files:
            if file.endswith('.md'):
                clean_file(os.path.join(root, file))

if __name__ == "__main__":
    main()
