func numberOfSpecialChars(word string) int {
    var lowerCase [26]int
    var upperCase [26]int
    for i := 0; i < 26; i++ {
        lowerCase[i] = -1
        upperCase[i] = -1
    }

    for i := 0; i < len(word); i++ {
        chr := word[i]
        if (chr >= 'a') && (chr <= 'z') {
            lowerCase[chr - 'a'] = i
        } else if (chr >= 'A') && (chr <= 'Z') {
            index := chr - 'A'
            if (upperCase[index] == -1) {
                upperCase[index] = i
            }
        }
    }

    var result int
    for i := 0; i < 26; i++ {
        if (lowerCase[i] > -1 && upperCase[i] > -1 && lowerCase[i] < upperCase[i]) {
            result++
        }
    }
    return result
}