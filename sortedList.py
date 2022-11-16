from typing import Callable


class SortedList:
    def __init__(self, *values, key: Callable = None) -> None:
        # Sets internal values to what is given
        self.compareKey: Callable = key

        # Initializes values list
        self._values: list = []

        # Inserts constructor data
        self.insert(values)

    def insert(self, *values) -> None:
        """
        Inserts set of values to the list
        :param values: Values to be inserted
        """
        if self.compareKey is None:
            self._insert(values)
        else:
            self._insertKey(values)

    def _insert(self, *values) -> None:
        """
        Internal insertion function called when key was not set in constructor
        :param values: Values to be inserted
        """
        for element in values:
            # Initializes index range
            startIndex, stopIndex = 0, len(self._values)

            # Index at which value will be inserted
            index = 0
            # While the range exists:
            while stopIndex - startIndex > 1:

                # Get element approx in the middle
                index = (startIndex + stopIndex) // 2

                # If that's what you are inserting, insert at this position (break)
                if element == self._values[index]:
                    break

                # Else adjust index range
                elif element > self._values[index]:
                    startIndex = index
                elif element < self._values[index]:
                    stopIndex = index

            # After the element is found or range doesn't exist anymore, insert the element
            self._values.insert(index, element)

    def _insertKey(self, *values):
        """
        Internal insertion function called when key was set in constructor
        :param values: Values to be inserted
        """
        for element in values:
            # Initializes index range
            startIndex, stopIndex = 0, len(self._values)

            # Index at which value will be inserted
            index = 0

            # Uses the key to extract element values
            elementValue = self.compareKey(element)

            # While the range exists:
            while stopIndex - startIndex > 1:

                # Get element approx in the middle
                index = (startIndex + stopIndex) // 2

                # Uses the key to extract compared values
                comparedValue = self.compareKey(self._values[index])

                # If that's what you are inserting, insert at this position (break)
                if elementValue == comparedValue:
                    break

                # Else adjust index range
                elif elementValue > comparedValue:
                    startIndex = index
                elif elementValue < comparedValue:
                    stopIndex = index

            # After the element is found or range doesn't exist anymore, insert the element
            self._values.insert(index, element)

    def insertKey(self, *values, key: Callable):
        """
        Insertion function to override key set in constructor
        :param values: Values to be inserted
        :param key: Function to be used as a key
        """
        for element in values:
            # Initializes index range
            startIndex, stopIndex = 0, len(self._values)

            # Index at which value will be inserted
            index = 0

            # Uses the key to extract element values
            elementValue = key(element)

            # While the range exists:
            while stopIndex - startIndex > 1:

                # Get element approx in the middle
                index = (startIndex + stopIndex) // 2

                # Uses the key to extract compared values
                comparedValue = key(self._values[index])

                # If that's what you are inserting, insert at this position (break)
                if elementValue == comparedValue:
                    break

                # Else adjust index range
                elif elementValue > comparedValue:
                    startIndex = index
                elif elementValue < comparedValue:
                    stopIndex = index

            # After the element is found or range doesn't exist anymore, insert the element
            self._values.insert(index, element)

    def __contains__(self, item) -> bool:
        """
        Overrides default ... in ...
        :return: whether item is found in the list
        """
        # Calls proper function based on whether the key was set in constructor
        if self.compareKey is None:
            return self._contains(item)
        else:
            return self._containsKey(item)

    def _contains(self, element) -> bool:
        # Initializes index range
        startIndex, stopIndex = 0, len(self._values)

        # While the range exists:
        while stopIndex - startIndex > 1:

            # Get element approx in the middle
            index = (startIndex + stopIndex) // 2

            # Found
            if element == self._values[index]:
                return True

            # Else adjust index range
            elif element > self._values[index]:
                startIndex = index
            elif element < self._values[index]:
                stopIndex = index

        # Error 404
        return False

    def _containsKey(self, element) -> bool:
        # Initializes index range
        startIndex, stopIndex = 0, len(self._values)

        # Uses the key to extract element values
        elementValue = self.compareKey(element)

        # While the range exists:
        while stopIndex - startIndex > 1:

            # Get element approx in the middle
            index = (startIndex + stopIndex) // 2

            # Uses the key to extract compared values
            comparedValue = self.compareKey(self._values[index])

            # Found
            if elementValue == comparedValue:
                return True

            # Else adjust index range
            elif elementValue > comparedValue:
                startIndex = index
            elif elementValue < comparedValue:
                stopIndex = index

        # Error 404
        return False


def tests() -> None:
    pass


if __name__ == "__main__":
    tests()
