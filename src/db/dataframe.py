import pandas as pd
from typing import List, Dict, Optional
from src.api.images_api import create_image

df = pd.DataFrame(columns=["image_link", "description"])


def update_dataframe(image_link: str, description: str):
    '''This function will update the dataframe with the new image link and description.'''
    global df
    new_row = pd.DataFrame({"image_link": [image_link], "description": [description]})
    df = pd.concat([df, new_row], ignore_index=True)


def get_dataframe() -> pd.DataFrame:
    '''This function will return the dataframe.'''
    return df


def get_dataframe_as_dict() -> List[Dict[str, str]]:
    '''This function will return the dataframe as a dictionary.'''
    return df.to_dict(orient="records")


def get_dataframe_info() -> Dict[str, int]:
    '''This function will return the dataframe information.'''
    return {"total_rows": len(df), "columns": list(df.columns)}


def clear_dataframe():
    '''This function will clear the dataframe.'''
    global df
    df = pd.DataFrame(columns=["image_link", "description"])


def get_rows(start: int = 0, end: Optional[int] = None) -> List[Dict[str, str]]:
    '''This function will return the rows of the dataframe.'''
    return df.iloc[start:end].to_dict(orient="records")


def save_dataframe_row_in_db(df: pd.DataFrame):
    '''This function will save the dataframe row in the database.'''
    pass
