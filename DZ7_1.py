from random import randint

NUMBER_OF_TESTS = 1_000_000

theoretical_result = {
    2: 1 / 36,
    3: 2 / 36,
    4: 3 / 36,
    5: 4 / 36,
    6: 5 / 36,
    7: 6 / 36,
    8: 5 / 36,
    9: 4 / 36,
    10: 3 / 36,
    11: 2 / 36,
    12: 1 / 36,
}

test_results = {i: 0 for i in range(2, 13)}

for _ in range(NUMBER_OF_TESTS):
    s = randint(1, 6) + randint(1, 6)
    test_results[s] += 1

print(
    f"{'| Сума': <7} | {'теоретичний результат': <25} | {'практичний результат': <25}"
)
print(f"|{'-'*6} | {'-'*25} | {'-'*25}")
for i, value in test_results.items():
    print(
        f"| {i: <5} | {theoretical_result[i]:<25.5f} | {value/NUMBER_OF_TESTS:<25.5f}"
    )
