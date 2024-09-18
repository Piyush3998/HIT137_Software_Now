import spacy
from collections import Counter
from transformers import pipeline

# Load SciSpaCy models
nlp_sci_sm = spacy.load("en_core_sci_sm")
nlp_bc5cdr = spacy.load("en_ner_bc5cdr_md")

# Load BioBERT model using Hugging Face Transformers
biobert_ner_pipeline = pipeline("ner", model="dmis-lab/biobert-base-cased-v1.1", tokenizer="dmis-lab/biobert-base-cased-v1.1")

def extract_entities_scipacy(text, model):
    doc = model(text)
    diseases = [ent.text for ent in doc.ents if ent.label_ == "DISEASE"]
    drugs = [ent.text for ent in doc.ents if ent.label_ == "CHEMICAL"]
    return diseases, drugs

def extract_entities_biobert(text):
    entities = biobert_ner_pipeline(text)
    diseases = [ent['word'] for ent in entities if 'disease' in ent['entity'].lower()]
    drugs = [ent['word'] for ent in entities if 'drug' in ent['entity'].lower() or 'chemical' in ent['entity'].lower()]
    return diseases, drugs

def process_file(file_path, chunk_size=1024*1024):
    # Counters for entities
    sci_sm_diseases, sci_sm_drugs = Counter(), Counter()
    bc5cdr_diseases, bc5cdr_drugs = Counter(), Counter()
    biobert_diseases, biobert_drugs = Counter(), Counter()

    with open(file_path, 'r', encoding='utf-8') as file:
        while True:
            text_chunk = file.read(chunk_size)
            if not text_chunk:
                break

            # Process with SciSpaCy models
            diseases_sci_sm, drugs_sci_sm = extract_entities_scipacy(text_chunk, nlp_sci_sm)
            diseases_bc5cdr, drugs_bc5cdr = extract_entities_scipacy(text_chunk, nlp_bc5cdr)

            # Update counters for SciSpaCy models
            sci_sm_diseases.update(diseases_sci_sm)
            sci_sm_drugs.update(drugs_sci_sm)
            bc5cdr_diseases.update(diseases_bc5cdr)
            bc5cdr_drugs.update(drugs_bc5cdr)

            # Process with BioBERT model
            diseases_biobert, drugs_biobert = extract_entities_biobert(text_chunk)

            # Update counters for BioBERT model
            biobert_diseases.update(diseases_biobert)
            biobert_drugs.update(drugs_biobert)

    return (sci_sm_diseases, sci_sm_drugs, bc5cdr_diseases, bc5cdr_drugs, biobert_diseases, biobert_drugs)

def compare_results(counter1, counter2, label):
    print(f"\nComparison for {label}:")
    print(f"Total entities detected by model 1: {sum(counter1.values())}")
    print(f"Total entities detected by model 2: {sum(counter2.values())}")

    common = counter1 & counter2
    diff1 = counter1 - counter2
    diff2 = counter2 - counter1

    print(f"Common entities detected: {len(common)}")
    print(f"Top common entities: {common.most_common(5)}")

    print(f"Entities unique to model 1: {len(diff1)}")
    print(f"Top unique entities in model 1: {diff1.most_common(5)}")

    print(f"Entities unique to model 2: {len(diff2)}")
    print(f"Top unique entities in model 2: {diff2.most_common(5)}")

# Example usage
file_path = r'output.txt'  # Replace with your .txt file path
results = process_file(file_path)

# Compare and display the results
compare_results(results[0], results[2], 'Diseases (SciSpaCy en_core_sci_sm vs. en_ner_bc5cdr_md)')
compare_results(results[1], results[3], 'Drugs (SciSpaCy en_core_sci_sm vs. en_ner_bc5cdr_md)')
compare_results(results[2], results[4], 'Diseases (en_ner_bc5cdr_md vs. BioBERT)')
compare_results(results[3], results[5], 'Drugs (en_ner_bc5cdr_md vs. BioBERT)')
