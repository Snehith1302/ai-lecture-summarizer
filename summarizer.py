from transformers import pipeline

# Load summarization pipeline (downloads once)
summarizer = pipeline(
    "summarization",
    model="facebook/bart-large-cnn"
)

def summarize_text(text):
    """
    Takes lecture text and returns an AI-generated summary
    """
    # Limit length for model stability
    text = text.strip()
    text = text[:3500]

    summary = summarizer(
        text,
        max_length=160,
        min_length=60,
        do_sample=False
    )

    return summary[0]["summary_text"]
