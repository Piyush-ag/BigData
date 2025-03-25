# Aspect-Based Sentiment Analysis on Yelp Reviews

##  Project Report:  
**Team_1_final_report.pptx**

---

##  Results:
1.  Successfully developed an **Aspect-Based Sentiment Analysis Model**.
2.  Extracted **actionable insights** from Yelp reviews for a given business.

---

##  Pre-Requisites to Run the Model:
1. **Yelp Review Dataset**  
   - [Download from Yelp](https://business.yelp.com/external-assets/files/Yelp-JSON.zip)  
   - Data size: **~4.5GB compressed** (~10GB uncompressed)  
   - Due to its size, it was **not included in the submission ZIP**.  

2. **Aspect Dictionary (`aspect_dictionary.csv`)**  
   - Included in the ZIP file.

---

##  About the Model:

###  **Data Collection and Structuring**
- Extracted **business-specific reviews** from a large Yelp dataset.
- Created a **focused dataset** reflecting customer experiences directly tied to the business.

###  **Sentiment Analysis - Comparing Two Models**
- **VADER Analysis**  
   Quick understanding of overall sentiment.  
   Useful for **daily or weekly** feedback monitoring.  

- **BERT Analysis**  
   Deeper insight into emotions and tone.  
   Captures **subtle nuances** that rule-based models like VADER might miss.

###  **Aspect-Based Sentiment Analysis**
- **Word Embeddings for Aspect Dictionary**  
  - Used **Word2Vec** to find the **top 250 words** with semantically similar meanings to predefined aspects (**food, pricing, ambiance, service quality**).  
  - **Fine-tuned** on **1 million+ reviews**.  

- **Aspect Sentiment Analysis with RoBERTa**  
  - Applied **RoBERTa model** to analyze sentiment for each aspect in the reviews.

###  **Data Visualization for Decision-Making**
- Built **actionable dashboards** for easy understanding of sentiment insights.
- **Managers & decision-makers** can track **sentiment trends over time** and adjust business strategies accordingly.

---

##  Key Features:
✔ Extracts **business-specific** reviews from a large dataset.  
✔ Uses **word embeddings (Word2Vec) for aspect identification**.  
✔ Applies **VADER & BERT** for sentiment analysis.  
✔ Implements **RoBERTa for Aspect-Based Sentiment Analysis**.  
✔ Provides **data visualization dashboards** for actionable insights.  

---

##  How to Run:
1. Download and extract **Yelp review dataset**.
2. Ensure **aspect_dictionary.csv** is in the working directory.
3. Run the **Python scripts** :  final_model.ipynb

---

##  Outcome:
 **Improved business decision-making** by extracting insights from customer reviews.  
 **Identified sentiment trends** to help businesses optimize their services.  
 **Automated NLP pipeline** for real-time customer feedback analysis.  

---

### Contact:
For any queries, feel free to reach out!  
 **Email:** [pagraw13@jh.edu](mailto:pagraw13@jh.edu)  

---

 **Project Report**:  `Team_1_final_report.pptx`