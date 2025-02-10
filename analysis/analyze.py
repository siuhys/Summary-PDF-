import pandas as pd
from typing import List, Dict


def generate_summary(extracted_data: List[Dict]) -> pd.DataFrame:
    return pd.DataFrame(extracted_data)
