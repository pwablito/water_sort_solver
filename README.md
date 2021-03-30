# Solver for iOS Water Sort Puzzle game

You can find the game [here](https://apps.apple.com/us/app/water-sort-puzzle/id1514542157)

## Usage:
```
usage: Solver for the WaterSortPuzzle iOS app
       [-h] -i INPUT_FILE [-v]

optional arguments:
  -h, --help      show this help
                  message and exit
  -i INPUT_FILE, --input-file INPUT_FILE
                  File name to read
                  puzzle from
  -v, --vertical  Input file tubes are
                  vertical
```

## Example runs:
### Vertical:
You can test the vertical example file with the following:
`./main.py -v -i vertical_example.txt`
### Horizontal:
You can test the vertical example file with the following:
`./main.py -i horizontal_example.txt`

## Input files:
The following puzzle can be represented by both horizontal and vertical input files:

![Example input file](example_input.jpg)

`vertical_example.txt` is an example of a vertical input file

`horizontal_example.txt` is an example of a horizontal input file
