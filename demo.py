# Demo
# This demo shows how to deidentify a toy dataset using Deidentifier
import time
import Deidentifier
def main():
    '''
    Deidentify the toy dataset "mabaoguo"
    '''
    inputFolder = "dataset/mabaoguo"
    outputFolder = "dataset/mabaoguo_deidentified"
    scriptFile = "mabaoguo.script"

    print("Deidentify the dataset")
    print("Original Dataset: {}".format(inputFolder))
    print("Deidentified Dataset: {}".format(outputFolder))

    tic = time.time()
    deidentifier = Deidentifier.DatasetDeidentifier(inputFolder,
                                                    outputFolder,
                                                    scriptFile)
    deidentifier.deidentifyDataset()
    toc = time.time()
    print("Time Elapsed {0} seconds".format(toc - tic))
if __name__ == "__main__":
    main()