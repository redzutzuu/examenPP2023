import re
import asyncio

class Handler:
    async def handleRequest(self, forwardDirection, messageToBeProcessed):
        pass

    def SetRight(self, right):
        pass

    def SetLeft(self, left):
        pass

    def SetVertical(self, vertical):
        pass


class CEOHandler(Handler):
    def __init__(self):
        self.right = None
        self.vertical = None

    async def handleRequest(self, forwardDirection, messageToBeProcessed):
        prioRegex = re.compile("^[0-9](?=\\:)")
        mesRegex = re.compile("(?<=\\:).+")
        prio = int(prioRegex.search(messageToBeProcessed).group())
        mes = mesRegex.search(messageToBeProcessed).group()
        if forwardDirection == "right":
            if prio == 1:
                print(f"Sunt CEO si prelucrez mesajul: \"{mes}\"...")
                await asyncio.sleep(0.2)
                asyncio.create_task(self.vertical.handleRequest("vertical", f"{prio}:Mesajul a fost prelucrat de catre CEO."))
            else:
                asyncio.create_task(self.right.handleRequest("right", messageToBeProcessed))
        elif forwardDirection in ["vertical", "left"]:
            if self.vertical is not None:
                print(f"Sunt CEO si transmit mai departe rezultatul unei prelucrari: \"{mes}\"")
                asyncio.create_task(self.vertical.handleRequest("vertical", messageToBeProcessed))
            else:
                print(f"Sunt CEO si am primit rezultatul unei prelucrari: \"{mes}\"")


    def SetRight(self, right):
        self.right = right

    def SetLeft(self, left):
        pass

    def SetVertical(self, vertical):
        self.vertical = vertical


class ExecutiveHandler(Handler):
    def __init__(self):
        self.right = None
        self.left = None
        self.vertical = None

    async def handleRequest(self, forwardDirection, messageToBeProcessed):
        prioRegex = re.compile("^[0-9](?=\\:)")
        mesRegex = re.compile("(?<=\\:).+")
        prio = int(prioRegex.search(messageToBeProcessed).group())
        mes = mesRegex.search(messageToBeProcessed).group()
        if forwardDirection == "right":
            if prio == 2:
                print(f"Sunt Executive si prelucrez mesajul: \"{mes}\"...")
                await asyncio.sleep(0.5)
                if self.vertical is not None:
                    asyncio.create_task(self.vertical.handleRequest("vertical", f"{prio}:Mesajul a fost prelucrat de catre Executive."))
                else:
                    asyncio.create_task(self.left.handleRequest("left", f"{prio}:Mesajul a fost prelucrat de catre Executive."))
            else:
                asyncio.create_task(self.right.handleRequest("right", messageToBeProcessed))
        elif forwardDirection == "vertical":
            print(f"Sunt Executive si transmit mai departe rezultatul unei prelucrari: \"{mes}\"")
            if self.vertical is not None:
                asyncio.create_task(self.vertical.handleRequest("vertical", messageToBeProcessed))
            else:
                asyncio.create_task(self.left.handleRequest("left", messageToBeProcessed))
        elif forwardDirection == "left":
            print(f"Sunt Executive si transmit mai departe rezultatul unei prelucrari: \"{mes}\"")
            asyncio.create_task(self.left.handleRequest("left", messageToBeProcessed))


    def SetRight(self, right):
        self.right = right

    def SetLeft(self, left):
        self.left = left

    def SetVertical(self, vertical):
        self.vertical = vertical


class ManagerHandler(Handler):
    def __init__(self):
        self.right = None
        self.left = None
        self.vertical = None

    async def handleRequest(self, forwardDirection, messageToBeProcessed):
        prioRegex = re.compile("^[0-9](?=\\:)")
        mesRegex = re.compile("(?<=\\:).+")
        prio = int(prioRegex.search(messageToBeProcessed).group())
        mes = mesRegex.search(messageToBeProcessed).group()
        if forwardDirection == "right":
            if prio == 3:
                print(f"Sunt Manager si prelucrez mesajul: \"{mes}\"...")
                await asyncio.sleep(0.8)
                if self.vertical is not None:
                    asyncio.create_task(self.vertical.handleRequest("vertical", f"{prio}:Mesajul \"{mes}\" a fost prelucrat de catre Manager."))
                else:
                    asyncio.create_task(self.left.handleRequest("left", f"{prio}:Mesajul \"{mes}\" a fost prelucrat de catre Manager."))
            else:
                asyncio.create_task(self.right.handleRequest("right", messageToBeProcessed))
        elif forwardDirection == "vertical":
            print(f"Sunt Manager si transmit mai departe rezultatul unei prelucrari: \"{mes}\"")
            if self.vertical is not None:
                asyncio.create_task(self.vertical.handleRequest("vertical", messageToBeProcessed))
            else:
                asyncio.create_task(self.left.handleRequest("left", messageToBeProcessed))
        elif forwardDirection == "left":
            print(f"Sunt Manager si transmit mai departe rezultatul unei prelucrari: \"{mes}\"")
            asyncio.create_task(self.left.handleRequest("left", messageToBeProcessed))


    def SetRight(self, right):
        self.right = right

    def SetLeft(self, left):
        self.left = left

    def SetVertical(self, vertical):
        self.vertical = vertical


