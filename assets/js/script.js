document.addEventListener('DOMContentLoaded', () => {
    const projectList = document.querySelector('#project-list ul');

    // Function to handle delete
    projectList.addEventListener('click', (e) => {
        if (e.target.classList.contains('delete-btn')) {
            const projectId = e.target.dataset.id;
            fetch(`/delete-project/${projectId}/`, {
                method: 'DELETE',
                headers: {
                    'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value
                }
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    e.target.parentElement.remove();
                }
            });
        }
    });
});
