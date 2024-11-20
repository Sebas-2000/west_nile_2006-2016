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

def sorter(frame: pd.DataFrame) -> list:
    """reads a dataFrame and creates a list of size 52 with the total amount of cases summed into each week where they occured

    Args:
        frame (pd.DataFrame): yearly cases csv that has been read by pd_reader()

    Returns:
        list: represents each week in a year
    """
    year_by_weeks = [0]*53
    for each, row in frame.iterrows():
        year_by_weeks[int(row['Week Reported'])-1] += row['Positive Cases']
    return year_by_weeks

def data_frame_maker(weeks: list, cases: list) -> pd.DataFrame:
    """Creates a dataframe using the weeks and cases lists

    Args:
        weeks (list): all 53 possible weeks in a year
        cases (list): number of cases that occured in each week, should have the case num in the correct index

    Returns:
        pd.DataFrame: dataframe with the weeks and cases
    """
    builtDF = pd.DataFrame({'Week Reported': weeks, 'Positive Cases': cases})
    return builtDF

def new_file_maker(df: pd.DataFrame, name: str) -> None:
    """Makes a new file using a given dataframe and names the files
    Args:
        df (pd.DataFrame):given dataframe that gets turned into a csv!
        name (str): name that its going to get saved under + "SortedByWeek.csv"
    """
    df.to_csv("SortedByWeek/"+name+"SortedByWeek.csv", index=False)
    return

def main(file: str) -> None:
    """Main function that does everything by sequentially calling the other functions. Needs a csv file to read.

    Args:
        file (str): file name without the .csv extension
    """
    numbered_weeks:list = list(range(1,54)) # Starting at 1 and needing to go up to 53 because it doesn't include the last num
    df_first: pd.DataFrame = pd_reader(file + ".csv")
    cases: list = sorter(df_first)
    final_frame: pd.DataFrame = data_frame_maker(numbered_weeks, cases)
    new_file_maker(final_frame, file)
    return

def repeater() -> None:
    """Repeats the main function for all the years in the targets list
    """
    targets:list[str] = ['2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016']
    for i in targets:
        main(i)
    return 

if __name__ == "__main__":
    repeater()
    print('done')
    