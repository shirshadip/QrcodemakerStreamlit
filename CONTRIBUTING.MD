# Contributing to QR code maker streamlit

Thanks for taking the time to contribute! Whether it's fixing a bug, suggesting a feature, or improving the docs — all contributions are welcome.

---

## Table of Contents

- [Getting Started](#getting-started)
- [Development Setup](#development-setup)
- [How to Contribute](#how-to-contribute)
  - [Reporting Bugs](#reporting-bugs)
  - [Suggesting Features](#suggesting-features)
  - [Submitting a Pull Request](#submitting-a-pull-request)
- [Adding a New QR Code Type](#adding-a-new-qr-code-type)
- [Code Style](#code-style)
- [Commit Message Guidelines](#commit-message-guidelines)

---

## Getting Started

1. **Fork** the repository on GitHub
2. **Clone** your fork locally:
   ```bash
   git clone https://github.com/your-username/qrcodemakerstreamlit.git
   cd qrcodemakerstreamlit
   ```
3. **Create a branch** for your work:
   ```bash
   git checkout -b feature/your-feature-name
   ```

---

## Development Setup

```bash
# Install dependencies
pip install streamlit "qrcode[pil]" Pillow

# Run the app locally
streamlit run app.py
```

---

## How to Contribute

### Reporting Bugs

If you find a bug, please [open an issue](https://github.com/yourusername/qr-forge/issues) and include:

- A clear, descriptive title
- Steps to reproduce the problem
- What you expected to happen vs. what actually happened
- Your Python version and OS

### Suggesting Features

Have an idea? Open an issue with the `enhancement` label. Describe:

- What the feature does
- Why it would be useful
- Any relevant QR code standards or protocols it uses

### Submitting a Pull Request

1. Make sure your branch is up to date with `main`:
   ```bash
   git fetch origin
   git rebase origin/main
   ```
2. Write clear, focused commits (see [Commit Message Guidelines](#commit-message-guidelines))
3. Push your branch and open a Pull Request against `main`
4. Fill in the PR description — what changed and why
5. Wait for a review; be open to feedback and requested changes

---

## Adding a New QR Code Type

New QR types are the most common contribution. Here's the pattern to follow:

**1. Add the generator function to `qr_functions.py`:**

```python
def my_new_qr_code(param1, param2):
    data = f"some-protocol:{param1}?option={param2}"
    return generate_qr(data)
```

**2. Wire it up in `main.py`:**

Add a new option to the QR type selector and a matching input form, then call your function and display the result.

**3. Document it in `README.md`:**

Add a row to the Features table and a section under Module Reference with the function signature, a usage example, and any gotchas.

**Checklist before opening a PR for a new QR type:**

- [ ] Function lives in `qr_functions.py` and follows the `-> bytes` return convention
- [ ] All parameters have sensible defaults where appropriate
- [ ] The Streamlit UI handles empty/invalid inputs gracefully
- [ ] README is updated

---

## Code Style

- Follow [PEP 8](https://peps.python.org/pep-0008/)
- Use descriptive variable names — avoid single-letter names outside of loops
- Keep functions small and single-purpose
- Add a brief docstring to any new function:
  ```python
  def my_qr_code(param):
      """Generate a QR code for <use case>. Returns PNG bytes."""
      ...
  ```

---

## Commit Message Guidelines

Use short, imperative-mood messages:

```
Add SMS QR code generator
Fix UPI link missing currency field
Update README with Wi-Fi security options
```

For larger changes, add a body:

```
Add email QR code generator

Implements mailto: URI scheme with subject and body support.
Handles URL encoding for special characters in the message body.
```

---

By contributing, you agree that your contributions will be licensed under the same [MIT License](LICENSE) as this project.