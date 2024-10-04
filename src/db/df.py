import pandas as pd
from typing import List, Dict, Optional

df = pd.DataFrame(columns=["image_link", "description"])


def update_dataframe(image_link: str, description: str):
    global df
    new_row = pd.DataFrame({"image_link": [image_link], "description": [description]})
    df = pd.concat([df, new_row], ignore_index=True)


def get_dataframe() -> pd.DataFrame:
    return df


def get_dataframe_as_dict() -> List[Dict[str, str]]:
    return df.to_dict(orient="records")


def get_dataframe_info() -> Dict[str, int]:
    return {"total_rows": len(df), "columns": list(df.columns)}


def clear_dataframe():
    global df
    df = pd.DataFrame(columns=["image_link", "description"])


def get_rows(start: int = 0, end: Optional[int] = None) -> List[Dict[str, str]]:
    return df.iloc[start:end].to_dict(orient="records")
