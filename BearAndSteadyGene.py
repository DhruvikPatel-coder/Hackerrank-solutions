def steady_gene(gene):
    # Write your code here
    gene = list(gene)
    character_counter = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
    character_required = len(gene) / 4

    for i in range(len(gene)):
        character_counter[gene[i]] = character_counter[gene[i]] + 1

    # Check no of characters required to replace in order to balance the string
    string_required = {
        'A': max(0, int(character_counter['A'] - character_required)),
        'C': max(0, int(character_counter['C'] - character_required)),
        'G': max(0, int(character_counter['G'] - character_required)),
        'T': max(0, int(character_counter['T'] - character_required))
    }

    # If the string is balanced then return 0
    if string_required['A'] == 0 and string_required['C'] == 0 and string_required['G'] == 0 and string_required['T'] == 0:
        return 0

    result = dict()
    result['A'] = 0
    result['G'] = 0
    result['C'] = 0
    result['T'] = 0
    i = 0
    j = 0
    minimum_length = len(gene)
    # Follow a two pointer sliding window until j reaches to length of string
    while j < len(gene):
        result[gene[j]] += 1
        if result['A'] >= string_required['A'] and \
                result['C'] >= string_required['C'] and \
                result['G'] >= string_required['G'] and \
                result['T'] >= string_required['T']:
            # We will find a valid substring once all the characters have been used
            minimum_length = min(minimum_length, j - i + 1)

            # try to shorten it from the left side by removing unwanted characters
            while result[gene[i]] > string_required[gene[i]]:
                result[gene[i]] -= 1
                i += 1
                minimum_length = min(minimum_length, j - i + 1)
        j += 1

    return minimum_length


if __name__ == '__main__':
    my_str = input()
    print(steady_gene(my_str))
