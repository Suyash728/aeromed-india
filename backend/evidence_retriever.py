"""
In-Memory Clinical Evidence Retriever (TF-IDF Vector Space Model)
Grounded on Adaption Labs Exported Datasets (2,050-Row Grade A Master Clinical Q&A,
9-Language Localized Advisories, Augmented Protocols, and CAQM GRAP Rules).
"""

import os
import glob
import logging
import pandas as pd
import numpy as np
from typing import Optional, Dict, Any, List
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

logger = logging.getLogger("innovate-aqi-api.retriever")

DATASET_METADATA_MAP = {
    "pan_india_master_clinical_qa_2050.csv": {
        "id": "8c3a464c-45c7-4164-aa8d-7a105125f3a9",
        "name": "Pan-India Respiratory Clinical Master Q&A (2,050 Rows)",
        "grade": "Grade A",
        "score": 9.4,
        "type": "combined_master"
    },
    "pan_india_aqi_clinical_qa_2000_grade_a.csv": {
        "id": "3bf58b6b-462c-4412-8171-fa1bed843e67",
        "name": "Pan-India AQI Respiratory Clinical Q&A (2,000 Rows)",
        "grade": "Grade A",
        "score": 9.4,
        "type": "invented"
    },
    "pan_india_localized_advisories.csv": {
        "id": "ac7589fd-355d-45e2-9168-4ab4a7e1ceef",
        "name": "Pan-India Localized Advisories (9 Indic Languages)",
        "grade": "Grade A",
        "score": 9.2,
        "type": "localized"
    },
    "indian_aqi_clinical_qa_50.csv": {
        "id": "cde47eea-5f78-4124-9a38-e46a6e0515a2",
        "name": "Indian AQI Clinical Q&A (50 Rows)",
        "grade": "Grade B",
        "score": 8.9,
        "type": "invented"
    },
    "pan_india_clinical_advisories_augmented_1003.csv": {
        "id": "24bada6c-7841-446c-9f12-b2bdec861d53",
        "name": "Pan-India Clinical Advisories (Augmented, 1,003 Rows)",
        "grade": "Grade B",
        "score": 8.8,
        "type": "augmented"
    },
    "caqm_grap_extracted_rules.csv": {
        "id": "31535351-f429-4240-a8ea-db8af555936e",
        "name": "CAQM Official GRAP Schedule Extracted Rules",
        "grade": "Statutory Standard",
        "score": 10.0,
        "type": "forge_extracted"
    },
    "multi_turn_clinical_trajectories.csv": {
        "id": "e6fd4ced-b683-4abb-8e99-77aa496456db",
        "name": "Multi-Turn Doctor-Patient Clinical Trajectories",
        "grade": "Grade A",
        "score": 9.3,
        "type": "trajectories"
    },
    "outdoor_workers_smog_protocols.csv": {
        "id": "0788bf56-1cf0-41fd-8a03-d255dc3ef4a7",
        "name": "India Outdoor Workers & High-Risk Commuter Smog Protocols",
        "grade": "Grade A",
        "score": 9.5,
        "type": "invented_localized"
    }
}


class ClinicalEvidenceRetriever:
    def __init__(self, data_dir: str):
        self.data_dir = data_dir
        self.documents: List[Dict[str, Any]] = []
        self.vectorizer: Optional[TfidfVectorizer] = None
        self.tfidf_matrix = None
        self.is_indexed = False

    def load_and_index(self):
        """Loads all available CSVs from data/adaption_exports/ and builds the vector index."""
        export_dir = os.path.join(self.data_dir, "adaption_exports")
        if not os.path.exists(export_dir):
            os.makedirs(export_dir, exist_ok=True)

        csv_files = sorted(glob.glob(os.path.join(export_dir, "*.csv")))
        docs = []

        for fpath in csv_files:
            fname = os.path.basename(fpath)
            meta = DATASET_METADATA_MAP.get(fname, {
                "id": "adaption_dataset_export",
                "name": fname.replace(".csv", "").replace("_", " ").title(),
                "grade": "Grade A",
                "score": 9.0,
                "type": "adaption_export"
            })

            try:
                df = pd.read_csv(fpath)
                for idx, row in df.iterrows():
                    # Extract prompt / title
                    prompt = (
                        row.get("enhanced_prompt") or
                        row.get("prompt") or
                        row.get("original_prompt") or
                        row.get("title") or
                        ""
                    )
                    # Extract completion / text
                    completion = (
                        row.get("enhanced_completion") or
                        row.get("completion") or
                        row.get("original_completion") or
                        row.get("text") or
                        ""
                    )

                    prompt_str = str(prompt).strip() if pd.notna(prompt) else ""
                    comp_str = str(completion).strip() if pd.notna(completion) else ""

                    if len(prompt_str) > 10 or len(comp_str) > 20:
                        docs.append({
                            "dataset_id": meta["id"],
                            "dataset_name": meta["name"],
                            "grade": meta.get("grade", "Grade A"),
                            "quality_score": meta.get("score", 9.4),
                            "prompt": prompt_str,
                            "completion": comp_str,
                            "search_text": f"{prompt_str} {comp_str[:300]}"
                        })
            except Exception as e:
                logger.warning(f"Error loading {fname} into retriever: {e}")

        self.documents = docs
        if not self.documents:
            logger.warning("No clinical evidence documents found to index.")
            self.is_indexed = False
            return

        # Fit TF-IDF Vectorizer
        corpus = [d["search_text"] for d in self.documents]
        self.vectorizer = TfidfVectorizer(
            max_features=15000,
            stop_words="english",
            ngram_range=(1, 2)
        )
        self.tfidf_matrix = self.vectorizer.fit_transform(corpus)
        self.is_indexed = True
        logger.info(f"ClinicalEvidenceRetriever successfully indexed {len(self.documents)} protocols from {len(csv_files)} datasets.")

    def search(self, query: str, top_k: int = 1, min_score: float = 0.12) -> Optional[Dict[str, Any]]:
        """Finds the best matching grounded clinical protocol for a given user query or clinical state."""
        if not self.is_indexed or self.vectorizer is None or self.tfidf_matrix is None:
            return None

        try:
            q_vec = self.vectorizer.transform([query])
            sims = cosine_similarity(q_vec, self.tfidf_matrix).flatten()
            best_idx = int(np.argmax(sims))
            best_score = float(sims[best_idx])

            if best_score < min_score:
                # Return top item anyway with fallback score indicator or return None
                return None

            match = self.documents[best_idx]
            return {
                "grounded_dataset_id": match["dataset_id"],
                "grounded_dataset_name": match["dataset_name"],
                "quality_grade": match["grade"],
                "quality_score": match["quality_score"],
                "matched_prompt": match["prompt"],
                "matched_clinical_protocol": match["completion"],
                "grounding_similarity_score": round(best_score, 4)
            }
        except Exception as e:
            logger.warning(f"Retriever search error: {e}")
            return None
