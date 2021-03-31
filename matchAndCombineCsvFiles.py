#! python3
import pandas as pd
import os
import sys


def runHelp():
    print(
        "Usage program: python3 matchAndCombineCsvFiles.py [filePath or cwd (current working directory)] [incidents filename] [incidents columnName] [assets filename] [assets columnname]")


def main():
    argLen = len(sys.argv)  # length of the arguments

    # check if length of the arguments is 2 and the second index is help
    if(argLen == 2 and sys.argv[1] == "help"):
        runHelp()  # runs the help command
        sys.exit()  # exits the program

    if(argLen == 1 or argLen < 6):  # check what the length is 1 or less than 6
        runHelp()
        os.sys.exit("ERROR: not enough arguments")
    else:  # runs the main
        del os.sys.argv[0]
        sourceDir, filePath1, column1, filePath2, column2 = os.sys.argv
        if(sourceDir == "cwd"):
            sourceDir = os.getcwd()
        if(os.path.exists(sourceDir) != True):
            os.sys.exit("ERROR: Path doesn't exists")
        filePath1 = os.path.join(sourceDir, filePath1)
        if os.path.exists(filePath1) != True:
            os.sys.exit("ERROR: First file doesn't exists")
        filePath2 = os.path.join(sourceDir, filePath2)
        if os.path.exists(filePath1) != True:
            os.sys.exit("ERROR: First file doesn't exists")
        df = pd.read_csv(filePath1)
        df1 = pd.read_csv(filePath2)
        columns = [*df.columns, *df1.columns]
        newDf = pd.DataFrame(columns=columns)
        try:
            toolbar_width = df.size
            sys.stdout.write("[%s]" % (" " * toolbar_width))
            # return to start of line, after '['
            sys.stdout.write("\b" * (toolbar_width+1))
            for index, row in df.iterrows():
                addEmpty = True
                for index1, row1 in df1.iterrows():
                    if str(row[column1]).lower() == str(row1[column2]).lower():  # check
                        s = pd.Series(data=[*row, *row1],
                                      index=columns)  # combines the two rows from both csv-file together
                        addEmpty = False  # lets the program know no empty row needs to be added
                        # adds the row to the new csv
                        newDf = newDf.append(s, ignore_index=True)
                        continue
                if addEmpty == True:
                    # calculates how many empty columns needed to add
                    toAddLen = len(columns) - len(row)
                    newRow = []  # the empty list for all the empty columns
                    for x in range(toAddLen):  # for loop until x is toAddLen
                        newRow.append("")  # appends
                    s = pd.Series(
                        data=[*row, *newRow],
                        index=columns)
                    newDf = newDf.append(s, ignore_index=True)
                sys.stdout.write("-")
                sys.stdout.flush()
            sys.stdout.write("]\n")  # this ends the progress bar
            newDf.to_csv(os.path.join(sourceDir, "out.csv"))
        except KeyboardInterrupt:  # run this when there was a keyboard interupt
            # generates a out.csv when keyboardInterrupt
            newDf.to_csv(os.path.join(sourceDir, "out.csv"))


if __name__ == "__main__":
    main()
