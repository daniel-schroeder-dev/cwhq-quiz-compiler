import webbrowser

lines = []
with open("quiz.txt", mode="rt", encoding="utf-8") as quiz_file:
    lines = quiz_file.readlines()


sanitized_lines = []
multiline_mode = False
for line in lines:
    if "<" in line or ">" in line:
        line = line.replace("<", "&lt;").replace(">", "&gt;")

    if "&lt;multiline-code&gt;" in line:
        multiline_mode = True
        line = line.replace("&lt;multiline-code&gt;", "<code>")

    if "&lt;/multiline-code&gt;" in line:
        multiline_mode = False
        line = line.replace("&lt;/multiline-code&gt;", "</code>")

    if multiline_mode:
        line = line.replace("\n", "<br>")

    sanitized_lines.append(line)


with open("sanitized-quiz.txt", mode="wt", encoding="utf-8") as sanitized_file:
    sanitized_file.writelines(sanitized_lines)


lines = []
with open("quiz-template.html", mode="rt", encoding="utf-8") as quiz_template_file:
    lines = quiz_template_file.readlines()


html_lines = []
for line in lines:
    if "<pre>" in line:
        line += "".join(sanitized_lines)

    html_lines.append(line)


with open("quiz-viewer.html", mode="wt", encoding="utf-8") as quiz_viewer_file:
    quiz_viewer_file.writelines(html_lines)


webbrowser.open("quiz-viewer.html")
