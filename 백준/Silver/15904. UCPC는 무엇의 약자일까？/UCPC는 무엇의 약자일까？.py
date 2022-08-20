def main():
    txts = input()
    check = ['U', 'C', 'P', 'C']
    ci = 0
    for txt in txts:
        if ci == 4: break
        if txt == check[ci]:
            ci += 1

    return 'love' if ci == 4 else 'hate'

print(f'I {main()} UCPC')