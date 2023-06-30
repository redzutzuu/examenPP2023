from functional import seq
import asyncio
import re

coroutines_per_processing = 4


async def _elimin_spatii_multiple(partition: str):
    return re.sub("[ ]{2,}", ' ', partition)


async def elimin_spatii_multiple(text):
    # text = seq(open(file, 'r').readlines())
    partition_len = text.len() // coroutines_per_processing + 1
    partitions = []
    while text.len() > 0:
        partitions.append(text.take(partition_len).make_string(''))
        text = text.drop(partition_len)
    tasks = [asyncio.create_task(_elimin_spatii_multiple(partition)) for partition in partitions]
    new_text = ''.join([await task for task in tasks])
    return new_text


async def _elimin_salturi_linie_noua(partition: str):
    return partition.replace('\n', '')


async def elimin_salturi_linie_noua(text):
    partition_len = text.len() // coroutines_per_processing + 1
    partitions = []
    while text.len() > 0:
        partitions.append(text.take(partition_len).make_string(''))
        text = text.drop(partition_len)
    tasks = [asyncio.create_task(_elimin_salturi_linie_noua(partition)) for partition in partitions]
    new_text = ''.join([await task for task in tasks])
    return new_text


async def main():
    file = "economics_to_be_happier.txt"
    text = seq(open(file, 'r').readlines())
    task = asyncio.create_task(elimin_spatii_multiple(text))
    new_text = await task
    print(f"Dupa eliminarea spatiilor multiple:\n{new_text}")
    task = asyncio.create_task(elimin_salturi_linie_noua(seq(new_text)))
    new_text = await task
    print(f"Dupa eliminarea salturilor la linie noua:\n{new_text}")
    with open("OUTPUT.txt", 'w') as output:
        output.write(new_text)


asyncio.run(main())