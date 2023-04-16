# Write a program that takes a year (e.g. 1872) and outputs the century and decade (e.g. "Nineteenth Century, Seventies")

year = int(input("What year is the book you're looking for?: "))

if year >= 1800 and year <= 1810:
    print("Nineteenth Century")
elif year >= 1810 and year < 1820:
    print("Nineteenth Century, Tens")
elif year >= 1820 and year < 1830:
    print("Nineteenth Century, Twenties")
elif year >= 1830 and year < 1840:
    print("Nineteenth Century, Thirties")
elif year >= 1840 and year < 1850:
    print("Nineteenth Century, Fourties")
elif year >= 1850 and year < 1860:
    print("Nineteenth Century, Fifties")
elif year >= 1860 and year < 1870:
    print("Nineteenth Century, Sixties")
elif year >= 1870 and year < 1880:
    print("Nineteenth Century, Seventies")
elif year >= 1880 and year < 1890:
    print("Nineteenth Century, Eighties")
elif year >= 1890 and year < 1900:
    print("Nineteenth Century, Nineties")
elif year >= 1900 and year < 1910:
    print("Twentieth Century")
elif year >= 1910 and year < 1920:
    print("Twentieth Century, Tens")
elif year >= 1920 and year < 1930:
    print("Twentieth Century, Twenties")
elif year >= 1930 and year < 1940:
    print("Twentieth Century, Thirties")
elif year >= 1940 and year < 1950:
    print("Twentieth Century, Forties")
elif year >= 1950 and year < 1960:
    print("Twentieth Century, Fifties")
else:
    print("Oops we dont have any books in that year yet")
