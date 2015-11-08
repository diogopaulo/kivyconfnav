def dollar_replace(string, replacements):
    for key, value in replacements.items():
        string = string.replace('$'+key+'$', value)
    return string
