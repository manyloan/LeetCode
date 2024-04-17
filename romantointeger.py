def romanToInt(s: str) -> int:
        m = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        ans = 0
        index_char_atual = list(m.keys()).index(s[0])

        for i in range(len(s)):

            if i > 0:
                index_char_atual = list(m.keys()).index(s[i])

            if i+1 > len(s)-1:     
                index_char_proximo = list(m.keys()).index(s[i])
            else:
                index_char_proximo = list(m.keys()).index(s[i+1])

            diferenca_index = index_char_proximo - index_char_atual

            if diferenca_index > 0:
                ans -= m[s[i]]
            else:
                ans += m[s[i]]

        return ans

print(romanToInt('MCMXCIV'))
print(romanToInt('LVIII'))
print(romanToInt('III'))
#print(romanToInt('MCMXCIV'))

# validar se o index é menor somente que o proximo index
# IV = 4
# IX != 9
