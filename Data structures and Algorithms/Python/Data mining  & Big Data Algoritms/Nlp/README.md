# NATURAL LANGUAGE PROCESSING (NLP)
Natural language processing is field of study making sense of language by using statistics and computers.

## GUIDE
- [NLP Topics](#nlp-topics)
- [NLP Applications](#nlp-applications)
    - [Regular expressions](#regular-expression)
    - [Tokenisation](#tokenisation)

## NLP Topics 
- Regular expression
- Topics identifications
- Sentiment Analysis

## NLP Applications
- Chatbots
- Translation
- Sentiment analysis

### Regular expression
- String with a special syntax
- Allows us to match patterns in other strings
- Applications of regural expression
    - Find all web links in a document
    - Find and parse email address
    - Extract phone numbers
    - Remove / Replace unwanted character
    - validate password

- It is use in python by importing re library :
```python
    import re
    re.match("abc","abcdef")
```

- The match is between a pattern and a string.
- It take the match as the fist argument and the string as the second.
- We can use special pattern that regex understand.
- **\w** only match a character, and matches any word character
    - letters: a-z, A-Z
    - digits: 0-9
    - underscore: _
    - \w  ≈  [a-zA-Z0-9_]
    ```python 
        import re
        re.match(r"\w", "hi there!")

        output : 
        h
    ```
    - to find all charcater separatly we can use **findall**
    ```python
        re.findall(r"\w", "hi there!")

        output : 
        ['h', 'i', 't', 'h', 'e', 'r', 'e']
    ```
    - it matches each character individually
- **\w+** use to match a word 
    -  **+** is a quantifier
    - It means: "one or more" of the previous element 
    - So **\w+** means: match one or more word characters in a row
    ```python
        word_regex="\w+"
        re.match(word_regex, "hi there!")

        output:
        hi
    ```
    - **\w+** is **greedy matching** , meaning: It takes as many valid characters as possible until it can't anymore.
    - To get all words we can use findall 
    ```python
    re.findall(r"\w+", "hi there!")

    output: 
    ['hi', 'there']
    ```

- **\d** use to match digit
- **\s** use to match spaces
- **.\*** use to match any letter or symbol
    - **.** replaces any character
    ```python
        re.search("h.llo", "hello")  # matches
    ```
- **+ or \*** use to greedy match, grabing repeat or single letter
    - + (one or more) :
        - Matches at least one occurrence of the preceding pattern
        - Example:
            - Regex: a+
            - Matches: "a", "aa", "aaa"
            - Does not match an empty string
            - grab one or more of this character
    - * (zero or more) :
        - Matches zero or more occurrences of the preceding pattern.
        - Regex: a*
        - Matches: "" (empty), "a", "aa", "aaa"
        - grab as many as possible, even none
- What does “greedy” mean : Greedy matching means the regex engine will take as much as it can while still allowing the overall pattern to succeed
- Greedy vs non-greedy (quick contrast) : If you don’t want greedy behavior, you can make it lazy by adding **?**
    - a+? → matches as few as as possible
    - .*? → stops at the earliest valid match
- **\S** anything that is not a space 
- using capital letter negate them 
- **^** start of a string
    - The match must begin at the start of the string
    ```python
    import re
    re.findall(r"^hello", "hello world")

    output :
    ['hello']

    re.findall(r"^hello", "say hello")

    output :
    []
    ```
- **$** end of a string :
    - The match must be at the end of the string
    ```python
        re.findall(r"world$", "hello world")

        output :
        ['world']

        re.findall(r"world$", "world hello")
        output :
        []
    ```
- Combine **^** and **$**
    ```python
        re.findall(r"^hello$", "hello")
        output :
        ['hello']
    ```
- Multiline Mode :
    - Normally: **^** = start of whole string and **$** = end of whole string
    - With re.M (multiline) **^** works per line
    ```python
        text = """hello
        world"""

        re.findall(r"^world", text, re.M)
    ```
- Sets and Ranges
```python
    r"[abc]"      # a OR b OR c
    r"[a-z]"      # lowercase letters
    r"[A-Z]"      # uppercase letters
    r"[0-9]"      # digits
    re.findall(r"[A-Z]", "Hello World")
    # ['H', 'W']
```

- **\*** 0 or more
- **\+** 1 or more
- **?** 0 or 1 
    - **a?** a may appear zero or one time
    - it can match nothing
    - or match one a 
    ```python
        import re
        re.findall(r"a?", "aaab")

        output: 
        ['a', 'a', 'a', '', '']
    ```
- **{}** exact repetitions :
    - a{3} match exactly 3 a in a row
    ```python
        re.findall(r"a{3}", "aa aaa aaaa")

        output:
        ['aaa', 'aaa']
    ```
    - a{2,5}  match at least 2 and at most 5 a
    ```python
        re.findall(r"a{2,5}", "a aa aaa aaaa aaaaa aaaaaa")

        output: 
        ['aa', 'aaa', 'aaaa', 'aaaaa', 'aaaaa']
    ```
    - Regex is greedy by default : it takes the maximum possible match 
    "aaaaaa" → matches "aaaaa" (5, not 2)

- **[]** set of caracters
- **\\** escape character
- **[a-z]** group of caracter (lowercase group)
- **re** the module
- **split** method that split a string into regex, return list of token
- **findall** find all patterns in string
- **match** match an entire string or substring base on a pattern
- **search** search for a pattern then a string
```python
    my_string = "Let's write RegEx!"
    PATTERN = "\w+"
    re.findall(PATTERN, my_string)

    output :
    ['Let', 's', 'write', 'RegEx']
```
- **finditer()** returns iterator
    - better for big data
    - scalable
    - can be process in real time
    - One-time use
    ```python
        matches = re.finditer(r"\d+", text)
        list(matches)  # ✅ works
        list(matches)  # ❌ empty
    ```
    - **findall** : EAGER
        - scans the entire string
        - builds a full list in memory
        - returns everything at once
        - slowdowns huge memory
        - memory crash
        - O(n) memory
        - allocates memory repeatedly
        - triggers garbage collection
        - CPU overhead from list building
        - recommended Usage :
            - small data
            - you just need values
            - quick scripting
    - **finditer** : LAZY
        - scans progressively
        - returns one match at a time
        - does NOT store everything
        - store only ONE match at a time
        - O(1) memory
        - minimal allocations
        - better CPU cache usage
        - smoother execution
        - recommended usage :
            - large files
            - streaming / pipelines
            - need positions
            - performance matters
            - production systems
    - Functionning explainaition :
        - findall:
            - scan whole text
            - create list
            - append each match
            - return list
            - costly operations:
                - list resizing
                - memory allocation
                - string copying
        - finditer:
            - create iterator object
            - each loop:
                - compute next match
                - yield it
            - discard previous match
            - no accumulation
    - Rich Match Object :
        - finditer() gives:
            match.group()
            match.start()
            match.end()
            match.span()

- **sub()** replace text
```python
    re.sub(r"\d", "X", "a1b2c3")
    # 'aXbXcX'
```

- It's important to prefix your regex patterns with **r** to ensure that your patterns are interpreted in the way you want them to. Else, you may encounter problems to do with escape sequences in strings. 
- For example, **"\n"** in Python is used to indicate a **new line**, but if you use the **r** prefix, it will be interpreted as the raw string **"\n"** - that is, the character "\" followed by the character "n" - and not as a new line.

- Grouping :
    - grouping is one of the most powerful feature in regex
    - Grouping is one of the most powerful features in regex
    - it allow to
        - Extract specific parts of a match
        - Organize patterns
        - Reuse parts of a regex
    - **First grouping method** : Parentheses () → Capturing Groups
    - Anything inside () is captured (stored) so you can reuse it
    ```python
        import re
        text = "My number is 123-456"
        match = re.search(r"(\d+)-(\d+)", text)

        print(match.group(1))  # 123
        print(match.group(2))  # 456
    ```
    - (\d+) → first group → numbers before - 
    - → literal dash
    - (\d+) → second group → numbers after -
    - Groups are numbered:
    - group(1) → first ()
    - group(2) → second ()
    - Why it’s powerful : **you extract structured data**
    - **Second grouping method** : Named Groups
    - Instead of numbers, you give names:
    ```python
        match = re.search(r"(?P<first>\d+)-(?P<second>\d+)", text)
        print(match.group("first"))   # 123
        print(match.group("second"))  # 456
    ```
    - Reusing Groups :
    ```python
        re.findall(r"(\w+)\s\1", "hello hello world")

        output :
        ['hello']
    ```
    - Non-capturing:
        - Use (?:...) when
        - you don’t need to extract
        - You just want grouping
        ```python
            (?:\d+)
        ```

- Flag (Modifiers) :
    - re.I ignore case (A = a)
    - re.M multiline (^ and $ work per line)
    - re.S dot matches newline (. includes newline)
    - can be combine (re.search(r"^hello.*world$", text, re.I | re.M | re.S))


#### Use case Regex: 
- only digits allowed :
```python
    re.match("^\d+$", "12345") # ✅ valid
    re.match(r"^\d+$", "123a5")  # ❌ invalid
```

- pattern  to match sentence endings (.?!) and split the sentence on the pattern
```python
    sentence_endings = r"[.?!]"
    print(re.split(sentence_endings, my_string))
```

- pattern to find(match)  all capitalized words in a sentence :
```python
    capitalized_words = r"[A-Z]\w+"
    print(re.findall(capitalized_words, my_string))
```

- pattern to split a sentence on spaces
```python
    spaces = r"\s"
    print(re.split(my_string, spaces))
```

- pattern to find all the digit in a string 
```python
    digits = r"\d"
    print(re.findall(digits, my_string))
```

- Extract date :
```python
    text = "Date: 2026-03-19"
    match = re.search(r"(\d{4})-(\d{2})-(\d{2})", text)

    year  = match.group(1)
    month = match.group(2)
    day   = match.group(3)
```

- Email :
```python
    pattern = r"[\w\.-]+@[\w\.-]+\.\w+"
```

- Phone Number :
```python
    pattern = r"\+?\d{1,3}[-]?\d{6,10}"
```

- url :
```python
    pattern = r"https?://[\w\.-]+"
```

- Get position of a match in a sentence
```python
    match = re.search("coconuts", scene_one)
    print(match.start(), match.end()) # Give the start and end indexes of match
```



### Tokenisation
- Tokenizasion is the process of turning a string or document into smaller chunk
- Those smaller chunk are called token
- One step in preparing a text for NLP
- They are many theory and rules and you can create your own rules
- In General tokenization does :
    - breaking out words and sentences
    - separating punctuation
    - separating all hashtags in a tweet
- **NLTK** is a common library use for tokenization
```python
    from nltk.tokenize import word_tokenize
    word_tokenize("Hi there!")

    output:
    ["Hi", "there", "!"]
```
- Why use tokenisation :
    - Easier to map part of speech
    - Matching common words
    - Removing unwanted tokens
    - Can help us see negation in a sentence
    - "I don't like Sam's shoes." =["I","do","n't","like","Sam","s","shoes","."]
- NLTK have many tokenizer : 
    - sent_tokenize : tokenise document into sentense 
    - regexp_tokenize : tokenize document or string base on regular expression
    - tweetTokeniser : Special class for tweet tokenisation, can separate hashtags, mentions and a lot of exclamation point
- Search VS Match :
    - **re.match** only match the pattern with the beginning of the string
    - **re.seach** will go though the entire string to findmatch

- **USE CASE** :
    - split document into sentences : 
        ```python
            from nltk.tokenize import sent_tokenize
            sentences = sent_tokenise(scene_one)
        ```
    - tokenise a sentence into words :
        ```python
            from nltk.tokenize import word_tokenize
            tokenize_words=word_tokenize(sentences[3])
        ```
    - get unique tokens of the entire document :
        ```python
            unique_tokens= set(word_tokenize(scene_one))
        ```

 