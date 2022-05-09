from subprocess import call


def main(file_name: str):
    call(
        [
            "python", "-m", "nbconvert",
            file_name,"--to","pdf"
        ]
    )


if __name__ == "__main__":
    main("investigate-dataset.ipynb")
