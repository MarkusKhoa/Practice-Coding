n, t = map(int, input().split())
books = list(map(int, input().split()))
l, max_books, read_books = 0, 0, 0

for i in range(len(books)):
    while t < books[i]:
        read_books -= 1
        l += 1
        t += books[i]

    read_books += 1
    t -= books[i]
    max_books = max(max_books, read_books)

print(max_books)