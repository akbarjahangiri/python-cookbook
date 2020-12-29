from collections import deque


def search(lines, pattern, history):
    previues_lines = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line, previues_lines
        previues_lines.append(line)


if __name__ == '__main__':
    with open("lines.txt") as f:
        for line, prevline in search(f, 'akbar', 5):
            for pline in prevline:
                print(pline, end=" ")
            print("---found result in the line => "+line, end=" ")
            print("\n"+"_____")
