# Quiz Compiler

Quiz Compiler is a Python script that takes a quiz from a human-readable format and converts it into CWHQ's quiz format.

## Usage

Clone this repo to your machine and add the contents of your quiz into `quiz.txt`.

You can then run the quiz compiler script like so:

```bash
python main.py
```

If you'd rather provide the path to the quiz you'd like to sanitize as a command line argument, you can do so like so:

```bash
python main.py path/to/my/quiz.txt
```

Whatever method you choose for the input quiz, the sanitized quiz will be written to `sanitized-quiz.txt` and an HTML preview will open in your default web browser.

## Escaping HTML Chars

The script automatically escapes HTML characters.

So, this:

```html
Q|Which of the following elements is not on the periodic table? 
AC|All of these
A|<!DOCTYPE>
A|<title>
A|<head>
```

Will be converted to this:

```html
Q|Which of the following elements is not on the periodic table? 
AC|All of these
A|&lt;!DOCTYPE&gt;
A|&lt;title&gt;
A|&lt;head&gt;
```

## Removing Spaces After The First `|`

The script also removes any whitespace after the initial `|` in a `Q|`, `AC|`, or `A|`.

So, this:

```html
Q|   Why would we use a flogger?
AC| Give it a shmoopy.
A| Something catchy.
A|   Eat a hotdog.
A| Dunno.
```

Will be converted to this:

```html
Q|Why would we use a flogger?
AC|Give it a shmoopy.
A|Something catchy.
A|Eat a hotdog.
A|Dunno.
```

## Multiline Code Samples

If you want to write human-readable multiline code samples, use the `<multiline-code>` tag like so:

```html
Q|Which of the following creates a round thing?
A|<multiline-code>
selector {
  width: 300px;
  height: 300px;
  border-radius: 1000%;
}</multiline-code>
A|<multiline-code>
selector {
  width: 300px;
  length: 300px;
  border-radius: tom%;
}</multiline-code>
AC|<multiline-code>
selector {
  width: 300px;
  height: 300px;
  border-radius: jerrypx;
}</multiline-code>
A|<multiline-code>
selector {
  width: 300px;
  height: 300px;
  border-radius: stevepx;
}</multiline-code>
```

That will be converted to:

```html
Q|Which of the following creates a round thing?
A|<code><br>selector {<br>  width: 300px;<br>  height: 300px;<br>  border-radius: 1000%;<br>}</code>
A|<code><br>selector {<br>  width: 300px;<br>  length: 300px;<br>  border-radius: tom%;<br>}</code>
AC|<code><br>selector {<br>  width: 300px;<br>  height: 300px;<br>  border-radius: jerrypx;<br>}</code>
A|<code><br>selector {<br>  width: 300px;<br>  height: 300px;<br>  border-radius: stevepx;<br>}</code>
```




## Note

Only tested on Linux. Should work fine on OSX and Windows as well though.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](https://choosealicense.com/licenses/mit/)