import re

def format_reference(ref):
    ref = ref.strip()

    doi_match = re.search(r'(10\.\d{4,9}/[-._;()/:A-Z0-9]+)', ref, re.I)
    doi = doi_match.group(1) if doi_match else None

    url_match = re.search(r'(https?://[^\s]+)', ref)
    url = url_match.group(1) if url_match else None

    # Journal Article
    journal_match = re.search(r'^(.*?)\.\s*\((\d{4})\)\.\s*(.*?)\.\s*(.*?),\s*(\d+)\((\d+)\),\s*([\d–\-]+)', ref)
    if journal_match:
        authors = journal_match.group(1)
        year = journal_match.group(2)
        title = journal_match.group(3)
        journal = journal_match.group(4)
        volume = journal_match.group(5)
        issue = journal_match.group(6)
        pages = journal_match.group(7)
        out = f"{authors} ({year}). {title}. *{journal}*, *{volume}*({issue}), {pages}."
        if doi:
            out += f" https://doi.org/{doi}"
        elif url:
            out += f" {url}"
        return out

    # Book
    book_match = re.search(r'^(.*?)\.\s*\((\d{4})\)\.\s*(.*?)\.\s*(.*?)\.', ref)
    if book_match and not url:
        authors = book_match.group(1)
        year = book_match.group(2)
        title = book_match.group(3)
        publisher = book_match.group(4)
        return f"{authors} ({year}). *{title}*. {publisher}."

    # Website
    website_match = re.search(r'^(.*?)\.\s*\((\d{4})\)\.\s*(.*?)\.\s*(.*?)\.\s*(https?://[^\s]+)', ref)
    if website_match:
        authors = website_match.group(1)
        year = website_match.group(2)
        title = website_match.group(3)
        site = website_match.group(4)
        link = website_match.group(5)
        return f"{authors} ({year}). {title}. *{site}*. {link}"

    # Fallback
    return f"[Could not parse] {ref}"

def format_all_references():
    print("📥 Paste your references below (one per line).")
    print("🔚 Type 'END' when you're done.\n")
    lines = []
    while True:
        line = input()
        if line.strip().upper() == 'END':
            break
        lines.append(line)
    
    print("\n📘 APA 7 Formatted References:\n")
    for ref in lines:
        if ref.strip():
            print(format_reference(ref))
            print()

# Run the formatter
if __name__ == "__main__":
    format_all_references()

