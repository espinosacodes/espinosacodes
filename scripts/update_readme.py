import datetime
import re
import math

QUOTES = [
    ("Talk is cheap. Show me the code.", "Linus Torvalds"),
    ("Any fool can write code that a computer can understand. Good programmers write code that humans can understand.", "Martin Fowler"),
    ("First, solve the problem. Then, write the code.", "John Johnson"),
    ("The best way to predict the future is to invent it.", "Alan Kay"),
    ("Simplicity is the soul of efficiency.", "Austin Freeman"),
    ("Code is like humor. When you have to explain it, it's bad.", "Cory House"),
    ("Make it work, make it right, make it fast.", "Kent Beck"),
    ("Programming isn't about what you know; it's about what you can figure out.", "Chris Pine"),
    ("The only way to learn a new programming language is by writing programs in it.", "Dennis Ritchie"),
    ("Experience is the name everyone gives to their mistakes.", "Oscar Wilde"),
    ("In order to be irreplaceable, one must always be different.", "Coco Chanel"),
    ("Java is to JavaScript what car is to carpet.", "Chris Heilmann"),
    ("Knowledge is power.", "Francis Bacon"),
    ("It's not a bug; it's an undocumented feature.", "Anonymous"),
    ("Perfection is achieved not when there is nothing more to add, but when there is nothing left to take away.", "Antoine de Saint-Exupery"),
    ("Testing leads to failure, and failure leads to understanding.", "Burt Rutan"),
    ("The most disastrous thing that you can ever learn is your first programming language.", "Alan Kay"),
    ("The function of good software is to make the complex appear to be simple.", "Grady Booch"),
    ("Before software can be reusable it first has to be usable.", "Ralph Johnson"),
    ("The best error message is the one that never shows up.", "Thomas Fuchs"),
    ("One machine can do the work of fifty ordinary men. No machine can do the work of one extraordinary man.", "Elbert Hubbard"),
    ("If debugging is the process of removing software bugs, then programming must be the process of putting them in.", "Edsger Dijkstra"),
    ("Measuring programming progress by lines of code is like measuring aircraft building progress by weight.", "Bill Gates"),
    ("Always code as if the guy who ends up maintaining your code will be a violent psychopath who knows where you live.", "John Woods"),
    ("Sometimes it pays to stay in bed on Monday, rather than spending the rest of the week debugging Monday's code.", "Dan Salomon"),
    ("Walking on water and developing software from a specification are easy if both are frozen.", "Edward V Berard"),
    ("The computer was born to solve problems that did not exist before.", "Bill Gates"),
    ("Computers are fast; developers keep them slow.", "Anonymous"),
    ("A language that doesn't affect the way you think about programming is not worth knowing.", "Alan Perlis"),
    ("The most important property of a program is whether it accomplishes the intention of its user.", "C.A.R. Hoare"),
    ("Deleted code is debugged code.", "Jeff Sickel"),
]

TIPS = [
    "Use `git stash` to save uncommitted changes before switching branches.",
    "Learn keyboard shortcuts in your IDE - it compounds over time.",
    "Write tests before you think you need them. Future you will thank you.",
    "Read the error message. Then read it again. The answer is usually there.",
    "Use `docker compose` to keep your dev environments reproducible.",
    "Profile before you optimize. Don't guess where the bottleneck is.",
    "Keep functions small and focused. If it needs a comment, it might need a refactor.",
    "Use `.env` files and never commit secrets to version control.",
    "Learn SQL well - it's one of the most transferable skills in tech.",
    "Contribute to open source. Start with documentation fixes.",
    "Use `tmux` or `screen` for persistent terminal sessions on remote servers.",
    "Master `grep`, `awk`, and `sed` - they'll save you hours.",
    "Write meaningful commit messages. Your future self is a stranger.",
    "Use type hints in Python. They catch bugs before runtime.",
    "Learn to read documentation before Stack Overflow. It's a superpower.",
    "Automate anything you do more than twice.",
    "Use `pre-commit` hooks to enforce code quality automatically.",
    "Keep your dependencies updated. Security vulnerabilities compound.",
    "Learn one new shortcut, tool, or concept every week.",
    "Take breaks. Your subconscious solves problems while you rest.",
    "Use feature flags to deploy code without releasing features.",
    "Master your debugger. `print()` debugging has its limits.",
    "Pair programming is underrated. Two minds catch more bugs.",
    "Use semantic versioning for your libraries and APIs.",
    "Write READMEs like someone else will maintain your code. Because they will.",
    "Learn vim keybindings. They work everywhere.",
    "Use `make` or `just` for project task automation.",
    "Monitor your applications in production. Logs are your eyes.",
    "Use branch protection rules. Your `main` branch is sacred.",
    "Embrace the terminal. GUIs come and go, the CLI is forever.",
    "Refactor continuously. Technical debt grows with compound interest.",
]

