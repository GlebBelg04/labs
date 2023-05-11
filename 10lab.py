def prog1():
    import os
    from pathlib import Path
    from PIL import Image

    source = Path("sourse")
    output= Path("output")

    if not source.exists():
        print(f"Source directory {source} does not exist")
        exit()

    if not output.exists():
        output.mkdir(parents=True)

    for filename in os.listdir(source):
        if filename.endswith(".jpg") or filename.endswith(".png") :

                image_path = source / filename
                with Image.open(image_path) as image:

                    image = image.rotate(90, expand=True)

                    target_path = output/ filename
                    image.save(target_path)


def prog2():

    import csv

    with open('data.csv') as f:
        reader = csv.reader(f)
        """next(reader)"""
        total_cost = 0
        items = []

        for row in reader:
            product = row[0]
            quantity = int(row[1])
            price = int(row[2])
            cost = quantity * price
            total_cost += cost
            items.append((product, quantity, price, cost))

    print("Нужно купить:")
    for item in items:
        print(f"{item[0]} - {item[1]} шт. за {item[2]} руб.")
    print(f"Итоговая сумма: {total_cost} руб.")

prog2()