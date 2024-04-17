import io

def last_lines(filename, buffer_size=io.DEFAULT_BUFFER_SIZE):
    with open(filename, 'rb') as file:
        file.seek(0, io.SEEK_END)
        end_position = file.tell()
        buffer = bytearray()
        position = end_position

        while position > 0:
            size_to_read = min(buffer_size, position)
            file.seek(position - size_to_read, io.SEEK_SET)
            buffer.extend(file.read(size_to_read))

            while buffer:
                try:
                    newline_index = buffer.rindex(b'\n', 0, len(buffer) - 1)
                    line = buffer[newline_index+1:].decode('utf-8')
                    yield line
                    buffer = buffer[:newline_index]
                except ValueError:
                    position -= size_to_read
                    break

            if position == 0 and buffer:
                yield buffer.decode('utf-8')