LANGUAGES = [
    ("Python", "3776AB"), ("TypeScript", "3178C6"), ("Rust", "000000"),
    ("Go", "00ADD8"), ("Java", "007396"), ("C++", "00599C"),
    ("Kotlin", "7F52FF"), ("Swift", "F05138"), ("Ruby", "CC342D"),
    ("Scala", "DC322F"), ("Haskell", "5D4F85"), ("Elixir", "4B275F"),
    ("Zig", "F7A41D"), ("Lua", "2C2D72"), ("Julia", "9558B2"),
]


def get_year_progress():
    now = datetime.datetime.now(datetime.timezone.utc)
    start = datetime.datetime(now.year, 1, 1, tzinfo=datetime.timezone.utc)
    end = datetime.datetime(now.year + 1, 1, 1, tzinfo=datetime.timezone.utc)
    progress = (now - start) / (end - start)
    filled = round(progress * 20)
    bar = "\u2593" * filled + "\u2591" * (20 - filled)
    return bar, progress


def get_phase_emoji(day_of_year):
    """Moon phase based on approximate lunar cycle."""
    phase = (day_of_year % 30) / 30
    if phase < 0.125:
        return "\U0001f311"
    elif phase < 0.25:
        return "\U0001f312"
    elif phase < 0.375:
        return "\U0001f313"
    elif phase < 0.5:
        return "\U0001f314"
    elif phase < 0.625:
        return "\U0001f315"
    elif phase < 0.75:
        return "\U0001f316"
    elif phase < 0.875:
        return "\U0001f317"
    else:
        return "\U0001f318"


def get_language_of_the_day(day_of_year):
    idx = day_of_year % len(LANGUAGES)
    return LANGUAGES[idx]


def build_section():
    now = datetime.datetime.now(datetime.timezone.utc)
    day_of_year = now.timetuple().tm_yday
    bar, progress = get_year_progress()
    quote_text, quote_author = QUOTES[day_of_year % len(QUOTES)]
    tip = TIPS[day_of_year % len(TIPS)]
    moon = get_phase_emoji(day_of_year)
    lang_name, lang_color = get_language_of_the_day(day_of_year)

    section = f"""### Daily Dose of Code {moon}

<div align="center">

> *"{quote_text}"*
> — **{quote_author}**

</div>

| | |
|---|---|
| **Year Progress** | `{bar}` {progress:.1%} of {now.year} |
| **Today's Tip** | {tip} |
| **Language to Explore** | ![{lang_name}](https://img.shields.io/badge/{lang_name}-{lang_color}?style=flat-square&logo={lang_name.lower()}&logoColor=white) |
| **Last Updated** | {now.strftime("%B %d, %Y %H:%M UTC")} |"""

    return section


def main():
    with open("README.md", "r") as f:
        content = f.read()

    section = build_section()

    start_marker = "<!-- DAILY-UPDATE:START -->"
    end_marker = "<!-- DAILY-UPDATE:END -->"

    if start_marker in content and end_marker in content:
        pattern = re.escape(start_marker) + r".*?" + re.escape(end_marker)
        replacement = f"{start_marker}\n{section}\n{end_marker}"
        content = re.sub(pattern, replacement, content, flags=re.DOTALL)
    else:
        # Insert before the final quote section
        insert_before = "---\n\n<div align=\"center\">\n\n  **\"Don't hurry"
        content = content.replace(
            insert_before,
            f"{start_marker}\n{section}\n{end_marker}\n\n{insert_before}",
        )

    with open("README.md", "w") as f:
        f.write(content)

    print("README updated successfully!")


if __name__ == "__main__":
    main()