class HappyWorkerHandler(Handler):
    def __init__(self):
        self.right = None
        self.left = None
        self.vertical = None

    async def handleRequest(self, forwardDirection, messageToBeProcessed):
        prioRegex = re.compile("^[0-9](?=\\:)")
        mesRegex = re.compile("(?<=\\:).+")
        prio = int(prioRegex.search(messageToBeProcessed).group())
        mes = mesRegex.search(messageToBeProcessed).group()
        if forwardDirection == "right":
            if prio == 4:
                print(f"Sunt HappyWorker si prelucrez mesajul: \"{mes}\"...")
                await asyncio.sleep(10)
                if self.vertical is not None:
                    asyncio.create_task(self.vertical.handleRequest("vertical", f"{prio}:Mesajul \"{mes}\" a fost prelucrat de catre HappyWorker."))
                else:
                    asyncio.create_task(self.left.handleRequest("left", f"{prio}:Mesajul \"{mes}\" a fost prelucrat de catre HappyWorker."))
            else:
                print(f"Sunt HappyWorker si nu am putut procesa mesajul \"{mes}\"")
                if self.vertical is not None:
                    asyncio.create_task(self.vertical.handleRequest("vertical", f"{prio}:Mesajul nu a putut fi procesat"))
                else:
                    asyncio.create_task(self.left.handleRequest("left", f"{prio}:Mesajul nu a putut fi procesat"))
        elif forwardDirection == "vertical":
            print(f"Sunt HappyWorker si transmit mai departe rezultatul unei prelucrari: \"{mes}\"")
            if self.vertical is not None:
                asyncio.create_task(self.vertical.handleRequest("vertical", messageToBeProcessed))
            else:
                asyncio.create_task(self.left.handleRequest("left", messageToBeProcessed))
        elif forwardDirection == "left":
            print(f"Sunt HappyWorker si transmit mai departe rezultatul unei prelucrari: \"{mes}\"")
            asyncio.create_task(self.left.handleRequest("left", messageToBeProcessed))


    def SetRight(self, right):
        self.right = right

    def SetLeft(self, left):
        self.left = left

    def SetVertical(self, vertical):
        self.vertical = vertical


class AbstractFactory:
    def getHandler(self, handler):
        pass


class EliteFactory(AbstractFactory):
    def getHandler(self, handler):
        if handler == "CEO":
            return CEOHandler()
        elif handler == "Executive":
            return ExecutiveHandler()
        else:
            return ManagerHandler()


class HappyWorkerFactory(AbstractFactory):
    def getHandler(self, handler):
        return HappyWorkerHandler()


class FactoryProducer:
    def getFactory(self, choice):
        if choice == "Elite":
            return EliteFactory()
        else:
            return HappyWorkerFactory()


async def main():
    factoryProducer = FactoryProducer()
    eliteFactory = factoryProducer.getFactory("Elite")
    happyWorkerFactory = factoryProducer.getFactory("HappyWorker")

    ceo1 = eliteFactory.getHandler("CEO")
    ceo2 = eliteFactory.getHandler("CEO")

    ex1 = eliteFactory.getHandler("Executive")
    ex2 = eliteFactory.getHandler("Executive")

    man1 = eliteFactory.getHandler("Manager")
    man2 = eliteFactory.getHandler("Manager")

    work1 = happyWorkerFactory.getHandler("HappyWorker")
    work2 = happyWorkerFactory.getHandler("HappyWorker")

    ceo1.SetRight(ex1)

    ex1.SetVertical(ex2)
    ex1.SetRight(man1)

    man1.SetRight(work1)
    man1.SetVertical(man2)

    work1.SetVertical(work2)

    ceo2.SetVertical(ceo1)

    ex2.SetLeft(ceo2)
    ex2.SetRight(man2)

    man2.SetLeft(ex2)
    man2.SetRight(work2)

    work2.SetLeft(man2)

    print("-" * 100)
    await ceo1.handleRequest("right", "4:Request")
    print("-" * 100)
    await man2.handleRequest("right", "3:Alt Request")
    print("-" * 100)
    await work1.handleRequest("right", "9:Request eronat")
    print("-" * 100)


asyncio.run(main())
