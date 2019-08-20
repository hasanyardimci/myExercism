def slices(series, length):
    if len(series) > 0 and length > 0 and len(series) >= length:
        t = []
        for i in range(len(series) - length + 1):
            t.append(series[i:length + i])
        return t
    else:
        raise ValueError('A very specific bad thing happened.')
