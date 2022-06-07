# Quiz Compiler

Quiz Compiler is a Python script that takes a quiz from a human-readable format and converts it into CWHQ's quiz format.

## Usage

Clone this repo to your machine and add the contents of your quiz into `quiz.txt`.

You can then run the script like so:

```bash
python main.py
```

If you'd rather provide the path to the quiz you'd like to sanitize as a command line argument, you can do so like so:

```bash
python main.py path/to/my/quiz.txt
```

Whatever method you choose for the input quiz, the sanitized quiz will be written to `sanitized-quiz.txt` and an HTML preview will open in your default web browser.

## Note

Only tested on Linux. Should work fine on OSX and Windows as well though.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](https://choosealicense.com/licenses/mit/)