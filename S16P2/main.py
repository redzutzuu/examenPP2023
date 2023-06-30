import asyncio
from concurrent.futures import ProcessPoolExecutor
from functools import partial


def multiply_constant(data, constant):
    result = {}
    for key, value in data.items():
        result[key] = value * constant
    return result


def add_elements(data):
    result = {}
    keys = list(data.keys())
    for i in range(len(keys)-1):
        result[keys[i]] = data[keys[i]] + data[keys[i+1]]
    return result


def replace_even_elements(data):
    result = {}
    for key, value in data.items():
        if value % 2 == 0:
            result[key] = 0
        else:
            result[key] = value
    return result


async def process_pipeline(data, constant):
    with ProcessPoolExecutor() as executor:
        processed_data = data.copy()
        pipeline_functions = [
            partial(multiply_constant, constant=constant),
            add_elements,
            replace_even_elements
        ]

        for pipeline_func in pipeline_functions:
            processed_data = await asyncio.get_event_loop().run_in_executor(executor, pipeline_func, processed_data)

        for key, value in processed_data.items():
            print(f"Key: {key}, Value: {value}")


if __name__ == "__main__":
    data = {
        "A": 1,
        "B": 2,
        "C": 3,
        "D": 4,
        "E": 5
    }

    constant = 2

    asyncio.run(process_pipeline(data, constant))
