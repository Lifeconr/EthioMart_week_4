# data_processing/amharic_data_cleaner.py
import re
import pandas as pd
from nltk.tokenize import wordpunct_tokenize
import os
import sys

# Custom Amharic text cleaner function
def sanitize_amharic_content(raw_text):
    """
    Sanitizes Amharic text by removing non-essential elements like URLs, special characters,
    and normalizing the text for downstream NER tasks.
    """
    if not isinstance(raw_text, str):
        return ""
    
    # Strip URLs and hyperlinks
    raw_text = re.sub(r'(https?://\S+)|www\.\S+', '', raw_text)
    
    # Retain Amharic characters (U+1200 to U+137F) and basic separators
    raw_text = re.sub(r'[^\u1200-\u137F\s.,!?0-9]', '', raw_text)
    
    # Collapse multiple spaces into a single space
    raw_text = ' '.join(raw_text.split())
    
    return raw_text.strip()

# Main data preprocessing function
def process_telegram_data(input_file_path):
    """
    Loads raw Telegram data from a JSON file, cleans the text, tokenizes it,
    and saves the processed data to a CSV file in a structured format.
    """
    # Check if the input file exists
    if not os.path.isfile(input_file_path):
        raise FileNotFoundError(f"Input file not located at: {input_file_path}")

    print(f"Starting to process data from: {input_file_path}")
    
    # Load JSON data
    with open(input_file_path, 'r', encoding='utf-8') as file_handle:
        data_records = pd.read_json(file_handle)
    
    # Apply text sanitization
    data_records['processed_text'] = data_records['text'].apply(sanitize_amharic_content)
    
    # Tokenize the cleaned text
    data_records['token_list'] = data_records['processed_text'].apply(wordpunct_tokenize)
    
    # Remove entries with no meaningful content
    data_records = data_records[data_records['processed_text'].str.len() > 0]
    
    # Define output directory and file path
    output_dir = os.path.join(os.path.dirname(input_file_path).replace('raw', 'cleaned'))
    os.makedirs(output_dir, exist_ok=True)
    output_file = os.path.join(output_dir, os.path.basename(input_file_path).replace('.json', '_cleaned.csv'))
    
    # Save the processed dataframe to CSV
    data_records.to_csv(output_file, index=False, encoding='utf-8-sig')
    print(f"Data processing complete. Saved to: {output_file}")
    
    return data_records

if __name__ == "__main__":
    # Accept command-line argument or use a default path
    if len(sys.argv) > 1:
        data_source = sys.argv[1]
    else:
        data_source = "data/raw/telegram_data_20250623_2211.json"
        print(f"Default path used since no argument provided: {data_source}")
    
    process_telegram_data(data_source)