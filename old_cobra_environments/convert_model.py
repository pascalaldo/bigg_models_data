import sys
from pathlib import Path


def main(in_filename, out_filename):
    in_filename = Path(in_filename)
    out_filename = Path(out_filename)
    suffix = in_filename.suffix
    if suffix == ".mat":
        convert_mat(in_filename, out_filename)
    elif suffix == ".json":
        convert_json(in_filename, out_filename)
    elif suffix == ".yaml" or suffix == ".yml":
        convert_yaml(in_filename, out_filename)
    else:
        convert_sbml(in_filename, out_filename)


def convert_json(in_filename, out_filename):
    from cobra.io import load_json_model, save_json_model

    model = load_json_model(in_filename)
    save_json_model(model, out_filename)


def convert_yaml(in_filename, out_filename):
    from cobra.io import load_yaml_model, save_yaml_model

    model = load_yaml_model(in_filename)
    save_yaml_model(model, out_filename)


def convert_sbml(in_filename, out_filename):
    from cobra.io import read_sbml_model, write_sbml_model

    model = read_sbml_model(in_filename)
    write_sbml_model(model, out_filename)


def convert_mat(in_filename, out_filename):
    from cobra.io import load_matlab_model, save_matlab_model

    model = load_matlab_model(in_filename)
    save_matlab_model(model, out_filename)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
