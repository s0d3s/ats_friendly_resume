
<div>  
  <div>
    <img align="right" src="https://img.shields.io/badge/-2025_Jan_--_Until_Now-blue?style=for-the-badge&color=black">
  </div>
  <h2 align="left">⌇ Your Incredible Employee </h2>
</div>
<div align="center">

He is optimizing his resume using `ats_friendly_resume` to pass through ATS and get an interview

Why you shouldn`t?

![PyPI - Downloads](https://img.shields.io/pypi/dm/ats-friendly-resume)
![GitHub last commit](https://img.shields.io/github/last-commit/s0d3s/ats_friendly_resume)
[![PyPI - Version](https://img.shields.io/pypi/v/ats-friendly-resume?link=https%3A%2F%2Fpypi.org%2Fproject%2Fats-friendly-resume%2F)](https://pypi.org/project/ats-friendly-resume/)

</div>

## About

> In short: Insert invisible text into your PDF for better matching with automated filtering systems

Applicant Tracking Systems(ATS) are trying to parse your resume to get data for further analysis. Most popular format to apply the vacancy is PDF.
But when you finish writing your resume, it might turn out that ATS cannot properly extract the text, and your resume simply fails the filtering process.
This might happen for the following reasons:  
- You created a visually appealing, custom-designed resume, but unfortunately, issues with text layers occurred after conversion.  
- You decided to rasterize all text layers, making it impossible to extract text except by using OCR.  
- Other design choices that result in problems with text conversion.

To eliminate any issues with text recognition, you simply need to add text that will be correctly extracted. This is exactly what this small application is designed to do.

## ⚒ How to
1. Install `ats_friendly_resume`
    - via pip
     
     ```bash
     pip install ats-friendly-resume
     ```
     > The actual executable name will be `ats_friendly_resume`
2. Prepare:
    - Your PDF to past text into it(`resume.pdf`, for this example)
    - Full text which you want to insert(`resume.txt`, for this example)
3. Run `ats_friendly_resume`(simplest example):
   ```bash
   ats_friendly_resume --input="/path/to/resume.pdf" --text-file="/path/to/resume.txt"
   ```
4. Thats all! Get your optimized resume and apply it!

> (in this case resume will be in the same folder as input, and name also like input but with timestamp prefix)

## 🚧 CLI Usage
```
usage: ats_friendly_resume  [-h] [--input INPUT] [--input-dir INPUT_DIR] [--text TEXT] [--text-file TEXT_FILE] [--out OUT] 
                            [--outdir OUTDIR] [--on-top] [--rotate-text ROTATE_TEXT] [--invisible-text]

Make sure ATS can accurately extract text from your resume by adding the full text in an invisible layer

optional arguments:
  -h, --help            show this help message and exit
  --input INPUT, -i INPUT
                        Path to target PDF
  --input-dir INPUT_DIR, -d INPUT_DIR
                        Process every PDF file in the provided directory
  --text TEXT, -t TEXT  Text to insert
  --text-file TEXT_FILE, -f TEXT_FILE
                        Get the text to insert from a file(.txt)
  --out OUT, -o OUT     Name of output file. If not set, '{datetime}_{input}' pattern will be used
  --outdir OUTDIR       Place the output file in a custom directory, following the naming convention '{datetime}_{input}'
  --on-top              If not set, an attempt will be made to insert text onto the background
  --rotate-text ROTATE_TEXT, -r ROTATE_TEXT
                        (Not recommended) Rotate text[0..360]
  --invisible-text      (Not recommended) Make text opacity equal to zero
```