# data_collection/telegram_data_collector.py
import os
import json
import pandas as pd
from pyrogram import Client
from datetime import datetime
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Load credentials from telegram_auth_setup.py
from auth.telegram_auth_setup import fetch_api_credentials
API_ID, API_HASH = fetch_api_credentials()

# Define target e-commerce channels
TARGET_CHANNELS = [
    "EthioMarketPlace",
    "AddisBazaar",
    "HabeshaShopOnline",
    "TadesseTrades",
    "GonderGoods"
]

def collect_telegram_data():
    """
    Collects messages from specified Telegram channels and saves them in JSON and CSV formats.
    """
    # Initialize Pyrogram client
    app = Client("ethio_ecommerce_bot", api_id=API_ID, api_hash=API_HASH)
    
    collected_data = []
    
    with app:
        for channel_name in TARGET_CHANNELS:
            logger.info(f"Starting data collection from {channel_name}")
            try:
                chat_details = app.get_chat(channel_name)
                channel_name_display = chat_details.title
                
                for msg in app.get_chat_history(channel_name, limit=500):  # Increased limit for more data
                    msg_content = msg.text or msg.caption or ""
                    if not msg_content.strip():
                        continue  # Skip empty messages
                    
                    msg_entry = {
                        "source_channel": channel_name,
                        "channel_display_name": channel_name_display,
                        "message_unique_id": msg.id,
                        "date_recorded": msg.date.isoformat(),
                        "message_content": msg_content.strip(),
                        "view_count": msg.views if msg.views else 0,
                        "media_category": str(msg.media) if msg.media else "None",
                        "includes_image": bool(msg.photo),
                        "includes_file": bool(msg.document)
                    }
                    collected_data.append(msg_entry)
            
            except Exception as scrape_error:
                logger.error(f"Failed to scrape {channel_name}: {scrape_error}")
    
    if not collected_data:
        logger.warning("No data was collected from any channel.")
        return
    
    # Set up output directory
    output_base = "data_collection/raw_data"
    os.makedirs(output_base, exist_ok=True)
    
    # Generate timestamped filenames
    time_stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    json_output = os.path.join(output_base, f"ethio_telegram_data_{time_stamp}.json")
    csv_output = os.path.join(output_base, f"ethio_telegram_data_{time_stamp}.csv")
    
    # Save to JSON
    with open(json_output, 'w', encoding='utf-8') as json_file:
        json.dump(collected_data, json_file, ensure_ascii=False, indent=4)
    
    # Save to CSV
    df = pd.DataFrame(collected_data)
    df.to_csv(csv_output, index=False, encoding='utf-8-sig')
    
    logger.info(f"Successfully collected {len(collected_data)} messages.")
    logger.info(f"JSON file saved at: {json_output}")
    logger.info(f"CSV file saved at: {csv_output}")
    
    return collected_data

if __name__ == "__main__":
    collect_telegram_data()