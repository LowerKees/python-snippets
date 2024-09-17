import pandas as pd


def list_ultimate_parents(
    df: pd.DataFrame,
    child_col_name: str,
    parent_col_name: str,
    ultimate_parent_col_name: str = "ultimate_parent",
) -> pd.Series:
    """Finds a list of ultimate parents in a data frame.

    The input data frame should have at least to series, with one series representing
    the child in the relationship, and one series representing the parent in the
    relationship.

    Args:
        df: data frame containing the parent-child-relationship.
        child_col_name: name of the series that contains the child element.
        parent_col_name: name of the series that contains the parent element.
        ultimate_parent_col_name: name of the series that is returned by the function.

    Returns:
        a pandas Series instance containing the ultimate parents from the input data
            frame.
    """
    child_suffix = "_child"
    parent_suffix = "_parent"
    df_joined = pd.merge(
        df,
        df,
        how="left",
        left_on=parent_col_name,
        right_on=child_col_name,
        suffixes=[child_suffix, parent_suffix],
    )
    ultimate_parents = df_joined.loc[
        df_joined[f"{child_col_name}{parent_suffix}"].isna(),
        f"{parent_col_name}{child_suffix}",
    ]

    ultimate_parents.rename(ultimate_parent_col_name, inplace=True)

    return ultimate_parents


def _ultimate_parents(child_col: pd.Series, parent_col: pd.Series) -> pd.Series:
    child_col_name = "children"
    parent_col_name = "parents"
    df = pd.DataFrame({child_col_name: child_col, parent_col_name: parent_col})

    # df_left = df.rename(columns={"children": "left_children", "parents": "parents"})
    # df_right = df.rename(columns={"children": "parents", "parents": "right_parents"})

    df = list_ultimate_parents(
        df=df, child_col_name=child_col_name, parent_col_name=parent_col_name
    )

children = pd.Series([1, 2, 3, 4])
parents = pd.Series([2, 3, 4, 5])

df = pd.DataFrame({"children": children, "parents": parents})

df = list_ultimate_parents(df=df, child_col_name="children", parent_col_name="parents")
