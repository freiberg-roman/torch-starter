import argparse
import fileinput
import os


def rename_src_directory(package_name):
    if os.path.exists("src") and os.path.isdir("src"):
        os.rename("src", package_name)
    else:
        print("Directory 'src' not found. Make sure you are in the correct directory.")


def replace_in_python_files(package_name):
    for root, _, files in os.walk("."):
        for file in files:
            if file.endswith(".py"):
                filepath = os.path.join(root, file)
                with fileinput.FileInput(filepath, inplace=True, backup=".bak") as file:
                    for line in file:
                        print(line.replace("from src.", f"from {package_name}."), end="")


def replace_package_name_placeholder(package_name):
    for root, _, files in os.walk("."):
        for file in files:
            if not file.endswith(".py") and not file.endswith(
                ".bak"
            ):  # Avoid Python and backup files
                filepath = os.path.join(root, file)
                with fileinput.FileInput(filepath, inplace=True, backup=".bak") as file:
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

    rename_src_directory(package_name)
    replace_in_python_files(package_name)
    replace_package_name_placeholder(package_name)
    print(f"Project configured with package name '{package_name}'")


if __name__ == "__main__":
    main()
