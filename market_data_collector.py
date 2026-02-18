import logging
from typing import Dict, Optional, List
import requests
from datetime import datetime

class MarketDataCollector:
    """
    Collects real-time market data from various sources for revenue analysis.

    Attributes:
        data_sources (Dict[str, str]): Mapping of data types to API endpoints.
        last_fetch_time (datetime): Timestamp of the last successful data fetch.
        api_keys (Dict[str, str]): Dictionary storing required API keys.
    """

    def __init__(self, config):
        self.data_sources = config['data_sources']
        self.api_keys = config.get('api_keys', {})
        self.last_fetch_time = None
        logging.basicConfig(
            filename='market_data.log',
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s'
        )

    def fetch_data(self, data_type: str) -> Optional[Dict]:
        """
        Fetches market data for the specified type from configured sources.

        Args:
            data_type (str): Type of data to fetch (e.g., 'price', 'volume').

        Returns:
            Dict: Fetched data or None if failed.
        """
        try:
            endpoint = self.data_sources.get(data_type)
            if not endpoint:
                logging.error(f"No source configured for data type: {data_type}")
                return None

            params = {
                'api_key': self.api_keys.get('key'),
                'timestamp': datetime.now().isoformat()
            }

            response = requests.get(endpoint, params=params)
            response.raise_for_status()

            data = response.json()
            logging.info(f"Successfully fetched {data_type} data: {data}")
            self.last_fetch_time = datetime.now()

            return data

        except requests.exceptions.RequestException as e:
            logging.error(f"Failed to fetch {data_type} data from {endpoint}: {str(e)}")
            return None