from flask import Flask, render_template, request, jsonify
from scripts.pdf_extractor import extract_text_from_pdf
from scripts.preprocessing import clean_text
from scripts.similarity import check_similarity
from scripts.ai_detection import detect_ai_generated_text
from scripts.web_scraper import check_online_plagiarism

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        text = request.form.get("text", "")
        pdf_file = request.files.get("pdf")

        if pdf_file:
            extracted_text = extract_text_from_pdf(pdf_file)
            text += " " + extracted_text  

        cleaned_text = clean_text(text)

        plagiarism_score = check_similarity(cleaned_text)
        ai_generated = detect_ai_generated_text(cleaned_text)
        online_plagiarism_score = check_online_plagiarism(cleaned_text)

        return jsonify({
            "plagiarism_score": plagiarism_score,
            "ai_generated": ai_generated,
            "online_plagiarism": online_plagiarism_score
        })

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
