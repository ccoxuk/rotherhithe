document.addEventListener("DOMContentLoaded", function() {
    // 1. Convert "::: interactive-block" divs into actual interactive forms
    // Note: MkDocs might render the ::: as a paragraph or code block depending on extensions.
    // However, our Python script will convert them to HTML divs with class 'interactive-block'
    // OR we can target the specific structure if we use the Admonition extension syntax.
    
    // Let's assume our Python script converts the `::: interactive-block` syntax 
    // into `<div class="interactive-block">...</div>` or we target the textareas directly.
    
    // Initialize all textareas with class 'user-note'
    const notes = document.querySelectorAll('.user-note');
    
    notes.forEach(note => {
        const id = note.id;
        if (!id) return;

        // Load saved value
        const savedValue = localStorage.getItem(id);
        if (savedValue) {
            note.value = savedValue;
        }

        // Save on input
        note.addEventListener('input', function() {
            localStorage.setItem(id, this.value);
            showSaveStatus(this);
        });
    });

    // Checkbox persistence
    const checkboxes = document.querySelectorAll('input[type="checkbox"]');
    checkboxes.forEach((box, index) => {
        // Create a unique ID based on page URL and index if not present
        const pageId = window.location.pathname;
        const uniqueId = `checkbox-${pageId}-${index}`;
        
        // Load state
        const savedState = localStorage.getItem(uniqueId);
        if (savedState === 'true') {
            box.checked = true;
        }

        // Save state
        box.addEventListener('change', function() {
            localStorage.setItem(uniqueId, this.checked);
        });
    });
});

function showSaveStatus(element) {
    // Find or create status indicator
    let status = element.nextElementSibling;
    if (!status || !status.classList.contains('save-status')) {
        status = document.createElement('div');
        status.className = 'save-status';
        status.textContent = 'Saved to browser storage';
        element.parentNode.insertBefore(status, element.nextSibling);
    }
    
    status.classList.add('visible');
    setTimeout(() => {
        status.classList.remove('visible');
    }, 2000);
}
