def filmChoose2(flight_length, movie_lengths):
    if len(movie_lengths) <= 0:
        return False
    else:
        for i in range(len(movie_lengths)):
            for j in range(len(movie_lengths)):
                print("i: {}, j: {}".format(movie_lengths[i], movie_lengths[j]))
                if (i != j) and (movie_lengths[i] + movie_lengths[j] == flight_length):
                    return True
        return False

def quickSort(movies, low, high):
    if low < high:
        pi = partition(movies, low, high)
        quickSort(movies, low, pi - 1)
        quickSort(movies, pi + 1, high)
    return movies

def partition(movies, low, high):
    pivot = movies[high]
    i = low - 1
    for j in range(low, high):
        if movies[j] < pivot:
            i += 1
            temp = movies[j]
            movies[j] = movies[i]
            movies[i] = temp
    temp = movies[high]
    movies[high] = movies[i + 1]
    movies[i + 1] = temp
    return i + 1

def filmChoose(flight_length, movie_lengths):
    seen = set()
    quickSort(movie_lengths, 0, len(movie_lengths) - 1)
    for length in movie_lengths:
        if (flight_length - length) in seen:
            return True
        else:
            seen.add(length)
    return False



print(filmChoose(60, [30, 25, 120, 20]))
