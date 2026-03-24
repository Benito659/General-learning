# Practicing regular expressions: re.split() and re.findall()
Now you'll get a chance to write some regular expressions to match digits, strings and non-alphanumeric characters.

- Split my_string on each sentence ending. To do this:
    - Write a pattern called sentence_endings to match sentence endings (.?!).
    - Use re.split() to split my_string on the pattern and print the result.

- Find and print all capitalized words in my_string by writing a pattern called capitalized_words and using re.findall().
    - Remember the [a-z] pattern shown in the video to match lowercase groups? Modify that pattern appropriately in order to match uppercase groups.

- Write a pattern called spaces to match one or more spaces ("\s+") and then use re.split() to split my_string on this pattern, keeping all punctuation intact. Print the result.
- Find all digits in my_string by writing a pattern called digits ("\d+") and using re.findall(). Print the result.