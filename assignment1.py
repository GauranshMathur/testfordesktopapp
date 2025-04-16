def reverse_words(input_string):
    i = 0
    result = []
    
    while i < len(input_string):
        if not input_string[i].isalnum():
            result.append(input_string[i])
            i += 1
            continue
        
        word_chars = []
        word_indices = []
        
        while i < len(input_string) and input_string[i].isalnum():
            word_chars.append(input_string[i])
            word_indices.append(i)
            i += 1
        
        word_chars.reverse()
        
        for j in range(len(word_indices)):
            result.append(word_chars[j])
    
    return ''.join(result)

def test_reverse_words():
    test_cases = [
        ("Hello World", "olleH dlroW"),
        ("a1b2c3 d4e5f6", "3c2b1a 6f5e4d"),
        ("", ""),
        ("SingleWord", "droWelgniS"),
        ("Multiple   Spaces", "elpitluM   secapS"),
        ("!@#$%^&*()", "!@#$%^&*()"), 
        ("a", "a"),  
        ("1", "1"),  
        ("a1", "1a")  
    ]
    
    for input_string, expected in test_cases:
        result = reverse_words(input_string)
        assert result == expected, f"For input '{input_string}', expected '{expected}' but got '{result}'"
    
    print("All tests passed!")

if __name__ == "__main__":
    test_reverse_words()
