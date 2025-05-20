
from sentence_transformers import SentenceTransformer, util
import numpy as np
# model = SentenceTransformer("sentence-transformers/paraphrase-mpnet-base-v2")
model = SentenceTransformer("cross-encoder/ms-marco-MiniLM-L-12-v2")

def check_similarity(text, reference_texts=None):
    """
    Calculate plagiarism score using sentence similarity
    and detect AI-generated content with improved accuracy.
    """
    if reference_texts is None:
        reference_texts = ["Predefined dataset text"]

    ai_reference_texts = [
        "AI-generated text looks like this.",
        "Machine learning models generate content like this.",
        "This text is generated using an AI model.",
        "Artificial intelligence creates structured text like this."
    ]
    
    combined_references = reference_texts + ai_reference_texts

    text_embedding = model.encode(text, convert_to_tensor=True)
    ref_embeddings = model.encode(combined_references, convert_to_tensor=True)

    similarity_scores = util.pytorch_cos_sim(text_embedding, ref_embeddings).cpu().numpy()

    top_k_scores = np.sort(similarity_scores.flatten())[-3:] 
    plagiarism_score = round(np.mean(top_k_scores) * 100, 2)

    ai_generated = "Yes" if plagiarism_score >= 50 else "No"  

    return plagiarism_score #ai_generated
    


