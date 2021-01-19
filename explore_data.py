from dxc.ai import explore_complete_data
import pandas as pd
import webbrowser


def explore_data(df):
    report = explore_complete_data(df)
    report.to_file(output_file=r"Report.html")
    #report.to_file(output_file='report.html')
    webbrowser.open_new_tab(r"Report.html")
    return report

if __name__ == "__main__":
    df=pd.read_csv('clean_df_tmp.csv')
    explore_data(df)
    print('success')