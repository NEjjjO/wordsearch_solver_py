import csv
import argparse
from termcolor import colored


class Puzzle:
    def __init__(self, args):
        self.puzzle = self.parse_puzzle(args.puzzle)
        self.words = self.parse_words(args.words)
        self.solved = []
        self.words_found = 0  # Initialize a word count

    def replace_word_with_hyphens(self, word):
        for ri, row in enumerate(self.puzzle):
            row_str = str(row[0])
            if word in row_str:
                start_idx = row_str.find(word)
                end_idx = start_idx + len(word)
                new_row = row_str[:start_idx] + '-' * len(word) + row_str[end_idx:]
                self.puzzle[ri][0] = new_row


    def parse_puzzle(self, puzzle_file=None):
        if puzzle_file is None:
            puzzle_file = 'puzzle.csv'
        puzzle = []
        with open(puzzle_file, 'r') as pfile:
            p_reader = csv.reader(pfile)
            for p_row in p_reader:
                puzzle.append(p_row)
        return puzzle

    def parse_words(self, list_file=None):
        if list_file is None:
            list_file = 'list.csv'
        words = []
        with open(list_file, 'r') as cfile:
            c_reader = csv.reader(cfile)
            for c_row in c_reader:
                words.append(str(c_row[0]).replace(' ', ''))
        return words

    def output_cli(self):
        for ri, row in enumerate(self.puzzle):
            for chi, ch in enumerate(row[0]):
                if (ri, chi) in self.solved:
                    print(colored("-", "red"), end="")
                else:
                    print(colored(f"{ch}", "blue"), end="")
            print()

    ef
    find_word(self):
    found_words = []  # Create a list to store found words
    for word in self.words:
        if self.find_horizontal(word):
            self.replace_word_with_hyphens(word)
            self.words_found += 1
            found_words.append(word)  # Append found word to the list
        if self.find_vertical(word):
            self.replace_word_with_hyphens(word)
            self.words_found += 1
            found_words.append(word)
        if self.find_diagonal(word):
            self.replace_word_with_hyphens(word)
            self.words_found += 1
            found_words.append(word)

    print("Words found:")
    for word in found_words:
        print(word)


def find_horizontal(self, word):
        for ri, row in enumerate(self.puzzle):
            if word in str(row):
                for i in range(0, len(word)):
                    self.solved.append((ri, str(row).find(word) - 2 + i))
                return True
            row_r = str(row)[::-1]
            if word in row_r:
                for i in range(0, len(word)):
                    self.solved.append((ri, len(row_r) - str(row_r).find(word) - 3 - i))
                return True
        return False

    def find_vertical(self, word):
        for char in range(len(self.puzzle[0][0])):
            temp = []
            for col in range(len(self.puzzle)):
                temp.append(self.puzzle[col][0][char])
            temp = ''.join(temp)
            temp_r = temp[::-1]
            if word in str(temp):
                for i in range(0, len(word)):
                    self.solved.append((str(temp).find(word) + i, char))
                return True
            if word in str(temp_r):
                for i in range(0, len(word)):
                    self.solved.append((len(temp_r) - str(temp_r).find(word) - 1 - i, char))
                return True
        return False

    def find_diagonal(self, word):
        for a in range(0, len(self.puzzle[0][0])):
            temp = [[] for i in range(8)]
            ranges = [[] for i in range(8)]
            i = 0
            while ((a - i) >= 0) and (i < len(self.puzzle)):
                coords = [[i, a - i], [29 - i, a - i], [29 - i, 29 - (a - i)], [i, 29 - (a - i)]]
                for cx, c in enumerate(coords):
                    temp[cx].append(self.puzzle[c[0]][0][c[1]])
                    ranges[cx].append((c[0], c[1]))
                    ranges[cx + 4].append((c[1], c[0]))
                i += 1

            for ti in range(4):
                temp[ti] = ''.join(temp[ti])
                temp[ti + 4] = temp[ti][::-1]

            for tx, t in enumerate(temp):
                if word in str(t):
                    for i in range(0, len(word)):
                        self.solved.append(ranges[tx][str(t).find(word) + i])
                    return True
        return False


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--puzzle', help='puzzle file location')
    parser.add_argument('--words', help='words file location')

    args = parser.parse_args()
    p = Puzzle(args)
    print("\nPROBLEM:")
    p.output_cli()
    print("\nSOLUTION:")
    p.find_word()
    p.output_cli()
    print(f"Number of words found: {p.words_found}")

    # Write the puzzle with hyphens to a CSV file
    with open('output.csv', 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        for row in p.puzzle:
            csv_writer.writerow([row[0]])