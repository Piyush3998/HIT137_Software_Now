import spacy

# Load the SciSpaCy model
nlp = spacy.load("en_core_sci_sm")

# Test with a sample text
doc = nlp("Aspirin is used for treating pain and inflammation.")

for entity in doc.ents:
    print(entity.text, entity.label_)

# Load BioBERT to check if it is correctly installed
from transformers import pipeline

# Create a pipeline for Named Entity Recognition using BioBERT
ner_pipeline = pipeline("ner", model="dmis-lab/biobert-base-cased-v1.1", tokenizer="dmis-lab/biobert-base-cased-v1.1")

# Test BioBERT with a sample text
text = "Patient is suffering from diabetes and has been prescribed metformin."
entities = ner_pipeline(text)
print(entities)
