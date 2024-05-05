# Look Up Letters (LUL) - Q&A for Stakeholder Letters
Team Members:
Wesley Barnes, 
Brandon Charletta, 
Micah Richardson, &
Luisa Schenk

## Project Overview
### Problem Statement
CEO letters to their stakeholders are often lengthy and may lose the reader's interest. Stakeholders need a tool to quickly extract relevant information without having to read the entire content. This project develops a search tool that retrieves pertinent information from CEO letters, enhancing efficiency for traders, stakeholders, and the general public.

### Data
The dataset consists of 357 CEO letters in text format, stored in a JSONL file. Each letter typically contains up to 20,000 characters, including the CEO's name, company name, and letter title. These letters are published annually at the start of the company's reporting period. The dataset was processed to ignore common stop words and normalize text to lowercase to maintain uniformity and relevance.

### Model Procedure
We utilized the BM25 algorithm for information retrieval due to its effectiveness in handling sparse and lengthy texts. The model processes preprocessed text data to rank and retrieve the most relevant sections of text in response to user queries.

## Technical Details
### Dependency Management
All dependencies are listed in a requirements.txt file, ensuring code reproducibility.

### Code Organization and Clarity
The project is structured in a Jupyter notebook with clear Markdown headers and sections. The code is organized logically with concise comments explaining each block's purpose, facilitating easy navigation and understanding. The notebook provides five different input query examples with corresponding outputs, demonstrating the practical application of the model.

### Web Application
The model was served with a flask application and its corresponding html and css files. This site returns the highest scored BM25 score to the user when they ask a question about any one of the CEO letters; ensuring that the user does not need to go through the pain of reading the letters in their entirety.


