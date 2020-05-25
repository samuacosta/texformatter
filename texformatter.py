import argparse


def main():
    '''Main method'''
    try:
        args = read_parameters()
        char_dict = read_dict("sample_dict_doc.tsv")
        with open(args.input) as inputfile:
            contents = inputfile.read()
            output_filename = args.input.replace(".bib", "_formatted.bib")
            with open(output_filename, 'w') as outputfile:
                for key, value in char_dict.items():
                    value = value.strip("\n")
                    print("Replacing " + key + " with " + value)
                    contents = contents.replace(key, value)
                outputfile.write(contents)
        print("Finished succesfully.")
    except Exception as exception:
        print("Error:")
        print(exception)
        raise


def read_parameters():
    parser = argparse.ArgumentParser()
    #parser.add_argument("-i", "--input", default="main.tex")
    parser.add_argument("-i", "--input", default="ref.bib")
    return(parser.parse_args())


def read_dict(dict_filename):
    char_dict = {}
    with open(dict_filename) as file:
        for line in file:
            (key, value) = line.split("\t")
            char_dict[key] = value
    return char_dict


if __name__ == "__main__":
    main()
