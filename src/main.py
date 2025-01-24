import os
import glob
import argparse
from typing import Optional
from datetime import datetime

import fitz


CURRENT_TIME = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")


def get_output_name_for_file(file_path: str, add_timestamp: bool = True) -> str:
    file_name = os.path.basename(file_path)
    return f"{file_name if not add_timestamp else f'{CURRENT_TIME}_{file_name}'}"


def add_invisible_text(
    pdf_path: str,
    output_path: str,
    text_to_insert: str,
    x: int = 0, y: int = 0,
    *,
    on_top: bool = False,
    rotate: Optional[int] = None,
    invisible_text: bool = False,
) -> None:

    doc = fitz.open(pdf_path)
    page = doc[0]
    text_color = (1, 1, 1, 0)
    opacity = 0 if invisible_text else 1
    
    page.insert_text(
        (x, y),
        text_to_insert,
        fontsize=1,
        color=text_color,
        overlay=on_top,
        stroke_opacity=opacity,
        fill_opacity=opacity,
        rotate=rotate,
    )

    doc.save(output_path)
    doc.close()


def process_single_file(
    file_path: str,
    output_name: Optional[str] = None,
    output_prefix_dir: Optional[str] = None,
    **kwargs
) -> None:

    if not os.path.isfile(file_path):
        print(f"Input '{file_path}' is not file")
        exit()
    
    output_path = os.path.abspath(
        get_output_name_for_file(file_path, add_timestamp=True)
        if output_name is None else output_name
    )
    if output_prefix_dir is not None:
        output_path = os.path.join(output_prefix_dir, output_path)

    if os.path.isfile(output_path):
        answer = input(f"Output file '{output_path}' is already exist. Do you want to overwrite? (yes/[no]): ")
        if answer not in ("y", "yes", "Yes"):
            print("Abort")
            exit()
        os.remove(output_path)
    
    add_invisible_text(file_path, output_path, **kwargs)


def process_files_in_dir(
    input_prefix_dir: Optional[str] = None,
    output_prefix_dir: Optional[str] = None,
    **kwargs
) -> None:
    for file_path in glob.glob(os.path.join(input_prefix_dir, "*.pdf")):
        print(f"Found {file_path}...", end=" ")
        process_single_file(file_path, output_prefix_dir=output_prefix_dir, **kwargs)
        print("Processed")


def main():
    parser = argparse.ArgumentParser(description="Make sure ATS can accurately extract text from your resume by adding the full text in an invisible layer")
    parser.add_argument("--input", "-i", type=str, help="Path to target PDF")
    parser.add_argument("--input-dir", "-d", type=str, help="Process every PDF file in the provided directory", default=None)
    parser.add_argument("--text", "-t", type=str, help="Text to insert")
    parser.add_argument("--text-file", "-f", type=str, help="Get the text to insert from a file(.txt)")
    parser.add_argument("--out", "-o", type=str, help="Name of output file. If not set, '{datetime}_{input}' pattern will be used", default=None)
    parser.add_argument("--outdir", type=str, help="Place the output file in a custom directory, following the naming convention '{datetime}_{input}'", default=None)
    parser.add_argument("--on-top", action="store_true", help="If not set, an attempt will be made to insert text onto the background", default=False)
    parser.add_argument("--rotate-text", "-r", type=int, help="(Not recommended) Rotate text[0..360]", default=0)
    parser.add_argument("--invisible-text",  action="store_true", help="(Not recommended) Make text opacity equal to zero", default=False)

    args = parser.parse_args()

    # check that at least one atlternative was passed
    for attrs_pair in (
        ("input", "input_dir"),
        ("text", "text_file"),
    ):
        if all(getattr(args, attr, None) is None for attr in attrs_pair):
            print(f"\nYou must specify at least one of '{attrs_pair[0]}' or '{attrs_pair[1]}'\n")
            exit()

    actual_text = args.text
    if args.text_file is not None:
        if not os.path.isdir(args.input_dir):
            print(f"'{args.text_file}' (text_file) is not found")
            exit()
        with open(args.text_file, "r", encoding="utf-8") as file:
            actual_text = file.read()

    output_prefix_dir = args.outdir
    if output_prefix_dir is not None:
        os.makedirs(output_prefix_dir, exist_ok=True)
    
    arguments = {
        **{
            k: v
            for k, v in (("on_top", args.on_top), ("rotate", args.rotate_text), ("invisible_text", args.invisible_text),)
            if v is not None
        },
        "text_to_insert": actual_text
    }

    if args.input_dir is not None:
        if not os.path.isdir(args.input_dir):
            print(f"'{args.input_dir}' directory is not found")
            exit()
        process_files_in_dir(args.input_dir, output_prefix_dir, **arguments)
    
    else:
        process_single_file(args.input, args.out, output_prefix_dir, **arguments)


if __name__ == '__main__':
    main()
