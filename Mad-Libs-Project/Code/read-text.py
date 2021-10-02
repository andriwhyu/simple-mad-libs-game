import os
import random

# Next task: Pisahkan fungsi show dengan hitung $


def read_text():
    parent_dir = os.path.dirname(os.getcwd())

    with open(os.path.join(parent_dir, 'Resource/mad-lib-library.txt')) as f:
        lines = f.readlines()
        f.close()

    list_sentences = []

    for sentence in lines:
        if(sentence == "\n"):
            break

        sentence = sentence.strip("\n")
        list_sentences.append(sentence)

    return list_sentences


def find_blank(output_sentence):
    blank_position = []

    while output_sentence.count("$") > 0:
        pos = output_sentence.find("$")

        output_sentence = output_sentence.replace("$", "", 1)

        blank_position.append(pos)

    words = []

    for i in range(0, len(blank_position), 2):
        word = output_sentence[blank_position[i]:blank_position[i+1]]
        words.append(word)

    return output_sentence, words


def play_mad_libs(sentences):
    index = random.randint(0, len(sentences)-1)

    output_sentence = sentences[index]
    count_blank = output_sentence.count("$") // 2

    output_sentence, words = find_blank(output_sentence)

    user_inputs = []

    for i in range(count_blank):
        direction = words[i].title()
        direction = direction.replace('_', " ")

        print("{}:".format(direction), end=" ")
        user_inputs.append(input().strip())

    for i in range(count_blank):
        output_sentence = output_sentence.replace(words[i], user_inputs[i], 1)

    print("-----------------Kalimat yang anda buat-----------------")
    print(output_sentence)


if __name__ == "__main__":
    data_sentence = read_text()

    play_mad_libs(data_sentence)
