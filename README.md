# CACDD
This repository is for the paper "Atomic Claim Decomposition for RAG-Generated Responses: A Chinese Annotated Dataset"

The dataset is built from WebCPM dataset.

The data format is as follows:
```
{
  "question": a open-domain question,
  "answer": RAG generated Long-form answer,
  "sentence_classification": sentences from answer and are classified as fact-1, opinion-2, instruction-3 and other-4,
  "atomic_claim": atomic claims from fact sentences above
}
```
