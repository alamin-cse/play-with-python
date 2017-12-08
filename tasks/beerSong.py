word = "bottles"
for beerNo in range(99,0,-1):
    print(beerNo, word, "of beer on the wall.")
    print(beerNo, word, "of beer.")
    print("Take one down.")
    print("Pass it around,")
    if beerNo == 1:
        print("No more bottles of beer on the wall.")
    else:
        new_no = beerNo - 1
        if new_no == 1:
            word = "bottle"
        print(new_no, word , "of beer on the wall.")

    print()
