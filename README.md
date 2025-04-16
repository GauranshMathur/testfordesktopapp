# Test for Software Dev

This repository contains two Python scripts for both assignments.

## File Structure

```tree
├── assignment1.py
├── assignment2.py
└── README.md
```

## Assignment 1: Word Reversal (`assignment1.py`)

This script reverses alphanumeric sequences ("words") within a string while keeping non-alphanumeric characters in their original positions.

### How to Run

```bash
python assignment1.py
```

> The script includes internal test cases that will be executed automatically.

Implementation Notes
<ul>
  <li>Iterates through the input string character by character</li>
  <li>Identifies contiguous sequences of alphanumeric characters</li>
  <li>Reverses only these alphanumeric sequences</li>
  <li>Rebuilds the output string with reversed words and original non-alphanumeric characters</li>
  <li>Ensures punctuation and spacing remain unchanged</li>
</ul>

## Assignment 2: Build Version Update (`assignment2.py`)

This script updates version numbers in specified source files (SConstruct and VERSION) based on environment variables.

### Seting Environment Variables:

> **BuildNum**: The new build number (e.g., export BuildNum=124).
> 
> **SourcePath**: The root path containing the target files (e.g., export SourcePath=/path/to/your/source).

### Implementation Notes

This script is designed for use in build environments. 
Key features include:
<ul>
  <li><strong>Safe File Handling:</strong> Uses <code>with open(...)</code> to ensure files are closed properly, even if errors occur.</li>
  <li><strong>Robustness:</strong> Includes checks for required environment variables and basic error handling for file operations.</li>
  <li><strong>Clarity:</strong> Uses <code>re.subn</code> to perform replacements only if the pattern is found and provides feedback via print statements.</li>
  <li><strong>Standard Practices:</strong> Avoids unnecessary actions like changing file permissions (<code>os.chmod</code>) and uses conventional temporary file names (<code>.temp</code>). The main logic is guarded by <code>if __name__ == "__main__":</code>.</li>
</ul>
