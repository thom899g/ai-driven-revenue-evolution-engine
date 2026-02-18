import logging
from typing import Dict, List
from datetime import datetime

class FeedbackLoop:
    """
    Processes market feedback and updates AI models accordingly.

    Attributes:
        last_update_time (datetime): Timestamp of the last update.
        model_updater: Handles model retraining based on new data.
    """

    def __init__(self):
        self.last_update_time = None
        self.model_updater = ModelUpdater()

    def process_feedback(self, feedback_data: Dict) -> bool:
        """
        Processes feedback data to improve AI models.

        Args:
            feedback_data (Dict): Feedback information to analyze.

        Returns:
            bool: True if update was successful, False otherwise.
        """
        try:
            self.model_updater.update_models(feedback_data)
            logging.info("Feedback processed successfully")
            self.last_update_time = datetime.now()
            return True

        except Exception as e:
            logging.error(f"Failed to process feedback: {str(e)}")
            return False