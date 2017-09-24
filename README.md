# calendar-maker
module that can transform .txt files to .csv or .ics(ical) calendars

## Table of Contents
1. [Requirements](#requirements)
2. [Install & Run](#install-&-run)
3. [Project Structure](#project-structure)
4. [Docs](#docs)
5. [License](license)

## Requirements
* python `3.0+`
* pip `9.0+`

## Install & Run

To install packages run:
```sh
$ pip install abc json re os json csv datetime
$ python main.py
```

## Project Structure

```
.
├── results                         # .ics and .csv files
├── source                          # .txt source files
└── main.py                         # file with method implementation
```
## Docs

There are some docs how to write [icalc](https://tools.ietf.org/html/rfc5545) files.

After you've jenerated .ics or .csv file use [theese](https://support.google.com/calendar/answer/37118) instructions to sync new calendar with gmail account

## Examples Of Use

There are some examples of implementation:

1. prepate `input.txt` file with data in this format:
```
name;date
Петя;01.05
Вася;02.05
```
2. save it as [Unicode](https://en.wikipedia.org/wiki/Unicode) plain text in the source directory.

3. Add this code to main.py
```python
page = Page('family.txt')
page.read();
page.save(type='csv');
page.save(type='ics');
```
4. run in the command line 
```sh
$ python main.py
```
5. browse results directory
## License

MIT
