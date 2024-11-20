import pandas as pd

def pd_reader(file_name: str) -> pd.DataFrame:
    """reads a csv file and makes a dataframe

    Args:
        file_name (str): name of the csv doc to read

    Returns:
        pd.DataFrame: just returns a df to do other things with
    """
    df = pd.read_csv(file_name)
    return df

def dict_builder(frame: pd.DataFrame) -> dict[str: int]:
    """reads a dataFrame and creates a dicitonary of counties and their total positive cases. Accounts for all counties by haivng all files incorporate all counties as case count 0
        and goes from there.

    Args:
        frame (pd.DataFrame): yearly cases csv that has been read by pd_reader()

    Returns:
        dict: represents each county and their total positive cases
    """
    holder:dict[str: int] = {}
    for each, row in frame.iterrows():
        if row['County'] in holder:
            holder[row['County']] += row['Positive Cases']
        else:
            holder[row['County']] = row['Positive Cases']
    return holder
        
def data_frame_maker(dict: dict[str:int]) -> pd.DataFrame:
    """By taking a dicitonary of counties and their total positive cases, it creates a dataframe

    Args:
        dict (string: integer): a dictionary of counties and their total positive cases
    Returns:
        pd.DataFrame: returns the dicitonary as a dataframe
    """
    builtDF = pd.DataFrame(list(dict.items()), columns=['County', 'Total Positive Cases']) 
    return builtDF


def new_file_maker(df: pd.DataFrame, name: str) -> None:
    """Literally just makes a new file using a given dataframe and names the files

    Args:
        df (pd.DataFrame): given dataframe that gets turned into a csv!
        name (str): file name you want to give it + "SortedByCounty.csv"
    """
    df.to_csv("SortedByCounty/"+name+"SortedByCounty.csv", index=False)
    return

def main(folder: str,file: str) -> None:
    """Main function that does everything by sequentially calling the other functions. Needs a csv file to read.

    Args:
        folder (str): folder location of the files you want to read from
        file (str): file name without the .csv extension
    """
    df: pd.DataFrame = pd_reader(folder + file + ".csv")
    holder: dict[str: int] = dict_builder(df)
    new_df: pd.DataFrame = data_frame_maker(holder)
    new_file_maker(new_df, file) 
    return

def repeater() -> None:
    """Function specific for my use case. Calls main() for each year in the targets list
    """
    targets:list[str] = ['2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016']
    for i in targets:
        main("Yearly CSV/",i)
    return 

if __name__ == "__main__":
    repeater()
    print('done')
