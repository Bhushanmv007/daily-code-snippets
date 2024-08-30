def title_case(sentence):
    return ' '.join(word.capitalize() for word in sentence.split())

print(title_case("hello world from gpt"))  #Output:"Hello World From Gpt"
