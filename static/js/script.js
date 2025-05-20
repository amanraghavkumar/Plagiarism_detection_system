document.getElementById("plagiarismForm").addEventListener("submit", function (e) {
    e.preventDefault();
    let formData = new FormData(this);

    fetch("/", {
        method: "POST",
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("plagiarismScore").innerText = `Plagiarism Score: ${data.plagiarism_score}%`;
        document.getElementById("aiGenerated").innerText = `AI-Generated: ${data.ai_generated}`;
        document.getElementById("onlinePlagiarism").innerText = `Online Plagiarism: ${data.online_plagiarism}%`;
    })
    .catch(error => console.error("Error:", error));
});
