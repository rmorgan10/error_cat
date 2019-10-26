# error_cat

### A fun way to display python errors.


Do you find long python error tracebacks annoying? Personally, they make me painfully aware of the fact that I don't know what I'm doing. And while that is certainly the case, sometimes I'd like that news to be delivered to me in a nicer way. For that, there is `error_cat`.

### Installation

```pip install error_cat```

### Usage

```error_cat python <name of your favorite python script>.py```

If `<name of your favorite python script>.py` runs successfully, you will see a fun, reassuring message from `error_cat`:

```
                ________________________
               /                        \
               |   Everything worked!   |
               \  ______________________/
              /  /
 ,_     _    / /
 |\\_,-~/   /'
 / _  _ |    ,--.
(  @  @ )   / ,-'
 \  _T_/-._( (
 /         `. \
|         _  \ |
 \ \ ,  /      |
  || |-_\__   /
 ((_/`(____,-'

```

On the other hand, if `<name of your favorite python script>.py` produces an error, `error_cat` will break the news to you. Here is an example script that will lead to an error:

`fake_error.py`

```python
def func():
	func2()
	
def func2():
	print(5 + "5")
	
func()
```

Here is what `error_cat` will tell you:

```
$ error_cat python fake_error.py

                _________________________________________________________________
               /                                                                 \
               |   File "fake_error.py", line 5, in func2                        |
               |   TypeError: unsupported operand types for +: 'int' and 'str'   |
               \  _______________________________________________________________/
              /  /
 ,_     _    / /
 |\\_,-~/   /'
 / _  _ |    ,--.
(  @  @ )   / ,-'
 \  _T_/-._( (
 /         `. \
|         _  \ |
 \ \ ,  /      |
  || |-_\__   /
 ((_/`(____,-'
 ```
 
## Artwork Credit
 
All ascii artwork is from the [ASCII Art Archive](https://www.asciiart.eu/). Individual artworks are credited to the artist (if known) in the comments of `error_cat/characters.py`. A big thank you to the following artists whose art has been incorporated into `error_cat`:

- Morfina
- Joan G. Stark 