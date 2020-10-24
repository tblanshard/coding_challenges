# Solutions to various LeetCode challenges

#### At the moment, all using Python3 to solve the challenges.

- CreateTargetArray.py
- DecompressRLEList.py
- DefangingIP.py
- DestinationCity.py
  - Given a list of lists, such as [["A", "B"], ["B", "D"], ["F", "A"], where each pair is a set of two points with a directed path between them.
  - Find the "end point" - i.e. the point which doesn't lead anywhere - in this example, it would be "D" as F -> A -> B -> D
  - In my solution, I realised that the end point had to be the second element of a pair (as they are directed paths), and couldn't also appear as a first element in a pair.
    - I therefore filtered out the first elements and the second elements and found the difference between the second elements and the first elements (i.e. the elements that appeared in the second position, but not the first)
    - Because they were directed paths and there was only one element, I could then return this value.
- GoodPairs.py
- JewelsAndStones.py
- KidsWithCandies.py
- LinkedListBinaryNumber.py
- MiddleOfLinkedList.py
- ReduceToZero.py
- RunningSum1DArray.py
- ShuffleString.py
- ShuffleTheArray.py
- SmallerThanCurrent.py
- SplitStringBalancedString.py
- SubtractProductSum.py
- TwoSum.py
