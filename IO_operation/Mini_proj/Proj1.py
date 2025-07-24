def decode_secret_message(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()

    # Calculate meeting time
    line_count = len(lines)
    time = line_count if line_count <= 12 else line_count - 12
    meridian = "AM" if line_count <= 12 else "PM"

    # Count word frequencies
    word_count = {}
    for line in lines:
        for word in line.strip().split():
            word = word.strip('.,!?').capitalize()
            word_count[word] = word_count.get(word, 0) + 1

    # Find most frequent word
    meeting_place_word = max(word_count, key=word_count.get)
    meeting_place = f"{meeting_place_word} Street"

    # Final message
    print(f"Meeting Time: {time} {meridian}")
    print(f"Meeting Place: {meeting_place}")