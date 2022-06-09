import webbrowser
import sys
from pathlib import Path


def get_quiz_path():
    """
    Allows the user to enter a path to their quiz and returns it. Otherwise,
    returns `quiz.txt` in the current directory as the `quiz_path
    """

    quiz_path = Path("quiz.txt")

    if len(sys.argv) > 1:
        quiz_path = Path(sys.argv[1])

    return quiz_path


def build_sanitized_quiz(quiz_path):
    """
    Applies HTML escaping to <> characters and replaces any newlines in
    <multiline-code> tags with <br> tags. Also turns <multiline-code> tags
    into <code> tags.
    """
    lines = []
    with open(quiz_path, mode="rt", encoding="utf-8") as quiz_file:
        lines = quiz_file.readlines()

    sanitized_quiz_lines = []
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

        if line.startswith("Q|") or line.startswith("AC|") or line.startswith("A|"):
            line = strip_space(line)

        sanitized_quiz_lines.append(line)

    with open("sanitized-quiz.txt", mode="wt", encoding="utf-8") as sanitized_file:
        sanitized_file.writelines(sanitized_quiz_lines)

    return sanitized_quiz_lines


def build_quiz_viewer(sanitized_quiz_lines):
    """
    Writes the `sanitized_quiz_lines` into `quiz-viewer.html` so that users can
    double-check that the sanitization process went smoothly.
    """
    lines = []
    with open(
        "quiz-viewer-template.html", mode="rt", encoding="utf-8"
    ) as quiz_viewer_template_file:
        lines = quiz_viewer_template_file.readlines()

    html_lines = []
    for line in lines:
        if "<pre>" in line:
            line += "".join(sanitized_quiz_lines)

        html_lines.append(line)

    with open("quiz-viewer.html", mode="wt", encoding="utf-8") as quiz_viewer_file:
        quiz_viewer_file.writelines(html_lines)


def strip_space(line):
    bar_index = line.index("|")
    for i, char in enumerate(line[bar_index+1:]):
        if not char.isspace():
            break
    line = line[:bar_index+1] + line[i+bar_index+1:]
    return line


if __name__ == "__main__":
    quiz_path = get_quiz_path()
    sanitized_quiz_lines = build_sanitized_quiz(quiz_path)
    build_quiz_viewer(sanitized_quiz_lines)
    # Convenience to double-check that the quiz looks correct.
    webbrowser.open("quiz-viewer.html")
