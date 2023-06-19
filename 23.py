def delete_html_tags(html_file, result_file='cleaned.txt'):
    with open(html_file, 'r', encoding='utf-8') as f:
        html = f.read()

    cleaned_text = ''
    tag_open = False

    for char in html:
        if char == '<':
            tag_open = True
        elif char == '>':
            tag_open = False
        elif not tag_open:
            cleaned_text += char

    with open(result_file, 'w', encoding='utf-8') as f:
        f.write(cleaned_text)
        