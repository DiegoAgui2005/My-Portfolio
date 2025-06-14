import asyncio
import time
import random
import multiprocessing

async def check_inventory(item):
    print(f"Checking inventory for {item}...")
    await asyncio.sleep(random.randint(3, 5))
    return random.choice([True, False])

async def process_payment(order_id):  # Fixed missing ":"
    print(f"Processing payment for order {order_id}...")
    await asyncio.sleep(random.randint(1, 3))
    print(f"Payment processed for order {order_id}.")
    return True

def calculate_total(items):  # Fixed function signature
    print(f"Calculating total for items...")
    time.sleep(5)  # Simulate time-consuming computation
    total = sum(item["price"] for item in items)
    print(f"Total cost for order: {total}.")
    return total

async def process_order(order_id, items):
    print(f"Processing order {order_id}...")

    # Check inventory asynchronously
    inventory_check = [check_inventory(item["name"]) for item in items]
    inventory_results = await asyncio.gather(*inventory_check)

    if not all(inventory_results):
        print(f"Order {order_id} cannot be processed due to insufficient inventory.")
        return  # Exit if inventory is insufficient

    # Use asyncio.to_thread() to avoid blocking in multiprocessing
    total = await asyncio.to_thread(calculate_total, items)

    # Process payment asynchronously
    payment_result = await process_payment(order_id)

    if payment_result:
        print(f"Order {order_id} has been successfully processed.")
    else:
        print(f"Order {order_id} payment failed.")

async def main():
    order_1 = [
        {"name": "item_1", "price": 10},
        {"name": "item_2", "price": 20}
    ]

    order_2 = [
        {"name": "item_3", "price": 30},
        {"name": "item_4", "price": 40}
    ]

    tasks = [process_order(1, order_1), process_order(2, order_2)]
    await asyncio.gather(*tasks)  # Ensures both orders run asynchronously

if __name__ == "__main__":
    asyncio.run(main())  # Run the event loop