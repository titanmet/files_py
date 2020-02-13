def write_to_file(data, content, mode='w'):
    with open(data, mode=mode) as f:
        return f.write(content)


def read_to_file(data):
    with open(data) as f:
        return f.read()


if __name__ == '__main__':
    write_to_file('dz.txt', 'Hi, whats\'ap ?')
    print(read_to_file('dz.txt'))
