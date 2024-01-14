import argparse
import fileinput
import os


def replace_in_python_files(src_dir, package_name):
    if os.path.exists(src_dir) and os.path.isdir(src_dir):
        for file in os.listdir(src_dir):
            if file.endswith(".py"):
                filepath = os.path.join(src_dir, file)
                with fileinput.FileInput(filepath, inplace=True) as file:
                    for line in file:
                        print(line.replace("from src.", f"from {package_name}."), end="")
    else:
        print(f"Directory '{src_dir}' not found. Make sure you are in the correct directory.")


def rename_src_directory(src_dir, package_name):
    if os.path.exists(src_dir):
        os.rename(src_dir, package_name)
    else:
        print(f"Could not rename '{src_dir}' as it does not exist.")


def replace_package_name_placeholder(top_level_dir, package_name):
    for file in os.listdir(top_level_dir):
        if not file.endswith(".py") and not os.path.isdir(file):
            filepath = os.path.join(top_level_dir, file)
            with fileinput.FileInput(filepath, inplace=True) as file:
                for line in file:
                    print(line.replace("{{package_name}}", package_name), end="")


def main():
    parser = argparse.ArgumentParser(description="Configure PyTorch Project")
    parser.add_argument("-n", "--name", type=str, help="Package name")
    args = parser.parse_args()

    if args.name:
        package_name = args.name
    else:
        package_name = input("Enter the package name: ")

    top_level_dir = "."
    src_dir = "src"

    replace_in_python_files(src_dir, package_name)
    rename_src_directory(src_dir, package_name)
    replace_package_name_placeholder(top_level_dir, package_name)
    print(f"Project configured with package name '{package_name}'")


if __name__ == "__main__":
    main()
