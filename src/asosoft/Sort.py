def kurdish_sort(inputList):
    # Kurdish alphabet in correct order
    ku = ["ئ", "ء", "ا", "آ", "أ", "إ", "ب", "پ", "ت", "ث",
          "ج", "چ", "ح", "خ", "د", "ڎ", "ڊ", "ذ", "ر", "ڕ",
          "ز", "ژ", "س", "ش", "ص", "ض", "ط", "ظ", "ع", "غ",
          "ف", "ڤ", "ق", "ك", "ک", "گ", "ڴ", "ل", "ڵ",
          "م", "ن", "و", "ۆ", "ۊ", "ۉ", "ۋ",
          "ه", "ھ", "ە", "ی", "ێ"]
    return CustomSort(inputList, ku)


def CustomSort(inputList, inputOrder):
    extended_ku = inputOrder + [chr(i) for i in range(128)]
    order_map = {ch: i for i, ch in enumerate(extended_ku)}

    def sort_key(s):
        # Convert each string to a list of its character order values,
        # with a fallback value that places unknown characters at the end.
        return [order_map.get(ch, len(extended_ku)) for ch in s]

    return sorted(inputList, key=sort_key)
