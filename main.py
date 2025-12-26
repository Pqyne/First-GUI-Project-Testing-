import time


def count_words(text):
    words = text.split()
    words_Count = len(words)
    return words_Count


def count_chars(text):
    counter = 0
    for i in text:
        if i != " ":
            counter += 1
    return counter

def main():
    is_running = True
    while is_running:

        start_time = time.time()
        text = input("input a secntence: ")
        end_time = time.time()
        input_time = end_time - start_time

        if text.lower() == "quit":
            print("bye!!")
            break
        final_word_count = count_words(text)
        final_chars_count = count_chars(text)
        wpm = final_word_count / (input_time / 60)
        result = f"Words: {final_word_count}, Chars: {final_chars_count}, Time: {input_time:.2f} WPM: {wpm:.2f}s\n"
        with open("PG1.txt", "a", encoding="UTF-8") as file:
            file.write(result)

        print(f"Result saved! {result}")


if __name__ == '__main__':
    main()
