class WrongBudget(Exception):
    pass


def greedy_algorythm(items, budget):
    # алгоритм жадібної обробки
    package = []
    total_calories = 0
    budget_remainder = budget
    food_efficiency = {
        key: int(items[key]["calories"]) / int(items[key]["cost"]) for key in items
    }

    while budget_remainder and len(food_efficiency):
        max_efficiency = 0
        max_key = ""
        for key in food_efficiency:
            if food_efficiency[key] > max_efficiency:
                max_efficiency = food_efficiency[key]
                max_key = key
        if items[max_key]["cost"] <= budget_remainder:
            package.append(max_key)
            total_calories += items[max_key]["calories"]
            budget_remainder -= items[max_key]["cost"]
            food_efficiency.pop(max_key)
        else:
            break

    return package, total_calories, budget_remainder


def get_cal_from_cost(items, cost):
    # Допоміжна функція, яка повертає калорійність, що відповідає вказаній вартості
    for key in items:
        if items[key]["cost"] == cost:
            return items[key]["calories"]


def get_item_from_cost(items, cost):
    # Допоміжна функція, яка повертає предмет, що відповідає вказаній вартості
    for key in items:
        if items[key]["cost"] == cost:
            return key


def dynamic_programming(items, budget):
    # алгоритм динамічного програмування

    # За основу беремо список з вартостями предметів
    cost = [int(items[key]["cost"]) for key in items]
    cost.sort()
    n = len(cost)

    K = [[0 for w in range(budget + 1)] for i in range(n + 1)]
    K_res = {}

    # будуємо таблицю K знизу вгору
    for i in range(n + 1):
        for w in range(budget + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
                K_res[(i, w)] = {}
            elif cost[i - 1] <= w:
                if (
                    get_cal_from_cost(items, cost[i - 1]) + K[i - 1][w - cost[i - 1]]
                    < K[i - 1][w]
                ):
                    K[i][w] = K[i - 1][w]
                    K_res[(i, w)] = K_res[(i - 1, w)]
                else:
                    K[i][w] = (
                        get_cal_from_cost(items, cost[i - 1])
                        + K[i - 1][w - cost[i - 1]]
                    )
                    K_res[(i, w)] = K_res[(i - 1, w - cost[i - 1])] | {
                        cost[i - 1]: True
                    }

            else:
                K[i][w] = K[i - 1][w]
                K_res[(i, w)] = K_res[(i - 1, w)]

    budget_remainder = budget
    package = []
    for cost in K_res[(n, budget)]:
        budget_remainder -= cost
        package.append(get_item_from_cost(items, cost))

    return package, K[n][budget], budget_remainder


if __name__ == "__main__":
    items = {
        "pizza": {"cost": 50, "calories": 300},
        "hamburger": {"cost": 40, "calories": 250},
        "hot-dog": {"cost": 30, "calories": 200},
        "pepsi": {"cost": 10, "calories": 100},
        "cola": {"cost": 15, "calories": 220},
        "potato": {"cost": 25, "calories": 350},
    }

    try:
        budget = int(input(f"Введіть бюджет\n"))
        if budget < 0:
            raise WrongBudget
    except (ValueError, WrongBudget):
        print("Помилка введення бюджета\n")

    food, total_calories, budget_remainder = greedy_algorythm(items, budget)
    print("Результат жадібного алгоритму")
    print(f"Пакет їжі складається з: {', '.join(f for f in food)}")
    print(f"Усього калорій: {total_calories}, залишок бюджету: {budget_remainder}")

    food, total_calories, budget_remainder = dynamic_programming(items, budget)
    print("Результат алгоритму динамічного програмування")
    print(f"Пакет їжі складається з: {', '.join(f for f in food)}")
    print(f"Усього калорій: {total_calories}, залишок бюджету: {budget_remainder}")
